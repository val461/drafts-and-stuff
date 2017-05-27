#setxkbmap -layout 'val,fr' -variant 't2,bepo'
#setxkbmap -option ''    # unset previous options if any
#setxkbmap -option 'terminate:ctrl_alt_bksp'
#setxkbmap -option 'option:option_name'

sudo ~/bin/luminosity 98
numlockx
xset r rate 250 12      # <delay:ms> <rate:Hz>
exec i3
