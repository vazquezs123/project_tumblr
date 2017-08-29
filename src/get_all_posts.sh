#!/bin/bash

#posts_dir=../tumblr_posts/tumblr_*_posts
for post in ../tumblr_posts/tumblr_*_posts
do
	echo $post
	python ./get_posts.py $post	
done
