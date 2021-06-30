# this file just stores some variables
import praw
from nrclex import NRCLex
import sys
import statsmodels
import numpy as np
from scipy.stats import ttest_ind, shapiro, chisquare
import matplotlib.pyplot as plt
import angry_os_functions as functions
from multiprocessing import Pool
from os import system 
print("from angry_os.py")
# --------- set up reddit object -------------------------------
#+this reddit object will spawn 
f = open("/home/brian/Documents/python/praw/secure_angry_os", "r")
id = f.readline()[:-1]
secret = f.readline()[:-1]
agent = f.readline()[:-1]
#reddit = praw.Reddit(client_id= id, client_secret = secret, user_agent = agent)
# ------------------ actually use functions here ------------------------------
def call_file(file_name=""):
    system("python {}".format("file_name"))

files_to_call = ("r_linux.py", "r_osx.py")
num_processes = 2
pool = Pool(processes=num_processes)
#pool.map(call_file, files_to_call)
limit = 100
#windows_scores = []
linux_words = ['linux', 'ubuntu', 'gnome', 'kde']
mac_words = ['mac', 'osx', 'macintosh', 'macos', 'macbook', 'apple']
windows_words = ['windows10', 'windows7', 'microsoft', 'windowsxp']
#linux_sub_scores, linux_comment_scores ,linux_sub_sents ,linux_com_sents= functions.get_score_arrays(reddit.subreddit('linux'),size,linux_words, windows_words + mac_words, lambda x: x != 0)
#linux_scores = linux_comment_scores + linux_sub_scores
#mac_sub_scores, mac_comment_scores, mac_sub_sents ,mac_com_sents = functions.get_score_arrays(reddit.subreddit('osx'),size,mac_words, windows_words + linux_words, lambda x: x != 0)
#mac_scores = mac_sub_scores + mac_comment_scores
# ---------------------------- printing results ----------------
#t_val, p_val = ttest_ind(linux_scores, mac_scores,equal_var = False)
#print('linux_scores has length:',len(linux_scores))
#print("mac_scores has length:", len(mac_scores))
#print("score for linux = ", sum(linux_scores)/len(linux_scores), sep="")
#print("score for mac = ", sum(mac_scores)/len(mac_scores), sep="")
#print("P test for linux vs. mac", p_val)
#print("LINUX P value for normality using shapiro:", shapiro(linux_scores))
#print("MAC P value for normality using shapiro:", shapiro(mac_scores))
##print("chisquare:", chisquare(linux_scores[:83], mac_scores))
## ---------- create a historgram to represent data
#plt.hist(linux_scores,bins=50)
#plt.savefig("linux_plot.png")
#plt.hist(mac_scores, bins=50)
#plt.savefig("mac_plot.png")
#plt.figure()
#plt.hist(linux_com_sents + linux_sub_sents, bins=50)
#plt.hist(mac_sub_sents+mac_com_sents, bins=50)
#plt.savefig("linux_mac_sent.png")


