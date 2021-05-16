PYTHON=/home/brian/anaconda3/bin/python
SHELL=/bin/bash
PATH=/home/brian/Documents/python/praw/angry_os
OS: $(cat os_list)
.PHONY: $(OS) affect_$(OS) done
a b c:
	$(touch a b c)
done: a b c
