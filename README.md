# Reddit_Bot

# Overview
Reddit Bot that will reply to comments if criteria is met.

# Requierments 
Python version 3.3+

Windows, MacOS, Linux

Libraries - Praw

# Instructions
To use this bot you must first place both reddit_bot.py & bot_info.py in the same folder, following this you need to enter your reddit credentials into the bot_info.py file. Now that you have the code you need to change some information.

First - You will want to change the User_Agent to another name that will relate to what your bot is doing.

Second - Change the subreddit you wish to search in line 42.

Third - Change line 50 if comment.body == "build a wall" and replace "build a wall" with whatever the comment you wish to reply to is. For example if you want to reply to anyone who asks "What is the speed of light".

Fourth - Following this you will want to change line 52 comment.reply("Oops, the wall never even got planning permission") to in relation to the previous example "The speed of light is - 186,282 miles per second".

# Example

I shall post an example of this bot in action soon.
