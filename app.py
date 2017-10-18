import os
import logging
import redis
import appModel
from datetime import datetime, timedelta


from flask import Flask, request, render_template

app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)

@app.route('/captureshame')
def captureShame():
    vol = request.args.get("volume")
    appModel.captureShame(vol)
    return 'Shame Captured ' + vol + " " + str(datetime.utcnow())  

@app.route('/')
def home():
    health = appModel.getData()
    return render_template('index.html', data=health)

@app.route('/clearcache')
def clearCache():
	appModel.clearCache()
	return 'Cleared cache'

@app.route('/init')
def init():
	appModel.init()
	return "Initialized"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
