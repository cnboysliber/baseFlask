# -*- coding:utf-8 -*-
from __future__ import absolute_import
import os
import sys
_basedir = os.path.abspath(os.path.dirname(__file__))
if _basedir not in sys.path:
    sys.path.insert(0, _basedir)

from application import app
from application.controller import register_blueprints

register_blueprints(app)

if __name__ == '__main__':
    app.run(app.config['HOST'], app.config['PORT'])
