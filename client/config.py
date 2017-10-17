from decouple import config

BACKEND_URL = config('NC_BACKEND_URL', default='http://localhost:8000/graphql')
SERVER_NAME = config('NC_SERVER_NAME')
API_KEY = config('NC_API_KEY')
PING_INTERVAL = config('NC_PING_INTERVAL', default=5 * 60)
