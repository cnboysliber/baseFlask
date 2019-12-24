import os
import random
import string
from contextlib import contextmanager
from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool
from application.controller import register_blueprints

from application.config import default_config

web_root = os.path.abspath(os.path.join(__file__, os.pardir, os.pardir))

app = Flask(
    __name__,
)

# 设置加载
app.config.from_object(default_config)

app.__version__ = '2.0.0'
# for session
app.secret_key = ''.join(random.choices(string.ascii_letters + str('0123456789'), k=40))


# 数据库连接方式为单链接，即一个链接完成即关闭，也可以采用其他链接方式，只需配不同参数即可
engine = create_engine(app.config['DB_URI'] + '?charset=utf8',
                       encoding='utf-8',
                       convert_unicode=True,
                       poolclass=NullPool,
                       echo=app.config['DB_ECHO'],
                       pool_pre_ping=True)

# SQLAlchemy session
session_factory = sessionmaker(bind=engine)


@contextmanager
def session_scope():
    session = session_factory()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()

