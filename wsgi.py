from werkzeug.serving import run_simple
from application.config import default_config as cfg
from application import app
from application.controller import register_blueprints

register_blueprints(app)

if __name__ == '__main__':
    run_simple(hostname=cfg.HOST, port=cfg.PORT, application=app)
