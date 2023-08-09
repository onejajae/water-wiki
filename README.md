# Water Wiki

## Backend
### Prerequisites
* Python 3.10+ (If lower, python cannot check some types)
* virtualenv
### Installation
```
water-wiki$ cd backend/
water-wiki/backend$ virtualenv venv --python=python3.10
water-wiki/backend$ source venv/bin/activate
(venv) water-wiki/backend$ pip install -r requirments.txt
```
## Frontend
### Prerequisites
* nodejs 16+
### Installation
```
water-wiki$ cd frontend/
water-wiki/frontend$ npm i
```

## Deployment
### Prerequisites
* docker
* docker-compose-plugin
### Build Docker Image
```
water-wiki$ docker compose build
```
### Write .env Files
* Write `.env.prod` into `backend/`
* Write `.env.production` into `frontend/`
### Run
```
water-wiki$ docker compose up
```
