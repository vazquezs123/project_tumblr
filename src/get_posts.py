#!/usr/bin/env python

from post import Post
import sys
import re

postsFile=sys.argv[1]
file = open(postsFile, "r")

for line in file:
	#print(line)
	
	
	#strippedLine = re.sub('[\s+]', '', line)
	post = Post(line)
	#print(strippedLine)
	print("DATE: " + post.getDate() + "---CONTENT: " + str(post.getContent()) + "---YEAR: " + post.getYear() + "---MONTH: " + post.getMonth())
