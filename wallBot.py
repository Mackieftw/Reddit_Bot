#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Import Required Libraries

import praw
import pdb
import re
import os
import time
import datetime
from bot_info import *

now = datetime.datetime.now() #sets datetime with system
current_hour = now.hour #takes hours from the now var  (Maybe change from 24 hour time)
current_min = now.minute #takes mins from the now var

#Set up User agent for session and login to Reddit
user_agent = ("WallPlanning v0.1")
r = praw.Reddit(user_agent = user_agent)

r.login(REDDIT_USERNAME, REDDIT_PASS)
t = 1

while t > 0:
	
	
#Checks if a file is created to save replied comment.id's to. 
# This will stop you from replying to the sae comment multiple times.
	if not os.path.isfile("Replied_To.txt"):
	Replied_To = []
#If the file already exists, opens and reads.	
	else:
		with open ("Replied_To.txt", "r") as f:
			Replied_To = f.read()
			Replied_To = Replied_To.split("\n")
			Replied_To = filter(None, Replied_To)


#Now we setup the subreddit we want to check, I picked Politics.
#Following this, setup comment reading in said subreddit and a limiter.(This is to go with Reddit API rules)
	subreddit = r.get_subreddit("politics")
	comments = subreddit.get_comments(limit=100)
#Here we check through the comments of the Hottest 5 posts, 
#Check for crieteria (This case build a wall) and if met reply to it
	for comments in subreddit.get_hot(limit=5):
	
		if comment.id not in Replied_To:
		
			if comment.body == "build a wall" :
			
				comment.reply("Oops, the wall never even got planning permission")
			
				print ("Bot replied to", subreddit, submission.id, comment.id)
			
				Replied_To.append(comment.id)
#Write the comment.id to a file to prevent us from commenting again
	with open ("Replied_To.txt", "W") as f:
		for post_id in Replied_To:
			f.write(comment.id + "\n")
			time.sleep(3600)
