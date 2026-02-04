# dotfiles
my dotfiles for arch linux, maintained with `git` and `stow`.

## install
create a `dotfiles` directory in your home folder. 
you need to make your `~/.config` subfolders match the subfolders in `~/dotfiles` for `stow` to work.


```
mkdir ~/dotfiles

cd ~/dotfiles && stow .
```


## dependencies
`git`

`stow`
