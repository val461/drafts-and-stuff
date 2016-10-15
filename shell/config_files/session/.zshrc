echo "Hello, ${USER}! Welcome to zsh!"

export INTERACTIVE=1

# Lines configured by zsh-newuser-install
HISTFILE=~/.histfile
HISTSIZE=1000
SAVEHIST=1000
unsetopt beep
bindkey -e
# End of lines configured by zsh-newuser-install

# The following lines were added by compinstall
zstyle :compinstall filename '/home/val/.zshrc'

autoload -Uz compinit
compinit
# End of lines added by compinstall

setopt INTERACTIVE_COMMENTS
setopt GLOB_DOTS
export EDITOR='geany'
export PATH='/usr/local/sbin:/usr/local/bin:/usr/bin:/usr/lib/jvm/default/bin:/usr/bin/site_perl:/usr/bin/vendor_perl:/usr/bin/core_perl:/home/val/.gem/ruby/2.3.0/bin:.'
export PROMPT='%n %2c %# '

#aliases

alias al="alsamixer"
alias cdb="cd '/home/val/mnt/Data/Documents/Dev/languages/scripting/shell'"
alias cdh="cd '/home/val/mnt/Data/Documents/Dev/languages/programming/functional/Haskell'"
alias cdj="cd '/home/val/mnt/Data/Documents/Dev/languages/programming/imperative/Java/workspaces/shell'"
alias cdr="cd '/home/val/Documents/Dev/languages/scripting/Ruby/workspace'"
alias chr='~/bin/chrono'
alias k="kill -s KILL"
alias ka="killall -s KILL"
alias ls='ls -Fa --color=auto'
alias ll='ls -Flah --color=auto'
alias l='ls'
alias lu='sudo /home/val/bin/luminosity'
alias pm='xterm -e sh ~/bin/update & disown ; exit'
alias reloadkb="bin/keyboard set"
alias sd='~/bin/setDNS'
alias sdo='~/bin/setDNS odns'
alias sdr='~/bin/setDNS resgp'
alias sdd='~/bin/setDNS default'
alias vi='vim'
