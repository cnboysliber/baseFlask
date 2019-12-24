# -*- coding:utf-8 -*-
from __future__ import absolute_import
import os
import sys
_basedir = os.path.abspath(os.path.dirname(__file__))
if _basedir not in sys.path:
    sys.path.insert(0, _basedir)
# from application.config.default_config import HOST, PORT
bind = "{ip}:{port}".format(ip='0.0.0.0', port=9091)
backlog = 2048

workers = 4
worker_connections = 1000
max_requests = 0
timeout = 30

daemon = False



