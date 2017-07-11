# -*- coding: utf-8 -*-

# DATABASE SETTINGS
pg_db_username = 'appusr'
pg_db_password = 'aplicacao'
pg_db_name = 'beerfactorydb'
pg_db_hostname = '192.168.0.10'


DEBUG = True
PORT = 5050
HOST = "0.0.0.0"
SECRET_KEY = "chavesecreta@paraAaplicacao"

LOG_ACTIVE = True
LOG_LEVEL = 'DEBUG'
LOG_PATH = '/var/log/beerfactory'
LOG_FILENAME = 'beerfactory.log'

UPLOAD_FOLDER = '/var/www/html/beerfactory/images'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
URL_IMAGES='http://192.168.0.10/beerfactory/images'



SQLALCHEMY_ECHO = True
SQLALCHEMY_TRACK_MODIFICATIONS = True



# import os
#
# basedir = os.path.abspath(os.path.dirname(__file__))
# databaseDir = basedir+os.sep+'db'
# if not  os.path.exists(databaseDir):
#     os.makedirs(databaseDir)


# PostgreSQL
SQLALCHEMY_DATABASE_URI = "postgresql://{DB_USER}:{DB_PASS}@{DB_ADDR}/{DB_NAME}".format(DB_USER=pg_db_username,
                                                                                        DB_PASS=pg_db_password,
                                                                                        DB_ADDR=pg_db_hostname,
                                                                                        DB_NAME=pg_db_name)


# SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(databaseDir, 'app.sqlite')
# SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')


try:
    from config_local import *
except ImportError:
    pass
