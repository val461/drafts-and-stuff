#!/usr/bin/env python3

# ./screenshot.py - make scrot more touchpad-friendly

# Instructions:
# Put whatever you want to capture on the next wm screen.
# The result will be saved in the current working directory, so you probably should
# run this script with the absolute path, e.g. ~/Dev/drafts-and-stuff/Python/screenshot.py
# You will be asked for the mouse positions (to delimit the capture zone),
# unless you manually edit ‘zone’ prior to running the script.

import pyautogui, subprocess, time

print('Adapt the script to the local context before running.'); exit()

zone = {}
# ~ zone = {'left': 954, 'top': 280, 'right': 1451, 'bottom': 679}

directions = ["left","right","top","bottom"]

if set(zone.keys()) != set(directions):
    zone = {}

    for d in directions[:2]:
        try:
            zone[d] = int(input('{} border (with mouse or keyboard); press enter to validate: '.format(d)))
        except ValueError:
            zone[d] = pyautogui.position()[0]
        print(zone[d])


    for d in directions[2:]:
        try:
            zone[d] = int(input('{} border (with mouse or keyboard); press enter to validate: '.format(d)))
        except ValueError:
            zone[d] = pyautogui.position()[1]
        print(zone[d])

print(repr(zone))

pyautogui.PAUSE = 0.3

# go to the next wm screen
pyautogui.hotkey('winleft', 'tab')

# run scrot
subprocess.Popen(['scrot', '--select', '--quality', '100'])

# select shooting area
i=0
pyautogui.moveTo(zone[directions[i]], zone[directions[i+2]])
pyautogui.mouseDown()
i=1
pyautogui.moveTo(zone[directions[i]], zone[directions[i+2]], 0.7)

# give the user some time to ponder over the surreal nature of existence
time.sleep(1)

# shoot
pyautogui.mouseUp()

# go to the previous wm screen
pyautogui.hotkey('winleft', 'shift', 'tab')
