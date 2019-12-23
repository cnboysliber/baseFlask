# -*- coding:utf-8 -*-


class AppError(Exception):
    def __init__(self, code, message):
        self.code = code
        self.message = message

    def __str__(self):
        return '<%d %s>' % (self.code, self.message)


ErrArgs = AppError(2000, '参数错误')
ErrInternal = AppError(2001, '服务内部错误')




