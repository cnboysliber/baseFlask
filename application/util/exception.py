import sys
import traceback

from flask import jsonify
from functools import wraps


def try_except(fn):
    @wraps(fn)
    def wrapped(*args, **kwargs):
        try:
            return fn(*args, **kwargs)
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            error_str = 'Function name: {0}; Error info: {1}: {2}; Traceback: {3}'\
                .format(str(fn.__name__),
                        str(e.__class__.__name__),
                        str(e),
                        str(traceback.extract_tb(exc_tb)))
            return jsonify({'success': False, 'error': str(error_str)})
    return wrapped

