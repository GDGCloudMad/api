
import urllib2
import logging

HOST='http://api-website-159123.appspot.com'

response = urllib2.urlopen("{}/get_author/ulysses".format(HOST))
html = response.read()
assert(html == "James Joyce")