# Locatepi

An health check solution for devices without static IPs. 

## Architecture

The project is split in three parts: backend, frontend and ping client. 

### Backend

The backend is a GraphQL API written in Python using Django and Graphene.   
Django's built-in admin is used to manage servers at http://localhost:8000/admin

#### How to start

```bash
cd backend
# Set up virtualenv or similar
pip install -p requirements.txt
./manage.py migrate
./manage.py runserver
# Runs on localhost:8000 by default
```

### Frontend

The frontend is written in React and Relay. It displays the devices along with their last known IP and last health ping. 

#### How to start
```bash
cd frontend
npm install # or yarn
npm start
# Runs on localhost:3000 by default
```

### Ping client

This application should run on all devices that needs health check. It's a simple Python script that sends a ping every five minutes to the backend. 

#### Environment config

|Key             |Description|Default|
|:---------------|:----------|:------|
|NC_BACKEND_URL  |Full URL to the GraphQL backend including /graphql|http://localhost:8000/graphql|
|NC_SERVER_KEY  |The device server key||
|NC_API_KEY      |API key corrosponding to the server key||
|NC_PING_INTERVAL|How often to ping in seconds|300(5 min)|

#### How to start

```bash
cd client
# Set up virtualenv or similar
pip install -p requirements.txt
# Set up environment variables
python client.py
```


## Update GraphQL schema

Every time the backend's schema is updated the frontend also needs to be updated. 

```bash
./backend/manage.py graphql_schema # Creates schema.json
cd frontend
npm run buildSchema
npm run relay
```
