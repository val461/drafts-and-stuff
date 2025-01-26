#!/usr/bin/env python3

# ./iterateHotkeys.py - iterate through hotkeys

import pyautogui, sys

default_pause_duration = 0.05

def do_hotkeys(hotkeys, pause_duration = default_pause_duration):
    for h in hotkeys:
        pyautogui.hotkey(*h, interval = pause_duration)


def iterate(quantity = 1, hotkeys_before = [], hotkeys_loop = [], hotkeys_after = [], pause_duration = default_pause_duration):
    pyautogui.PAUSE = pause_duration

    do_hotkeys(hotkeys_before, pause_duration)

    for i in range(quantity):
        do_hotkeys(hotkeys_loop, pause_duration)

    do_hotkeys(hotkeys_after, pause_duration)


def iterate_cmdarg(**kwargs):
    """
    If one command line argument is provided, it will override quantity.
    If at least two command line arguments are provided, they will be used to calculate quantity.
    """
    nb_cmd_args = len(sys.argv) - 1
    if nb_cmd_args > 0:
        if nb_cmd_args >= 2:
            indices = list(map(int, sys.argv[1:3]))           # get the first two command line arguments as integers
            quantity = indices[1] - indices[0] + 1
        elif nb_cmd_args == 1:
            quantity = int(sys.argv[1])
        iterate(quantity, **kwargs)
    else:
        iterate(**kwargs)
