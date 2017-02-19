import urllib2
import json
from google.appengine.ext import vendor
vendor.add('lib')

from flask import Flask
app = Flask(__name__)

from api_key import key

@app.route('/get_author/<title>')
def get_author(title):
    host = 'https://www.googleapis.com/books/v1/volumes?q={}&key={}&country=US'.format(title, key)
    request = urllib2.Request(host)
    try:
        response = urllib2.urlopen(request)
    except urllib2.HTTPError, error:
        contents = error.read()
        print ('Received error from Books API {}'.format(contents))
        return str(contents)
    html = response.read()
    author = json.loads(html)['items'][0]['volumeInfo']['authors'][0]
    return author

if __name__ == '__main__':
    app.run(debug=True)
