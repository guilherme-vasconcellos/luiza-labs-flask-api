# Luiza Labs Hiring Test - Employees Manager

Employees manager is an api to manage employees data.

# Tech area

Dependencies used on development:

- Python v3.7.4
- MySQL v5.7

The application is written in python3 with flask micro framework and mysql as database.

# How to use

## Prepare development environment
*Note: Assuming you have a mysql db with schema named Employee*

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

## Start database
```sh
docker run --name mysql -p 3306:3306 -e MYSQL_DATABASE=Employee -e MYSQL_ROOT_PASSWORD=root mysql:5.7
```

## Install dependencies
```sh
pipm install
```

## Run integration tests (Needs an instance of mysql running with schema named Employee)
```sh
pytest
```

## Start application
```sh
python src\server.py
```
