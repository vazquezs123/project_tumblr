#!/bin/bash

# get tumblr posts
FILES=/home/svaquez/project_tumblr/tumblr_posts/yearly_posts/

# make file 
find $FILES -type f -name 'tumblr_201*' -exec cut {} -f6 -d'/' >> all_posts.txt \;

