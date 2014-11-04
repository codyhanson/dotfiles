
#init nvm
export NVM_DIR=~/.nvm
source $(brew --prefix nvm)/nvm.sh

#init rbenv
eval "$(rbenv init -)"

#colorful prompt
export PS1="\[\033[36m\]\u\[\033[m\]@\[\033[32m\]\h:\[\033[33;1m\]\w\[\033[m\]\$ "

#add local bin to PATH
export PATH=~/bin:$PATH

#put /usr/local/bin before /usr/bin
export PATH=/usr/local/bin:$PATH

#term colors
export CLICOLOR=1
export LSCOLORS=GxFxCxDxBxegedabagaced

#better ls coloring
alias ls='ls -GFh'

source ~/.bash_prompt
