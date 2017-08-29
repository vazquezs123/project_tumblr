#!/usr/bin/env python

from post import Post
import re

file = open("/home/svaquez/project_tumblr/tumblr_posts/tumblr_2010_posts", "r")

for line in file:
	#print(line)
	
	
	#strippedLine = re.sub('[\s+]', '', line)
	post = Post(line)
	#print(strippedLine)
	print("DATE: " + post.getDate())
	print("CONTENT: " + str(post.getContent()))
	print("YEAR: " + post.getYear())
	print("MONTH: " + post.getMonth())
