#!/usr/bin/python

import praw
import argparse
import collections
import numpy as np
import matplotlib.pyplot as plt

subs = []
comsubs = []
nodupsubs = []
commentLabels = []
submitLabels = []
commentCount = []
submitCount = []

doxxit = praw.Reddit(user_agent='D0xxIt/0.1 by sgtscherer')
doxxit.config._ssl_url = None
doxxit.login('d0xxit', '')

todox = doxxit.get_redditor('')
submitted = todox.get_submitted(limit=None)
comments = todox.get_comments(limit=None)

def get_submitted_subs(submits):
#This function gets all the subreddits a user has submitted links or selfposts to
	
	subreddits = []

	for thing in submits:

		print thing
		sub = thing.subreddit.display_name
		subreddits.append(sub)

	return subreddits

def get_comment_subs(comms):
#This function gets all the subreddits a user has commented on.

	commented_subs = []

	for thing2 in comms:
		
		print thing2.subreddit.display_name
		commented_subs.append(thing2.subreddit.display_name)

	return commented_subs

def common_subs(submittedSubs,subreddits):
#This function lists each unique subreddit a user has submitted links to, and printss how many submissions along with it

	for n in submittedSubs.most_common(len(subreddits)):

		print n[0] + " " + str(n[1])

def common_comment_subs(commentsInSubs,commentedSubs):
#This function lists each unique subreddit a user has commented on, and prints how many comments

	for x in commentsInSubs.most_common(len(commentedSubs)):

		print x[0] + " " + str(x[1])

def sub_list(list_subs):
#This function takes a list full of subreddits and cuts out duplicates to return a list of unique subreddits

	newlist = []

	for i in list_subs:

		if i not in newlist:

			newlist.append(i)

	return newlist

subs = get_submitted_subs(submitted)
comsubs = get_comment_subs(comments)
countsubs = collections.Counter(subs)
countcoms = collections.Counter(comsubs)
nodupsubs = sub_list(subs)
common_subs(countsubs,subs)
common_comment_subs(countcoms,comsubs)
print nodupsubs
