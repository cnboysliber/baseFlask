from application.models.testModel import Test
from application import session_scope


def add_test(**kwargs):
    with session_scope() as session:
        testObj = Test(**kwargs)
        session.add(testObj)
        session.flush()


def get_test(**kwargs):
    with session_scope() as session:
        q = session.query(Test).filter_by(id=kwargs.get('id', None))
        return [s.to_dict() for s in q]


def del_test(id):
    with session_scope() as session:
        session.query(Test).filter_by(id=id).update({'status': 0})


def modify_test(**kwargs):
    id = kwargs.pop('id')
    with session_scope() as session:
        session.query(Test).filter_by(id=id).update(kwargs)

