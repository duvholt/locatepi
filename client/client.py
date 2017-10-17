from gql import Client, gql
from gql.transport.requests import RequestsHTTPTransport
import logging
import config
import time

logging.basicConfig(format='%(asctime)s %(message)s', level=logging.DEBUG)
logger = logging.getLogger('pinger')


class Pinger:
    def __init__(self, server_name, api_key):
        self.server_name = server_name
        self.api_key = api_key
        requests_transport = RequestsHTTPTransport(
            config.BACKEND_URL
        )
        self.gql_client = Client(transport=requests_transport)

    def ping(self):
        query = gql(f'''
        mutation {{
          createPing(serverName: "{self.server_name}", apiKey: "{self.api_key}") {{
            ok
          }}
        }}
        ''')
        result = self.gql_client.execute(query)['createPing']
        if result['ok']:
            logger.debug('Successfully pinged')
        else:
            logger.error('Failed to create ping')

    def start(self):
        logger.info(f'Started pinger against server {self.server_name}')
        while True:
            self.ping()
            time.sleep(config.PING_INTERVAL)


if __name__ == '__main__':
    pinger = Pinger(config.SERVER_NAME, config.API_KEY)
    pinger.start()
