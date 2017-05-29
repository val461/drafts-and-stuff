#!/usr/bin/env python3

# ./copy.py - copy elements one by one from a tab into another tab

import pyautogui, time

print('Adapt the script to the local context before running.'); exit()

i_first = 19
i_last = 20
pyautogui.PAUSE = 0.3

# wait a little for the user to be prepared
time.sleep(2)

for i in range(i_first, i_last + 1):
    pyautogui.hotkey('ctrl', 'c')
    pyautogui.hotkey('ctrl', 'tab')
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.hotkey('ctrl', 'shift', 'tab')
    pyautogui.hotkey('down')
