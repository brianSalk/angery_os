from nrclex import NRCLex
from textblob import TextBlob
import re
def get_score_arrays(the_subreddit, limit=10, search_for=[], exclude = [], condition= lambda x: True):
    submission_scores = []
    comment_scores = []
    for each_submission in the_subreddit.new(limit=limit):
        submission_selftext = each_submission.selftext.lower()
        submission_score = get_score(submission_selftext, search_for, exclude)
        if submission_score != None and condition(submission_score):
            submission_scores.append(submission_score)
        each_submission.comments.replace_more(limit=None)
        for each_comment in each_submission.comments.list(): 
            comment_body = each_comment.body.lower()
            comment_score = get_score(comment_body, search_for, exclude)
            if comment_score != None and condition(comment_score):
                comment_scores.append(comment_score)
    return submission_scores, comment_scores

def get_score(text, search_for, exclude):
    for exclude_word in exclude:
        if re.search("\\b" + exclude_word + "\\b", text):
            return None
    for include_word in search_for:
        if re.search("\\b" + include_word + "\\b", text):
            return NRCLex(text).affect_frequencies['anger']
    return None

# find   
#def get_pro(the_subreddit = "", search_for = [], exclude = [], condition = lambda x: True ):
    
