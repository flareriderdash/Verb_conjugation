#!/usr/bin/python

import sys
import os
import cPickle as pickle

	#Gets Dictonary with keys and conjugation sheets
if len(sys.argv) == 9 or len(sys.argv) == 3:
	sheets = pickle.load(open("dict","rb"))

try:

	if sys.argv[1] != "--remove-key":
		try:
			#		generates the list from arguements and appends to dictonary 
			#		and saves in pickle file for verb_conjugation.py to access
			#		and writes to the .Word file that tells the content of the
			#		dictonary and the english meaning then closes files.
			#----------------------------------------------------------------------------
			infinative="                "+sys.argv[1]+"\n"
			template1 ="             yo         "+"\033[31m"+sys.argv[2]+"\033[0m"+"\n"
			template2 ="             tu         "+"\033[31m"+sys.argv[3]+"\033[0m"+"\n"
			template3 ="     el/ella/UD         "+"\033[31m"+sys.argv[4]+"\033[0m"+"\n"
			template4 ="       nosotros         "+"\033[31m"+sys.argv[5]+"\033[0m"+"\n"
			template5 ="       vosotros         "+"\033[31m"+sys.argv[6]+"\033[0m"+"\n"
			template6 ="ellos/ellas/Uds         "+"\033[31m"+sys.argv[7]+"\033[0m"+"\n"
			list = [infinative , template1 , template2 , template3 ,template4, template5 , template6]
			cake = ""
			for i in list:
				cake += i
			if len(sys.argv) == 9:
				sheets[sys.argv[1]]=cake
				pickle.dump(sheets,open('dict','wb'))
				file2 = open(".Words","a+")
				if len(sys.argv[1]) < 6:
					file2.write(sys.argv[1]+"		English: "+sys.argv[8]+"\n")
				else:
					file2.write(sys.argv[1]+"	English: "+sys.argv[8]+"\n")
			file2.close()
			#-----------------------------------------------------------------------------


		# Sets a error message if there arent enough agruments
		except IndexError:
			print "\nPlace a list of the infinative and then the conjucations\n\nFor example:\n\033[31m addtable.py yo tu el/ella/Ud nosotros vosotros ellos/ellas/Uds english_meaning\033[0m\n this will create a table for those infinatives\nIf you want to remove a word from the list just type --remove-key and then the key/word\n"
	

	#	runs and removes a key in the sheets
	#	dictonary if the first argument is 
	#	--remove-key and uses the aregument
	#	after that to delete the key
	#-------------------------------------------------
	else:
		del sheets[sys.argv[2]]
		pickle.dump(sheets,open('dict','wb'))
	#-------------------------------------------------

#Sets error message if there arent enough arguments
except IndexError:
	print "\nPlace a list of the infinative and then the conjucations\n\nFor example:\n\033[32maddtable.py yo tu el/ella/Ud nosotros vosotros ellos/ellas/Uds english_meaning\033[0m\nthis will create a table for those infinatives\nIf you want to remove a word from the list just type --remove-key and then the key\n"

