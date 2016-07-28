#!/usr/bin/python

import urllib
import os
import time
import re

def filter_func(char):
    return ord(char)>32 or ord(char) < 126

def downloadAll():
	links = []

	try:
		file = open('links.txt', 'r')
	except IOError:
		print('[ERROR] Where is your "links.txt" file?\nProgram exits with no action.')
		return

	with open("links.txt") as linksfile:
		links = linksfile.readlines()
	dirname = time.strftime("%m%d%Y") + "files"

	if not os.path.exists(dirname):
		os.makedirs(dirname)

	i = 0
	while (i < len(links)):
		delim = links[i].split('/')
		s = delim[len(delim)-1]
		urllib.urlretrieve(links[i], dirname+"/"+re.sub("\s+", "", s))
		print('Downloaded ' + s)
		i+=1

	print('[SUCCESS] Files downloaded to directory named `' + dirname + '`. \nProgram exits with success!')

if __name__ == "__main__":
	downloadAll()