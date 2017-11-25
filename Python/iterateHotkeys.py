#!/usr/bin/env python3

# ./iterateHotkeys.py - iterate through hotkeys

import pyautogui, sys

def do_hotkeys(hotkeys):
    for h in hotkeys:
        pyautogui.hotkey(*h)

def iterate(quantity, hotkeys_before, hotkeys_loop, hotkeys_after, pause_duration):
    pyautogui.PAUSE = pause_duration

    do_hotkeys(hotkeys_start)

    for i in range(quantity):
        do_hotkeys(hotkeys_loop)

    do_hotkeys(hotkeys_end)

def iterate_cmdarg(hotkeys_before, hotkeys_loop, hotkeys_after, pause_duration = 0.6):
    if len(sys.argv) >= 2:
        indices = map(int, sys.argv[1:3])           # get the first two command line arguments as integers
        quantity = indices[1] - (indices[0] - 1)
    else:
        quantity = int(sys.argv[0])
    iterate(quantity, hotkeys_before, hotkeys_loop, hotkeys_after, pause_duration)
