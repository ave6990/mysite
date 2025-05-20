import os

class Config:
  SECRET_KEY = os.environ.get('SECRET_KEY') or "enter"
  SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
    f'mariadb+mariadbconnector://ave:{SECRET_KEY}@192.168.0.118:3306/midb'
  RECORDS_LIMIT = 100
