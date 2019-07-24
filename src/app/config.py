import os

# Environment config
ENV = os.getenv('FLASK_ENV', 'development')
DEBUG = ENV == 'development'

SERVER_NAME = os.getenv('SERVER_NAME', '127.0.0.1:8000')

# Datase config
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_DATABASE_URI = os.getenv(
    'MYSQL_URI', 'mysql+pymysql://root:root@localhost:3306/Employee')
