#!/usr/bin/env python3

# ./copy.py quantity
# ./copy.py i_first i_last

# Copy elements one by one from one tab into another tab.

# quantity (integer): number of items to copy.
# i_first (integer): number of the first item to copy.
# i_last (integer): number of the last item to copy.

from iterateHotkeys import iterate_cmdarg as iterate_hotkeys

print('Adapt the script to the local context before running.'); exit()

iterate_hotkeys(
    hotkeys_start = [['winleft', 'left']],
    hotkeys_loop = [
        ['ctrl', 'c'],
        ['ctrl', 'tab'],
        ['ctrl', 'v'],
        ['ctrl', 'shift', 'tab'],
        ['down'],
    ],
    hotkeys_end = [['winleft', 'right']],
    pause_duration = 0.3,
)
