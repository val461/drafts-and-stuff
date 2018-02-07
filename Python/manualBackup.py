#!/usr/bin/env python3

# ./manualBackup.py

# Zip folders and upload them. (UNTESTED)

import pyautogui

print('Adapt the script to the local context before running.'); exit()

pyautogui.PAUSE = 0.6

def make_zip():
    pyautogui.hotkey('n')
    pyautogui.hotkey('a')
    pyautogui.hotkey('enter')
    pyautogui.hotkey('enter')

def open_import_menu():
    pyautogui.click(x=69, y=247)
    pyautogui.hotkey('down')
    pyautogui.hotkey('down')
    pyautogui.hotkey('enter')
    pyautogui.click(x=328, y=249)

pyautogui.hotkey('winleft', 'left')
pyautogui.hotkey('ctrl', 't')

pyautogui.typewrite('do')
pyautogui.hotkey('enter')
pyautogui.click(x=371, y=458, button='right')
make_zip()

pyautogui.hotkey('winleft', 'left')
pyautogui.hotkey('t')
pyautogui.hotkey('enter')
pyautogui.click(x=371, y=219, button='right')
make_zip()

pyautogui.hotkey('winleft', '1')
pyautogui.hotkey('ctrl', 't')
pyautogui.typewrite('dr')
pyautogui.hotkey('down')
pyautogui.hotkey('enter')

open_import_menu()
pyautogui.click(x=885, y=506)
pyautogui.hotkey('enter')

open_import_menu()
pyautogui.click(x=755, y=453)
pyautogui.hotkey('enter')
pyautogui.click(x=794, y=273)
pyautogui.hotkey('enter')

pyautogui.hotkey('winleft', '3')
pyautogui.hotkey('winleft', 'right')
