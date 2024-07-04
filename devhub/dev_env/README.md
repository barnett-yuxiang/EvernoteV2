
## git 101

gitconfig
```
[user]
	name = <NAME>
	email = <MAIL>
[core]
	editor = vim
[filter "lfs"]
	clean = git-lfs clean -- %f
	smudge = git-lfs smudge -- %f
	process = git-lfs filter-process
	required = true
[alias]
	i = init
	co = checkout
```

tools
- Fork
- tig


## Mac

`brew install git curl wget`

font

`git clone --depth 1 https://github.com/ryanoasis/nerd-fonts.git`

plugins

```
git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions

git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting

git clone https://github.com/zsh-users/zsh-completions ${ZSH_CUSTOM:-${ZSH:-~/.oh-my-zsh}/custom}/plugins/zsh-completions

git clone https://github.com/zsh-users/zsh-history-substring-search ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-history-substring-search
```

zsh theme

`git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k`

other useful terminal tools: `brew install gh eza bat procs ripgrep`


- gh


- eza
- bat
- procs
- ripgrep, https://github.com/BurntSushi/ripgrep

## Linux


## Windows

