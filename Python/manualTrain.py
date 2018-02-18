#!/usr/bin/env python3

# ./manualTrainToC.py
# Display available trains.

import pyautogui, time, sys

if len(sys.argv) <= 1 or sys.argv[1] != '-f':
    print('Adapt the script to the local context before running.'); exit()

def fillTown(town):
    pyautogui.typewrite(town)
    time.sleep(0.3)
    pyautogui.hotkey('tab')

def main(origin, destination):
    pyautogui.PAUSE = 0.3

    # get the webpage
    pyautogui.hotkey('winleft', '1')
    pyautogui.hotkey('ctrl', 't')
    pyautogui.typewrite('sn')
    pyautogui.hotkey('down')
    pyautogui.hotkey('enter')
    time.sleep(2)

    # use the webpage
    pyautogui.click(x=376, y=473)
    for i in range(5):
        pyautogui.hotkey('tab')
    fillTown(origin)
    fillTown(destination)
    input("Type enter to resume. ")
    pyautogui.hotkey('winleft', '1')
    pyautogui.click(x=917, y=597)
    pyautogui.typewrite('12')
    pyautogui.hotkey('tab')
    pyautogui.hotkey('tab')
    pyautogui.hotkey('enter')
