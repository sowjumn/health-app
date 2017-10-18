import os
import logging
import redis
import random
import psycopg2
import jsonpickle
import sys
import healthModel
import json
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime, timedelta
from flask import Flask, request, render_template

app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)

try: 
    logging.debug(os.environ["KUBERNETES_SERVICE_HOST"])
    DB_IP = os.environ["POSTGRES_SERVICE_PORT_5432_TCP_ADDR"]
    DB_PORT = os.environ["POSTGRES_SERVICE_PORT_5432_TCP_PORT"]
    DATABASE_URL="postgres://" + DB_IP + ":" + DB_PORT
except:
    DATABASE_URL=os.environ["DATABASE_URL"]
    pass

#init db session
engine = create_engine(DATABASE_URL, echo=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)

def getData():
    logging.debug("get data from postgres")
    session = Session()
    shame = session.query(healthModel.Health).all()
    return shame
  
def insertHealth(nameid, a1c):
    session = Session()
    health = healthModel.Health(nameid, a1c)
    session.add(health)
    session.commit()

def createSchema():
    if not engine.dialect.has_table(engine, 'healthdata'):
        healthModel.createDbSchema(engine)
        logging.debug("creating db schema")
    else:
        logging.debug("db schema already exists") 

