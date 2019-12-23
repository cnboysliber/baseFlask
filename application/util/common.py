import time
from flask import request, current_app
from flask import jsonify as flask_jsonify


def jsonify(interface, has_error=False, data=None, output=True):
    out = {
        '_head': {
            '_version': current_app.__version__,
            '_msgType': 'response',
            '_interface': interface,
            '_remark': '',
            '_timestamps': time.time()
        },
        '_data': {
            '_errCode': None,
            '_errStr': None,
            '_ret': None
        }
    }

    if has_error:
        out['_data']['_errCode'] = data.code
        out['_data']['_errStr'] = data.message
        out['_data']['_ret'] = -1
    else:
        out['_data']['_errCode'] = 0
        out['_data']['_errStr'] = 'ok'
        out['_data']['_ret'] = 0
        if data is not None:
            out['_data']['retData'] = data

    if current_app.debug and output:
        print('<%s> <%s>' % (request.path, str(out)))

    return flask_jsonify(out)



