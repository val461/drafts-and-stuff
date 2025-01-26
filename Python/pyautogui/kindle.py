#!/usr/bin/env python3

# ./kindle.py - scrape ebook

# Instructions:
# Put the ebook on the next window, in fullscreen.
# (Identical screenshots signal the ebook may be complete, so avoid having a clock/animation visible in the screenshots.)
# The result will be saved in the current working directory, so you probably should
# run this script with the absolute path, e.g. python3 ~/Documents/Dev/drafts-and-stuff/Python/pyautogui/kindle.py

import pyautogui, time, os
import hashlib

def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def ask_int(msg, default=None):
    try:
        value = int(input(msg))
    except ValueError:
        value = default
    return value

pyautogui.PAUSE = 0.3
PAUSE_TO_LOAD_PAGE = 0.3

print('Adapt the script to the local context before running.'); exit()

if input('Is the current directory the right location to save the files? (Will overwrite without warning.) y/[n] ') != 'y':
    print('Aborting.')
    exit()

# first_file = 0
first_file = ask_int('next image file number (0 if no file yet): ', 0)
assert first_file >= 0

# digits = 2
# digits = ask_int(f'how many digits in filename? (zero-padding) (suggested: {len(n_pages)}) ', len(n_pages))
digits = ask_int(f'digits in filename: (zero-padding) (suggested: 4) ', 4)
# digits = len(n_pages)
assert digits > 0

n_pages = 10**digits
# n_pages = 73
# n_pages = input('total page number in the book (indicated accurately from page 2): ')

# factor = 0.8
# if input(f'Multiply total page number by {factor} ? [y]/n')=='n':
#     factor = 1
factor = 1
n_pages = int(float(n_pages)*factor)

# go to the next window
pyautogui.hotkey('alt', 'tab')

hash = None

for k in range(first_file, n_pages):
    f = f'{str(k).zfill(digits)}.jpg'
    print(f)
    pyautogui.screenshot(f)
    hash2 = md5(f)
    if hash2 == hash:
        pyautogui.hotkey('alt', 'tab')
        if input("Same image. Stop? [y]/n") != 'n':
            print(f"Deleting duplicate image '{f}'.")
            os.remove(f)
            break
        pyautogui.hotkey('alt', 'tab')
    hash = hash2
    pyautogui.hotkey('right')
    time.sleep(PAUSE_TO_LOAD_PAGE)
else:
    pyautogui.hotkey('alt', 'tab')
