
call pathogen#infect()

filetype plugin indent on

syntax on

colorscheme koehler

set shiftwidth=4
set tabstop=4
set expandtab
set autoindent
set number

highlight OverLength ctermbg=red ctermfg=white guibg=#592929
match OverLength /\%81v.\+/

set pastetoggle=<F10>


