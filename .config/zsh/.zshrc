# Lines configured by zsh-newuser-install
HISTFILE=~/.cache/zsh/histfile
HISTSIZE=10000
SAVEHIST=10000
LESSHISTFILE=/dev/null
bindkey -v
# End of lines configured by zsh-newuser-install
# The following lines were added by compinstall
zstyle :compinstall filename '$HOME/.config/zsh/.zshrc'

autoload -Uz compinit
compinit
# End of lines added by compinstall

source ~/.config/zsh/aliases

source ~/.config/zsh/zsh-autosuggestions/zsh-autosuggestions.zsh
source ~/.config/zsh/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh

export PS1="%{$(tput setaf 226)%}%n%{$(tput setaf 220)%}@%{$(tput setaf 214)%}%m %{$(tput setaf 33)%}%8~ %{$(tput sgr0)%}$ "
