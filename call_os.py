# this file calls the os.py program with different arguments
from multiprocessing import Pool
from os import system

# execute each file containing one or more calls to a praw function here.
#+this will allow us to run all of them in parallel
def call_file(file_name=""):
    system("python {}".format(file_name))

num_proc = 3
pool = Pool(processes=num_proc)
oss = ["mac", "linux", "windows"]
subreddits = ["linux", "osx", "windows10", "computerscience"]
files_to_call = []

for each_os in oss:
    for each_subreddit in subreddits:
        files_to_call.append("os.py " + each_subreddit + " " + each_os)
interprets = []     
for each_os in oss:
    interprets.append("interpret_.py " + each_os)

pool.map(call_file, files_to_call)
print("ALL DONE!!!!!!!!!!!!!!!!!!!!!\n\n\n\n")
pool.map(call_file, interprets)

system("ls shelf | xargs -I{} rm shelf/{}")
