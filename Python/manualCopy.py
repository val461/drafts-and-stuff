#!/usr/bin/env python3

# ./copy.py i_first i_last
# Copy elements one by one from a tab into another tab.
# i_first (integer): number of the first item to copy.
# i_last (integer): number of the last item to copy.

from iterateHotkeys import iterate_cmdarg as iterate

print('Adapt the script to the local context before running.'); exit()

iterate(
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
