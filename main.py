import urllib2
import logging
import json
from google.appengine.ext import vendor
vendor.add('lib')

from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

@app.errorhandler(500)
def server_error(e):
    # Log the error and stacktrace.
    logging.exception('An error occurred during a request.')
    return 'An internal error occurred.', 500    

if __name__ == '__main__':
    app.run(debug=True)
