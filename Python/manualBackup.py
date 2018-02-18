#!/usr/bin/env python3

# ./manualBackup.py

# Zip folders and upload them.

import pyautogui, time, sys

if len(sys.argv) <= 1 or sys.argv[1] != '-f':
    print('Adapt the script to the local context before running.'); exit()

pyautogui.PAUSE = 1.5

def make_zip():
    pyautogui.hotkey('n')
    pyautogui.hotkey('a')
    pyautogui.hotkey('enter')
    pyautogui.hotkey('enter')

def open_import_menu():
    pyautogui.click(x=69, y=247)
    time.sleep(0.5)
    pyautogui.hotkey('down')
    pyautogui.hotkey('down')
    pyautogui.hotkey('enter')
    pyautogui.click(x=328, y=249)

# go to file manager
pyautogui.hotkey('winleft', 'left')
pyautogui.hotkey('ctrl', 't')

pyautogui.typewrite('do')
pyautogui.hotkey('enter')
pyautogui.click(x=85, y=446, button='right')
make_zip()

pyautogui.hotkey('winleft', 'left')
pyautogui.hotkey('t')
pyautogui.hotkey('enter')
pyautogui.click(x=371, y=219, button='right')
make_zip()

# go to web browser
pyautogui.hotkey('winleft', '1')
pyautogui.hotkey('ctrl', 't')
pyautogui.typewrite('dr')
pyautogui.hotkey('down')
pyautogui.hotkey('enter')
time.sleep(1)

open_import_menu()
pyautogui.click(x=761, y=495)
pyautogui.hotkey('enter')

open_import_menu()
pyautogui.click(x=755, y=453)
pyautogui.hotkey('enter')
pyautogui.click(x=794, y=273)
pyautogui.hotkey('enter')

# go back
pyautogui.hotkey('winleft', '3')
