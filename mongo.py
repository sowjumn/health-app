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
import pymongo 
from pymongo import MongoClient
from bson import json_util

import appModel

app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)

#Get the Mongo database
mongo_uri_dict = pymongo.uri_parser.parse_uri(os.environ["MONGODB_URI"])
database_value_from_uri = mongo_uri_dict["database"]

client = MongoClient(os.environ["MONGODB_URI"])
db = client[database_value_from_uri]


def insertHealth(id, name, provider):
 	health = {"nameid": id, "name": name, "provider": provider} 
 	db.health.insert_one(health)

def getData():
 	collection = db.health.find()
 	health = []
 	for x in collection:
 		health.append(x)
 	return health