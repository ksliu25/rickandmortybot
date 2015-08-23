import praw
import pdb
import re
import os
import random
from config_bot import *
from catchphrase import *

if not os.path.isfile("config_bot.py"):
	print "You must create a config file with username and password!"
	exit(1)

if not os.path.isfile("catchphrase.py"):
	print "You need a catchphrase database bruh"
	exit(1)

user_agent = ("rick_and_morty robo 0.1")
r = praw.Reddit(user_agent = user_agent)

r.login(REDDIT_USERNAME, REDDIT_PASS)


#ensure comments text
if not os.path.isfile("comments_replied_to.txt"):
	comments_replied_to = []

else:
	with open("comments_replied_to.txt", "r") as f:
		comments_replied_to = f.read()
		comments_replied_to = comments_replied_to.split("\n")
		comments_replied_to = filter(None, comments_replied_to)

	# Code to look through comments
subreddit = r.get_subreddit("pythonforengineers")
subreddit_comments = subreddit.get_comments()
for comment in subreddit_comments:
	if re.search("rickandmortybot.rick",comment.body, re.IGNORECASE) and comment.id not in comments_replied_to:
		comment.reply("RICK: " + random.choice(RICK_CATCHPHRASES)+ "\n\n*I am maintained by /u/Crispy-snax*")
		print "Bot replying to : ",comment.body
		comments_replied_to.append(comment.id)
	elif re.search("rickandmortybot.morty",comment.body, re.IGNORECASE) and comment.id not in comments_replied_to:
		comment.reply("MORTY: " + random.choice(MORTY_CATCHPHRASES)+ "\n\n*I am maintained by /u/Crispy-snax*")
		print "Bot replying to : ",comment.body
		comments_replied_to.append(comment.id)        	
	elif re.search("rickandmortybot",comment.body, re.IGNORECASE) and comment.id not in comments_replied_to:
		comment.reply(random.choice(SHOW_CATCHPHRASES) + "\n\n*I am maintained by /u/Crispy-snax*")
		print "Bot replying to : ",comment.body
		comments_replied_to.append(comment.id)


with open("comments_replied_to.txt", "w") as f:
	for comments_id in comments_replied_to:
		f.write(comments_id + "\n")

# if not os.path.isfile("posts_replied_to.txt"):
# 	posts_replied_to = []

# else:
# 	with open("posts_replied_to.txt", "r") as f:
# 		posts_replied_to = f.read()
# 		posts_replied_to = posts_replied_to.split("\n")
# 		posts_replied_to = filter(None, posts_replied_to)

##REPLYING TO POSTS


# subreddit = r.get_subreddit('pythonforengineers')
# for submission in subreddit.get_hot(limit=5):

# 	if submission.id not in posts_replied_to:

# 		if re.search("rickandmortytest", submission.title, re.IGNORECASE):

# 			submission.add_comment("GRASSSSS.... TASTES BAD-UH")
# 			print "Bot replying to : ", submission.title

#         # Store the current id into our list
#         posts_replied_to.append(submission.id)

# 			# Write our updated list back to the file
# with open("posts_replied_to.txt", "w") as f:
# 	for post_id in posts_replied_to:
# 		f.write(post_id + "\n")



