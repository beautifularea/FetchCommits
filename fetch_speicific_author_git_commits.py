# -*- coding: utf-8 -*-
import commands
import sys

class Author:
    name = ""

    ''' If author name is nil , default fetch all commits by all authors'''

    def get_git_author(self):
    	if len(sys.argv) < 2:
    		print 'No author specific'
        else :
        	self.name = sys.argv[1]

class Fetch:
    author = ""
    status = ""
    ret = ""

    def __init__(self, author):
 	    self.author = author

    def fetch_all_commit(self):
    	command = 'git log --author=' + self.author.name
    	st, ret = commands.getstatusoutput(command)
        self.status = st
        self.ret = ret 	

    def print_all_commit(self):
        print self.ret    

#author
author = Author()
author.get_git_author()

#fetch
fetch = Fetch(author)
fetch.fetch_all_commit()
fetch.print_all_commit()