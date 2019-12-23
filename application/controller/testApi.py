from flask import request
from flask import blueprints

from application import app
from application.middles import testMiddle as m
from application.controller import route

bp = blueprints.Blueprint(app, __name__, url_prefix='/example')


@route(bp, '/get_test_info', methods=['POST'])
def get_test_info():
    params = request.get_json(force=True)
    result = m.get_test(**params)
    return result




