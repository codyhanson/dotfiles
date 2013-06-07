#!/usr/bin/env python

import sys
import os

homedir = os.getenv("HOME")
curdir = os.getcwd()

print "home: ", homedir
print "cwd: ", curdir

dotfiles = []

dotfiles.append(".vimrc")
dotfiles.append(".screenrc")


#if dotfiles already exist, confirm with user before overwriting.
for dotfilename in dotfiles:
    dotfilepath = curdir+ '/' + dotfilename
    linkpath = homedir + '/' + dotfilename
    if (os.path.exists(linkpath) is True):
        #link exists
        sys.stdout.write("{0} exists, clobber? (y/n):".format("linkpath"))
        choice = sys.stdin.read(2) #read choice + \n 
        choice = choice.rstrip()
        if (choice == 'Y' or choice == 'y'):
            os.remove(linkpath)
            os.symlink(dotfilepath,linkpath)
            print "{0} -> {1}".format(dotfilepath,linkpath)
        else:
            print "skipping {0}".format(dotfilename)
    else:
        os.symlink(dotfilepath,linkpath)
        print "{0} -> {1}".format(dotfilepath,linkpath)

