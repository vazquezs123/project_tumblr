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
	print("DATE: " + post.getDate())
	print("CONTENT: " + str(post.getContent()))
	print("YEAR: " + post.getYear())
	print("MONTH: " + post.getMonth())
