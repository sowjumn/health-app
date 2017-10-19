import os
import logging
import redis
import random
import psycopg2
import jsonpickle
import sys
import json
import random
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime, timedelta
from flask import Flask, request, render_template, jsonify
from pymongo import MongoClient
from bson import json_util

import cache
import mongo
import postgres

import salesforce
import requests

app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)

caching_enabled = os.environ["CACHING_ENABLED"]
riskUrl = os.environ["RISK_URL"]

def uniqueName(name):
    newName = name.replace(" ", "").lower()
    print(newName)
    return newName

def combineData(providerData, bloodData):
    combined = []
    aoneDict = []

    for y in bloodData:
        aoneDict.append(y.a1c)

    risks = getRisks(aoneDict)

    for x in providerData:
        for index, y in enumerate(bloodData):
            if x["nameid"] == y.nameid:
                risk = risks[index] 
                user = { 'name': x["name"], 'provider': x["provider"], 'a1c': round(float(y.a1c / 100),1), 'risk': risk }
                combined.append(user)
    return combined

def getRisks(risks):
    risksJson = json.dumps(risks)
    r = requests.post(riskUrl, data=risksJson)
    return r.json()

def getData():
    data = ""
    logging.debug("is_caching_enabled:" + caching_enabled)

    if caching_enabled == "true": 
       data = cache.get()
    
    if data == "":
        providerData = mongo.getData()
        bloodData = postgres.getData()
        data = combineData(providerData, bloodData)
        
    if caching_enabled == "true":
        cache.set(data)
    return data
    
def insertInitData():
    names = salesforce.getData()
    providers = ["Aetna", "Blue Cross", "Kasier", "Oscar", "United", "Humana"]

    for x in names:
        insertProviderData(x, random.choice(providers))
        insertA1C(x, random.randint(450, 1000))

def insertProviderData(name, provider):
    data = mongo.insertHealth(uniqueName(name), name, provider)
        
def insertA1C(name, a1c):
    data = postgres.insertHealth(uniqueName(name), a1c)
    
def init():
    if caching_enabled == "true":
        cache.clear()

    #Create the DB schmea if it doesn't exist
    postgres.createSchema()
    
    #Add init data if it doesn't exist 
    data = getData()
    if len(data) == 0:
        insertInitData()
