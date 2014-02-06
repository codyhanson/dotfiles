
#init nvm
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

#for git shell prompt
# Configure colors, if available.
if [ -x /usr/bin/tput ] && tput setaf 1 >&/dev/null; then
    c_reset='\[\e[0m\]'
    c_user='\[\e[1;33m\]'
    c_path='\[\e[0;33m\]'
    c_git_cleancleann='\[\e[0;36m\]'
    c_git_dirty='\[\e[0;35m\]'
    else
    c_reset=
    c_user=
    c_git_cleancleann_path=
    c_git_clean=
    c_git_dirty=
fi
# Function to assemble the Git parsingart of our prompt.
git_prompt ()
{
    if ! git rev-parse --git-dir > /dev/null 2>&1; then
        return 0
    fi
        git_branch=$(git branch 2>/dev/null | sed -n '/^\*/s/^\* //p')
    if git diff --quiet 2>/dev/null >&2; then
        git_color="$c_git_clean"
    else
        git_color="$c_git_dirty"
    fi
    echo "[$git_color$git_branch${c_reset}]"
}
# Thy holy prompt.
PROMPT_COMMAND='PS1="${c_user}\u${c_reset}@${c_user}\h${c_reset}:${c_path}\w${c_reset}$(git_prompt)\$ "'
#end git prompt code


