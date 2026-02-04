# dotfiles
my dotfiles for arch linux, maintained with `git` and `stow`.

## install
install packages from `pkglist.txt`

```
pacman -S --needed $(comm -12 <(pacman -Slq | sort) <(sort pkglist.txt))

```

and additional AUR packages

```
yay -Sua --needed < pkglist.txt
```

create a `dotfiles` directory in your home folder. 
you need to make your `~/.config` subfolders match the subfolders in `~/dotfiles` for `stow` to work.


```
mkdir ~/dotfiles

cd ~/dotfiles && stow .
```

## dependencies
`git`

`stow`
