#!/usr/bin/python
from os import listdir
from os import path
import re

for fName in listdir("individual_posts"):
	filename = path.join("individual_posts",fName)
	file = open(filename)
	# get each line in file
	for line in file: 
		line = line.strip('<div class="')
		line = re.search('*', line)
		print line
			#with open(date, "w") as outFile:
			#	outFile.write(line)
