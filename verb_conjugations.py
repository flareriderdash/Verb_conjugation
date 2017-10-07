#!/usr/bin/python

import cPickle as pickle
import sys
sheet = pickle.load(open('dict','rb'))

try:
	try:
		print sheet[str(sys.argv[1])]
	except KeyError:
		print "\n\033[32mOops Word Not In Dictonary, Try Again\033[0m\n"
except IndexError:
	
	file = open(".Words", "r")
	file = file.read(10000)
	print
	print "\033[36mAvalible Searches"
	print "-----------------\033[0m" 
	print file
	print
	
