#!/usr/bin/env python3

# ./manualDownload.py quantity
# ./manualDownload.py i_first i_last

# Download the targets of links of an opened browser page.

# quantity (integer): number of items to copy.
# i_first (integer): number of the first item to copy.
# i_last (integer): number of the last item to copy.

from iterateHotkeys import iterate_cmdarg as iterate_hotkeys

print('Adapt the script to the local context before running.'); exit()

iterate_hotkeys(
    hotkeys_before = [['winleft', 'tab']],
    hotkeys_loop = [
        ['alt', 'enter'],
        ['enter'],
        ['tab'],
    ],
    hotkeys_after = [['winleft', 'shift', 'tab']],
    pause_duration = 0.6,
)
