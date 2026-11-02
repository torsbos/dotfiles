let mapleader=' '

imap <C-BS> <C-W>
nnoremap <cr> <Esc>:w<cr>
nnoremap K i<cr><Esc>

command! W execute 'w !sudo tee % > /dev/null' <bar> edit!
command WC execute '!cat % | wc -w'

map <leader>cd :Ex<cr>
map <leader>n :set relativenumber!<cr>
map <leader>q :q<cr>
map <leader>g :!groff -ms % -k -Tpdf > %.pdf<cr>
