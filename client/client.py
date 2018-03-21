from gql import Client, gql
from gql.transport.requests import RequestsHTTPTransport
import logging
import config
import time
import socket

logging.basicConfig(format='%(asctime)s %(message)s', level=logging.DEBUG)
logger = logging.getLogger('pinger')


class Pinger:
    def __init__(self, server_key, api_key):
        self.server_key = server_key
        self.api_key = api_key
        requests_transport = RequestsHTTPTransport(
            config.BACKEND_URL
        )
        self.gql_client = Client(transport=requests_transport)

    def ping(self):
        query = gql('''
        mutation {{
          createPing(
            serverKey: "{server_key}",
            apiKey: "{api_key}",
            localIp: "{find_local_ip}"
          ) {{
            ok
          }}
        }}
        '''.format(
            server_key=self.server_key,
            api_key=self.api_key,
            find_local_ip=self.find_local_ip())
        )
        result = self.gql_client.execute(query)['createPing']
        if result['ok']:
            logger.debug('Successfully pinged')
        else:
            logger.error('Failed to create ping')

    def start(self):
        logger.info('Started pinger against server {}'.format(self.server_key))
        while True:
            self.ping()
            time.sleep(config.PING_INTERVAL)

    def find_local_ip(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip


if __name__ == '__main__':
    pinger = Pinger(config.SERVER_KEY, config.API_KEY)
    pinger.start()
