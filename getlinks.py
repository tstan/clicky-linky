from BeautifulSoup import BeautifulSoup
import urllib2
import re

def getLinks():
    html_page = urllib2.urlopen("http://www.textfiles.com/art/")
    soup = BeautifulSoup(html_page)
    for link in soup.findAll('a'):
        print "http://www.textfiles.com/art/" + link.get('href')

getLinks()