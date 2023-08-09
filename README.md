# Water Wiki
A portal for bottled-spring-water information that has been manufactured and sold in Korea.

## Backend
### 1. Prerequisites
* Python 3.10+ (If lower, python cannot check some types)
* virtualenv
### 2. Installation
```
water-wiki$ cd backend/
water-wiki/backend$ virtualenv venv --python=python3.10
water-wiki/backend$ source venv/bin/activate
(venv) water-wiki/backend$ pip install -r requirments.txt
```

## Frontend
### 1. Prerequisites
* nodejs 16+
### 2. Installation
```
water-wiki$ cd frontend/
water-wiki/frontend$ npm i
```

## Deployment
### 1. Prerequisites
* docker
* docker-compose-plugin
### 2. Build Docker Image
```
water-wiki$ docker compose build
```
### 3. Write .env Files
* Write `.env.prod` into `backend/`
* Write `.env.production` into `frontend/`
### 4. Run
```
water-wiki$ docker compose up
```
