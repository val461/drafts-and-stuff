#!/usr/bin/env python3

# ./screenshot.py - make scrot more touchpad-friendly

# Instructions:
# Put whatever you want to capture on the next wm screen.
# The result will be saved in the current working directory, so you probably should
# run this script with the absolute path, e.g. ~/Dev/drafts-and-stuff/Python/pyautogui/screenshot.py
# You will be asked for mouse positions (to delimit the capture zone),
# unless you manually edit ‘zone’ prior to running the script.

import pyautogui, subprocess, time

print('Adapt the script to the local context before running.'); exit()

zone = {}
# ~ zone = {'left': 954, 'top': 280, 'right': 1451, 'bottom': 679}

directions = ["left","bottom","right","top"]

for d in set(directions) - set(zone.keys()):
    try:
        zone[d] = int(input('select {} border (with the mouse or type a number) [enter]'.format(d)))
        mode = "keyboard"
    except ValueError:
        dimension = int(d in ["top","bottom"])
        zone[d] = pyautogui.position()[dimension]
        mode = "mouse"
    print(zone[d], "(selected from {} input)".format(mode))


print(repr(zone))

pyautogui.PAUSE = 0.3

# go to the next wm screen
pyautogui.hotkey('winleft', 'tab')

# run scrot
subprocess.Popen(['scrot', '--select', '--quality', '100'])

# select shooting area
i=0
pyautogui.moveTo(zone[directions[i]], zone[directions[i+1]])
pyautogui.mouseDown()
i=2
pyautogui.moveTo(zone[directions[i]], zone[directions[i+1]], 0.7)

# give the user some time to ponder over the surreal nature of existence
time.sleep(2)

# shoot
pyautogui.mouseUp()

# go to the previous wm screen
pyautogui.hotkey('winleft', 'shift', 'tab')
