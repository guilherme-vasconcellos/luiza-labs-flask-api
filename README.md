# Luiza Labs Hiring Test - Employees Manager

Employees manager is an api to manage employees data.

# Tech area

Dependencies used on development:

- Python v3.7.4
- Docker v18.09.2
- MySQL v5.7

The application is written in python3 with flask micro framework and mysql as database.

Docker is used to run the application in "production mode" and guarantee their functionality in different environments.

# How to use

## Prepare development environment
```sh
# Install virtualenv
pip install virtualenv

# Create virtual environment
virtualenv .venv

# Activate the environment (Follow the steps according your SO)

# Windows
.venv\Scripts\activate.bat

# Linux / Mac OS
.venv/bin/activate

# Install package manager for development
pip install pipm
```

## Install dependencies
```sh
pipm install --all
```

## Run integration tests (Needs an instance of mysql running)
```sh
pytest
```

## Build application
```sh
docker-compose build
```

## Start application
```sh
# Development
python src\server.py

# Production
docker-compose up
```
