from __future__ import absolute_import
import os
import sys
_basedir = os.path.abspath(os.path.dirname(__file__))
if _basedir not in sys.path:
    sys.path.insert(0, _basedir)

from werkzeug.serving import run_simple
from application import app
from application.controller import register_blueprints

register_blueprints(app)

if __name__ == '__main__':
    run_simple(app.config['HOST'], app.config['PORT'], app)
