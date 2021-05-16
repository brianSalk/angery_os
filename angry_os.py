import praw
from nrclex import NRCLex
import sys
import statsmodels
import numpy as np
from scipy.stats import ttest_ind
import matplotlib.pyplot as plt
# --------- functions
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


def get_score_if(each, search_for=None, exclude=None):
        has_search_word = False
        has_exclude_word = False
        for word in exclude:
            if word in each:
                has_exclude_word = True
                break
        if has_exclude_word:
            return -1
        for word in search_for:
            if word in each:
                has_search_word = True
                break
        if has_search_word:
            return NRCLex(each).affect_frequencies['anger']

def get_comments_and_posts_mean_for(sub, limit=10,search_for=[], exclude = [], arr=[], condition=True):
    anger_score = 0
    for submission in sub.new(limit=limit):
        submission_text = submission.selftext.lower()
        submission.comments.replace_more(limit=None)
        submission_score = get_score_if(submission_text, search_for, exclude) 
        if condition(submission_score):
            arr.append(submission_score)
        for comment in submission.comments:
            comment_text = comment.body.lower()
            score = get_score_if(comment_text,search_for, exclude)
            if condition(score):
                arr.append(score)
    print("count:",len(arr))
# --------- set up reddit object -------------------------------

f = open("/home/brian/Documents/python/praw/secure_angry_os", "r")
id = f.readline()[:-1]
secret = f.readline()[:-1]
agent = f.readline()[:-1]
reddit = praw.Reddit(client_id= id, client_secret = secret, user_agent = agent)
# ------------------ actually use code here ------------------------------
mac_scores = []
linux_scores = []
windows_scores = []
get_comments_and_posts_mean_for(reddit.subreddit("linux"), 100, ["linux", "ubuntu", "gnome"], ["windows", "mac", "osx", "windows10", "window7"], linux_scores,condition = lambda x: x != None and x > 0)
get_comments_and_posts_mean_for(reddit.subreddit("osx"), 10, ["mac", "osx", "apple","macintosh"], ["windows", "linux", "ubuntu", "debian", "windows10", "windows7"], mac_scores, condition = lambda x: x != None and x > 0)
get_comments_and_posts_mean_for(reddit.subreddit("windows10"), 10, ["windows10", "windows7", "microsoft"], ["mac", "osx", "linux"], condition = lambda x: x != None and x > 0)
# ---------------------------- printing results
t_val, p_val = ttest_ind(linux_scores, mac_scores,equal_var = False)
print("score for linux = ", sum(linux_scores)/len(linux_scores), sep="")
print("score for mac = ", sum(mac_scores)/len(mac_scores), sep="")
print("P test for linux vs. mac", p_val)
# ---------- create a historgram to represent data
plt.hist(linux_scores,bins=100)
plt.savefig("linux_plot.png")
