#!/usr/bin/env python3

# ./upload.py

# Upload archives to Google Drive.

import pyautogui, time, sys

if len(sys.argv) <= 1 or sys.argv[1] != '-f':
    print('Adapt the script to the local context before running.'); exit()

pyautogui.PAUSE = 1.5

# go to web browser
pyautogui.hotkey('winleft', '1')
pyautogui.hotkey('ctrl', 't')
pyautogui.typewrite('drive/u/1')
time.sleep(1)
pyautogui.hotkey('down')
pyautogui.hotkey('enter')
time.sleep(5)

# open import menu
pyautogui.click(x=69, y=247)
pyautogui.hotkey('down')
pyautogui.hotkey('down')
pyautogui.hotkey('enter')

pyautogui.hotkey('winleft', '3')
input("Press [enter] if the two archives are done with code zero: ")
pyautogui.hotkey('winleft', '1')

pyautogui.click(x=328, y=249)
pyautogui.click(x=761, y=443)
pyautogui.hotkey('enter')
time.sleep(1)

# open import menu
pyautogui.click(x=69, y=247)
pyautogui.hotkey('down')
pyautogui.hotkey('down')
pyautogui.hotkey('enter')

pyautogui.click(x=755, y=388)
pyautogui.hotkey('enter')
pyautogui.click(x=794, y=273)
pyautogui.hotkey('enter')

# go back
pyautogui.hotkey('winleft', '3')
