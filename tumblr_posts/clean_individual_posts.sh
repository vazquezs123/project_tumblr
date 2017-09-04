#!bin/sh
grep -o \<p.*\</p /home/svaquez/tumblr_posts/individual_posts/* > /home/svaquez/tumblr_posts/tumblr_dictionary

#clean dictionary
perl -pi.back -e 's/<p>//g;' tumblr_dictionary

perl -pi.back -e 's/<\/p//g;' tumblr_dictionary

perl -pi.back -e 's/<br \/>//g;' tumblr_dictionary

perl -pi.back -e 's/&nbsp//g;' tumblr_dictionary

perl -pi.back -e 's/&rsquo;/'\''/g;' tumblr_dictionary

perl -pi.back -e 's/&hellip;/.../g;' tumblr_dictionary

perl -pi.back -e 's/&quot;/"/g;' tumblr_dictionary

perl -pi.back -e 's/&ldquo;/"/g;' tumblr_dictionary

perl -pi.back -e 's/&rdquo;/"/g;' tumblr_dictionary

perl -pi.back -e 's/&lt;/</g;' tumblr_dictionary

perl -pi.back -e 's/&gt;/>/g;' tumblr_dictionary

perl -pi.back -e 's/&mdash;/-/g;' tumblr_dictionary

perl -pi.back -e 's/&ndash;/-/g;' tumblr_dictionary

perl -pi.back -e 's/&amp;/&/g;' tumblr_dictionary

grep 2010 tumblr_dictionary > tumblr_2010_posts

grep 2011 tumblr_dictionary > tumblr_2011_posts

grep 2012 tumblr_dictionary > tumblr_2012_posts

grep 2013 tumblr_dictionary > tumblr_2013_posts

grep 2014 tumblr_dictionary > tumblr_2014_posts

grep 2015 tumblr_dictionary > tumblr_2015_posts
