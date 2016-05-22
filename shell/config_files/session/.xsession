#setxkbmap -layout 'val,fr' -variant 't2,bepo'
#setxkbmap -option ''    # unset previous options if any
#setxkbmap -option 'terminate:ctrl_alt_bksp'
#setxkbmap -option 'option:option_name'

numlockx
xset r rate 250 12      # <delay:ms> <rate:Hz>
sh /home/val/.fehbg
exec i3
