#!/usr/bin/env python3

# launch luminosity and alsamixer

import pyautogui
import time

pyautogui.PAUSE = 0.2

pyautogui.hotkey('winleft', '2')

# launch bin/luminosity

pyautogui.hotkey('winleft', 'd')
time.sleep(5)
pyautogui.typewrite('lu')
pyautogui.press('enter')
pyautogui.press('enter')
pyautogui.press('enter')
pyautogui.press('enter')

# launch alsamixer

pyautogui.hotkey('winleft', 'd')
pyautogui.typewrite('al')
pyautogui.press('enter')

# set up layout

pyautogui.hotkey('winleft', 'e')
pyautogui.hotkey('winleft', 'e')
pyautogui.hotkey('winleft', 'up')
pyautogui.hotkey('winleft', 'r')
pyautogui.hotkey('up')
pyautogui.hotkey('up')
pyautogui.hotkey('up')
pyautogui.press('enter')
