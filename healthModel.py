from flask import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import *

app = Flask(__name__)
Base = declarative_base()

class Health(Base):
    __tablename__ = 'healthdata'

    id = Column(Integer, autoincrement=True, primary_key=True)
    nameid = Column('nameid', String(32))
    a1c = Column('a1c', Integer())

    def __init__(self, nameid, a1c):
        self.nameid = nameid
        self.a1c = a1c

def createDbSchema(engine):
	Base.metadata.create_all(engine)
	