# shellcheck shell=bash
# When our attackers have given up,
# show off our beautiful and fancy bash shell prompt
# to them to make them jealous.

USERNAME_HOST="\$(lolcat --freq 0.5 --force <<< 'haxlab@MAKE-HAXWORKS-GREAT-AGAIN')"
PROMPT_ARROW="\033(0mq\033(B➤ "

# ADMIN TODO: fortune-like message Ex. "You got the shell, but so what?" before prompt arrow, different one each time
PS1="\[\033[01m\]$USERNAME_HOST\[\033[00m\] \[\033[07m\]\w\[\033[00m\]\n$PROMPT_ARROW "
