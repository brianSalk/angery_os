import praw
from nrclex import NRCLex
import sys
"""
def get_comments_and_posts(sub, limit = 10):
    text = []
    for each in sub.new(limit=limit):
        text.append(each.selftext)
        for comment in each.comments:
            text.append(each.selftext)
    return ''.join(text)
"""
def get_comments_and_posts(sub, limit = 10):
    text = ""
    for each in sub.new(limit=limit):
        text += (each.selftext)
        for comment in each.comments:
            text += (comment.body)
    return text

def get_comments_and_posts_for(sub, limit=10,search_for=""):
    text = ""
    count = 0
    for each in sub.new(limit=limit):
        text += each.selftext
        count += 1
        for comment in each.comments:
            text += comment.body
f = open("/home/brian/Documents/python/praw/secure_angry_os", "r")
id = f.readline()[:-1]
secret = f.readline()[:-1]
agent = f.readline()[:-1]
reddit = praw.Reddit(client_id= id, client_secret = secret, user_agent = agent)

subreddit_name = sys.argv[1]
OS_text = get_comments_and_posts(reddit.subreddit(subreddit_name),30)

print(subreddit_name + ":",NRCLex(OS_text).affect_frequencies["anger"])

# find all comments and posts that contian EXACTLY one of the following words.
# linux, windows, mac
# from there, look at the posts manually to make sure the posts are pertinent
# if a post is not pertinent (I opened all my windows), then remove it from the output file and subtract one from the count
# after submissions/comments have been inspected, use the formula:
# (scores[i]/number_of_posts_containing_OS_TYPE)
# to determine which operating system causes the most anger.
# possibly also use textblob to check whether the polarity was positive/negative.


