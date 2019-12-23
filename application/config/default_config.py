
# -*- coding:utf-8 -*-
import os

web_root = os.path.abspath(os.path.join(__file__, os.pardir, os.pardir, os.pardir))

DEBUG = True
HOST = '0.0.0.0'
PORT = 9091

DB_URI = 'mysql+pymysql://hjx:123456@119.29.141.207/flask_base'
DB_POOL_SIZE = 5
DB_POOL_RECYCLE = 5
DB_MAX_OVERFLOW = 10
DB_ECHO = False
