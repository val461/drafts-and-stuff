#!/usr/bin/env python3

# ./mouseLocation.py - display mouse location

import pyautogui

answer = ""
while answer == "":
    location = pyautogui.position()
    print("x={}, y={}".format(location[0], location[1]))
    answer = input()
