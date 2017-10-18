import os
import logging
import redis
import random
import psycopg2
import jsonpickle
import sys
import healthModel
import json
from datetime import datetime, timedelta
from flask import Flask, request, render_template

app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)

try: 
    REDIS_URL=os.environ["REDIS_SERVICE_PORT_6379_TCP"]
except:
    REDIS_URL=os.environ["REDIS_URL"]
    pass

#init cache
rserver = redis.from_url(REDIS_URL)

def set(data):
    rserver.set("shameData", jsonpickle.encode(data))

def get():
    shame = ""   
    fromCache = rserver.get("shameData")
    if fromCache is not None:
        shame = jsonpickle.decode(fromCache)
        logging.debug("retrieved from Cache")
    return shame
    

def clear():
    rserver.delete("shameData")