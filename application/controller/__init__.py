# -*- coding: utf-8 -*-

from __future__ import absolute_import

import traceback
import pkgutil
import importlib
from functools import wraps

from flask import request
from flask.blueprints import Blueprint
from voluptuous import MultipleInvalid
from werkzeug import exceptions as wkerr

from application.error import ErrArgs, ErrInternal
from application.util.common import jsonify


def route(bp, *args, **kwargs):
    output = kwargs.pop('output') if 'output' in kwargs else True

    def decorator(f):
        @bp.route(*args, **kwargs)
        @wraps(f)
        def wrapper(*args, **kwargs):
            try:
                rv = f(*args, **kwargs)
            except (wkerr.BadRequest, MultipleInvalid) as e:
                # 入参get_json解析错误会抛BadRequest
                print(111111, traceback.format_exc())
                return jsonify(request.path, has_error=True, data=ErrArgs)
            except Exception:
                print(traceback.format_exc())
                print(2222222, traceback.format_exc())
                return jsonify(request.path, has_error=True, data=ErrInternal)

            return jsonify(request.path, data=rv, output=output)

        return f

    return decorator


def register_blueprints(app):
    rv = []
    for _, name, _ in pkgutil.iter_modules(__path__):
        m = importlib.import_module("%s.%s" % (__name__, name))
        for item in dir(m):
            item = getattr(m, item)
            if isinstance(item, Blueprint):
                app.register_blueprint(item)
            rv.append(item)
    return rv




