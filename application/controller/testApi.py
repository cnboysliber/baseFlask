from flask import request, jsonify

from application import app
from application.middles import testMiddle as m
from application.util.exception import try_except


@app.route('/get_test_info', methods=['POST'])
@try_except
def get_test_info():
    params = request.get_json(force=True)
    result = m.get_test(**params)
    return jsonify({'success': True, 'res': result})




