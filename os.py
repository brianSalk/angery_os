# this is the file that gets called by call_os.py
#it takes two CLAs, the first one is the subreddit, the second is the os
import angry_os
import praw
import angry_os_functions
import shelve
import sys
print("calling",sys.argv[0], sys.argv[1], sys.argv[2])
subreddit_to_search = sys.argv[1]
os = sys.argv[2]
exclude_words = []
search_words = []
if (sys.argv[2] == "linux"):
    exclude_words = angry_os.windows_words + angry_os.mac_words
    search_words = angry_os.linux_words
elif (sys.argv[2] == "windows"):
    exclude_words = angry_os.linux_words + angry_os.mac_words
    search_words = angry_os.windows_words
else:
    exclude_words = angry_os.windows_words + angry_os.linux_words
    search_words = angry_os.mac_words
# shelves to a file called shelf/{user defined CLA}.out
reddit = praw.Reddit(client_id=angry_os.id,
        client_secret = angry_os.secret, 
        user_agent=angry_os.agent,
        condition=lambda x: x != 0)

sub_scores, comment_scores = angry_os_functions.get_score_arrays(the_subreddit=reddit.subreddit(subreddit_to_search),
        limit=100, 
        search_for=search_words, 
        exclude= exclude_words)
os_scores = sub_scores + comment_scores
my_shelf = shelve.open('shelf/{}.out'.format(os))
# check if os_scores exists in shelf/os.out
try:
    os_scores_from_shelf = my_shelf["os_scores"]
    os_scores_from_shelf = os_scores_from_shelf + os_scores
    my_shelf["os_scores"] = os_scores_from_shelf
    print("appended to list")
except Exception:
    # if there is no os_scores, shelf the current one
    my_shelf["os_scores"] = os_scores
    print("added the list because it did not exist")



my_shelf.close()
print("os is done executing")
