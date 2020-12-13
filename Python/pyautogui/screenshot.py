#!/usr/bin/env python3

# ./screenshot.py - automate area screenshots

'''
TODO :
Fix loop.
Move parameters (filename, extension, folder) to data file along with region coordinates.
Make window switching togglable.
Update instructions.
'''

# Instructions:
# Put whatever you want to capture on the next wm screen.
# The result will be saved in the current working directory, so you probably should
# run this script with the absolute path, e.g. ~/Dev/drafts-and-stuff/Python/pyautogui/screenshot.py
# You will be asked for mouse positions (to delimit the capture region),
# unless you manually edit ‘region’ prior to running the script.

import pyautogui, subprocess, time

print('Adapt the script to the local context before running.'); exit()

filename='%Y-%m-%d@%H:%M:%S'
extension='png'
folder='~/Pictures/screenshots'

pyautogui.PAUSE = 0.3

directions = ["left","bottom","right","top"]
region = {}
# region = {'left': 954, 'top': 280, 'right': 1451, 'bottom': 679}
fullscreen = True
answer = None

while answer != 'q':
    answer = input('> ')
    if answer = ""
        # take screenshot

        # go to the next window
        pyautogui.hotkey('alt', 'tab')

        # run scrot
        if fullscreen:
            subprocess.Popen(['scrot', f'{folder}/{filename}.{extension}'])
        else:
            x = region["left"]
            y = region["top"]
            w = region["right"] - region["left"]
            h = region["bottom"] - region["top"]
            subprocess.Popen(['scrot', f'-a{x},{y},{w},{h}', f'{folder}/{filename}.{extension}'])

        # return to the previous window
        pyautogui.hotkey('alt', 'tab')
    elif answer = "f"
        fullscreen = True
    elif answer = "r"
        # FIXME
        # switch to region mode unless region coordinates are missing
        fullscreen = False
    elif answer = "m"
        # FIXME
        # set region coordinates
        for d in set(directions) - set(region.keys()):
            try:
                region[d] = int(input('select {} border (with the mouse or type a number) [enter]'.format(d)))
                source = "keyboard"
            except ValueError:
                dimension = int(d in ["top","bottom"])
                region[d] = pyautogui.position()[dimension]
                source = "mouse"
            print(region[d], "(selected from {} input)".format(source))
        print(repr(region))
    elif answer = "l"
        # FIXME
        # choose region coordinates to load from a data file
        pass
    elif answer = "s"
        # FIXME
        # save region coordinates in a data file, if with a possibly empty title
        # data file format: python dictionaries
        pass
    elif answer = "q"
        print('Quitting.')



