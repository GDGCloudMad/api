
import urllib2
import logging

HOST='http://api-website-159123.appspot.com'

response = urllib2.urlopen("{}/".format(HOST))
html = response.read()
print(html)
assert(html == "Hello, World!")
