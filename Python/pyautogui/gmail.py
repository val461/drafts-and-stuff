#!/usr/bin/env python3

# ./gmail.py <quantity>

# Select the first displayed messages on the Gmail page open behind the terminal.

# quantity (integer): number of items to select.

import pyautogui, time
import iterateHotkeys as ht

# print('Adapt the script to the local context before running.'); exit()

pyautogui.hotkey('alt', 'tab', interval = ht.default_pause_duration)
pyautogui.hotkey('home', interval = ht.default_pause_duration)
pyautogui.click(x=176, y=328, clicks = 2)

ht.iterate_cmdarg(
    hotkeys_loop = [
        ['space'],
        ['tab'],
        ['tab'],
    ],
    hotkeys_after = [['alt', 'tab']],
)
