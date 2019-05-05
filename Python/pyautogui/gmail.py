#!/usr/bin/env python3

# ./gmail.py quantity
# ./gmail.py i_first i_last

# Select all displayed messages on the Gmail page open behind the terminal.

# quantity (integer): number of items to select.
# i_first (integer): number of the first message to select.
# i_last (integer): number of the last message to select.

import pyautogui
import iterateHotkeys as ht

# print('Adapt the script to the local context before running.'); exit()

pyautogui.hotkey('alt', 'tab', interval = ht.default_pause_duration)
pyautogui.hotkey('home', interval = ht.default_pause_duration)
pyautogui.click(x=177, y=332, clicks = 2)

ht.iterate_cmdarg(
    hotkeys_loop = [
        ['space'],
        ['tab'],
        ['tab'],
    ],
    hotkeys_after = [['alt', 'tab']],
)
