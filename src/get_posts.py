#!/usr/bin/env python

from post import Post
import sys
import re

yearlyPostsFile=sys.argv[1]
file = open(yearlyPostsFile, "r")

postMap = {}
for line in file:
	#print(line)
	
	
	#strippedLine = re.sub('[\s+]', '', line)
	post = Post(line)
	#print(strippedLine)
	
	postDate = post.getDate()
	if postDate in postMap.keys():
	#	print(postMap[postDate])
		postMap[str(int(postDate) + 1)] = post.getContent()
	#	print(postMap[str(int(postDate) + 1)])
	else:
		postMap[postDate] = post.getContent()

keyList = postMap.keys().sort()
for key in sorted(postMap):
	print("key: " + str(key) +  " POST: " + str(postMap[key]))
