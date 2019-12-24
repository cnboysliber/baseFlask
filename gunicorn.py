# -*- coding:utf-8 -*-
from application.config.default_config import HOST, PORT
bind = "{ip}:{port}".format(ip=HOST, port=PORT)
backlog = 2048

workers = 4
worker_connections = 1000
max_requests = 0
timeout = 30

daemon = False



