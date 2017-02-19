import urllib2
import json
from google.appengine.ext import vendor
vendor.add('lib')

from flask import Flask
app = Flask(__name__)

from api_key import key

@app.route('/')
def index():
    return "Hello, World!"

if __name__ == '__main__':
    app.run(debug=True)
