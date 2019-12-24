from werkzeug.serving import run_simple
from application import app
from application.controller import register_blueprints

register_blueprints(app)

if __name__ == '__main__':
    run_simple(hostname=app.config['HOST'], port=app.config['PORT'], application=app)
