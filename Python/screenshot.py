#!/usr/bin/env python3

# ./screenshot.py - make scrot more touchpad-friendly

# Instructions:
# Put whatever you want to capture on the next wm screen.
# The result will be saved in the current working directory, so you probably should run
# this script with the absolute path, e.g. ~/Dev/drafts-and-stuff/Python/screenshot.py
# You will be asked for the mouse starting and ending positions.

import pyautogui, subprocess, time

print('Adapt the script to the local context before running.'); exit()

pos = []
#~ pos = [(575, 53), (1109, 836)]

if len(pos) != 2:
    pos = [None, None]
    for i in range(2):
        input('Put the mouse at location {} and type enter to validate: '.format(i+1))
        pos[i] = pyautogui.position()

print(repr(pos))

pyautogui.PAUSE = 0.3

# go to the next wm screen
pyautogui.hotkey('winleft', 'tab')

# run scrot
subprocess.Popen(['scrot', '--select', '--quality', '100'])

# select shooting area
pyautogui.moveTo(*pos[0])
pyautogui.mouseDown()
pyautogui.moveTo(*pos[1], 1)

# give the user some time to ponder over the surreal nature of existence
time.sleep(3)

# shoot
pyautogui.mouseUp()

# go to the previous wm screen
pyautogui.hotkey('winleft', 'shift', 'tab')
