import os
import logging
import redis
import appModel
from datetime import datetime, timedelta


from flask import Flask, request, render_template

app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)


@app.route('/')
def home():
    health = appModel.getData()
    return render_template('index.html', data=health)

@app.route('/init')
def init():
	appModel.init()
	return "Initialized"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
