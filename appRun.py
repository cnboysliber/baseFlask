from application import app
from application.controller import register_blueprints

register_blueprints(app)

if __name__ == '__main__':
    app.run(host=app.config['HOST'], port=app.config['PORT'])
