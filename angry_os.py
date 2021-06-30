import praw
from nrclex import NRCLex
import sys
import statsmodels
import numpy as np
from scipy.stats import ttest_ind, shapiro, chisquare
import matplotlib.pyplot as plt
import angry_os_functions as functions
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
# ------------------ actually use functions here ------------------------------
size = 1000000
windows_scores = []
linux_words = ['linux', 'ubuntu', 'gnome', 'kde']
mac_words = ['mac', 'osx', 'macintosh', 'macos', 'macbook', 'apple']
windows_words = ['windows10', 'windows7', 'microsoft']
linux_sub_scores, linux_comment_scores= functions.get_score_arrays(reddit.subreddit('linux'),size,linux_words, windows_words + mac_words, lambda x: x != 0)
linux_scores = linux_comment_scores + linux_sub_scores
mac_sub_scores, mac_comment_scores = functions.get_score_arrays(reddit.subreddit('osx'),size,mac_words, windows_words + linux_words, lambda x: x != 0)
mac_scores = mac_sub_scores + mac_comment_scores
# ---------------------------- printing results ----------------
t_val, p_val = ttest_ind(linux_scores, mac_scores,equal_var = False)
print('linux_scores has length:',len(linux_scores))
print("mac_scores has length:", len(mac_scores))
print("score for linux = ", sum(linux_scores)/len(linux_scores), sep="")
print("score for mac = ", sum(mac_scores)/len(mac_scores), sep="")
print("P test for linux vs. mac", p_val)
print("LINUX P value for normality using shapiro:", shapiro(linux_scores))
print("MAC P value for normality using shapiro:", shapiro(mac_scores))
print("chisquare:", chisquare(linux_scores, mac_scores))
# ---------- create a historgram to represent data
plt.hist(linux_scores,bins=50)
plt.savefig("linux_plot.png")
plt.hist(mac_scores, bins=50)
plt.savefig("mac_plot.png")

