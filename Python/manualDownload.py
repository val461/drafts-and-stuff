#!/usr/bin/env python3

# ./copy.py - download links from an opened browser page

import pyautogui, time

#~ print('Adapt the script to the local context before running.'); exit()

i_first = 1
i_last = 1
pyautogui.PAUSE = 0.6

pyautogui.hotkey('winleft', 'tab')

for i in range(i_first, i_last + 1):
    pyautogui.hotkey('alt', 'enter')
    pyautogui.press('enter')
    pyautogui.hotkey('tab')
