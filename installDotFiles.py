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

#install VIM plugins with the Pathogen plugin
#install pahthogen
#mkdir ~/.vim/autoload ~/.vim/bundle
#pull down     https://raw.github.com/tpope/vim-pathogen/master/autoload/pathogen.vim
#into ~/.vim/autoload

#TODO, put these into ~/.vim/bundle
#git clone git://github.com/tpope/vim-fugitive.git
#git clone git://github.com/tpope/vim-rails.git
#git clone git://github.com/tpope/vim-bundler.git
#git@github.com:tpope/vim-surround.git
#git clone https://github.com/scrooloose/nerdtree.git
#git@github.com:kien/ctrlp.vim.git


