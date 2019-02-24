from datetime import datetime

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime

from application import engine


Base = declarative_base()


class Test(Base):
    __tablename__ = 'test'
    __table_args__ = {
        "mysql_engine": "InnoDB",
        "mysql_charset": "utf8"
    }

    id = Column(Integer, primary_key=True)
    test_name = Column(String(64), nullable=False)
    status = Column(Integer, default=1, nullable=False)
    update_time = Column(DateTime, default=datetime.now, nullable=False)
    create_time = Column(DateTime, default=datetime.now, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'test_name': self.test_name,
            'update_time': self.update_time,
            'create_time': self.create_time
        }


Base.metadata.create_all(engine)
