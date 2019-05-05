#!/usr/bin/env python3

# ./clipboard.py

# Like pyperclip, but works on my system.
# Note that content copied with this module seems to get erased from the
# clipboard when exiting the python interpreter.


from tkinter import Tk
import time


_r = Tk()
_r.withdraw()


def empty():
    _r.clipboard_clear()


def copy(string):
    empty()
    _r.clipboard_append(string)
    _r.update()


def paste():
    return _r.clipboard_get()


def quit():
    '''Quit the underlying Tk application.'''
    _r.destroy()
