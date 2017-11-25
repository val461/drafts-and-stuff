#!/usr/bin/env python3

# ./manualDownload.py i_first i_last
# Download links from an opened browser page.
# i_first (integer): number of the first item to copy.
# i_last (integer): number of the last item to copy.

from iterateHotkeys import iterate_cmdarg as iterate

print('Adapt the script to the local context before running.'); exit()

iterate(
    hotkeys_before = [['winleft', 'tab']],
    hotkeys_loop = [
        ['alt', 'enter'],
        ['enter'],
        ['tab'],
    ],
    hotkeys_after = [['winleft', 'shift', 'tab']],
    pause_duration = 0.6,
)
