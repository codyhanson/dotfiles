#!/usr/bin/env python

import sys
import os
#https://github.com/kennethreitz/requests
import requests

homedir = os.getenv("HOME")
curdir = os.getcwd()
print "home: " + homedir
print "cwd: " +  curdir

dotfiles = ['.vimrc', '.screenrc']
#if dotfiles already exist, confirm with user before overwriting.
for dotfilename in dotfiles:
    dotfilepath = curdir+ '/' + dotfilename
    linkpath = homedir + '/' + dotfilename
    if (os.path.exists(linkpath) is True):
        #link exists
        sys.stdout.write("{0} exists, clobber? (y/n):".format(linkpath))
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
for vimdir in (['/.vim/autoload','/.vim/bundle']):
    dirPath = homedir + vimdir
    if not os.path.exists(dirPath):
        print "Creating " + dirPath
        os.makedirs(dirPath)

#pull down latest pathogen.vim
#into ~/.vim/autoload
pathogenUrl =  'https://raw.github.com/tpope/vim-pathogen/master/autoload/pathogen.vim'
r = requests.get(pathogenUrl)
f = open(homedir + '/.vim/autoload/pathogen.vim','w')
f.write(r.text)
f.close()
print "Pulled the latest pathogen.vim to ~/.vim/autoload/pathogen.vim"

#put the packages to use into ~/.vim/bundle
gitClone = 'cd ~/.vim/bundle; git clone '
plugins = [
    'git://github.com/tpope/vim-fugitive.git',
    'git://github.com/tpope/vim-rails.git',
    'git://github.com/tpope/vim-bundler.git',
    'git://github.com/tpope/vim-surround.git',
    'git://github.com/scrooloose/nerdtree.git',
    'git://github.com/kien/ctrlp.vim.git'
]

for plugin in plugins:
    print "Cloning plugin {0}".format(plugin)
    os.system(gitClone + plugin)

print "Done"
