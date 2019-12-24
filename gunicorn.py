# -*- coding:utf-8 -*-
# from application.config.default_config import HOST, PORT
bind = "{ip}:{port}".format(ip='0.0.0.0', port=9091)
backlog = 2048

workers = 4
worker_connections = 1000
max_requests = 0
timeout = 30

daemon = False



