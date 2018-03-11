#!/usr/bin/env python3

# ./manualTrain.py
# Display available trains.

import pyautogui, time, sys

if len(sys.argv) <= 1 or sys.argv[1] != '-f':
    print('Adapt the script to the local context before running.'); exit()

def fillTown(town):
    pyautogui.typewrite(town)
    time.sleep(0.7)
    pyautogui.hotkey('down')
    pyautogui.hotkey('down')
    pyautogui.hotkey('tab')
    pyautogui.hotkey('tab')

def main(origin, destination):
    pyautogui.PAUSE = 0.3

    # get the webpage
    pyautogui.hotkey('winleft', '1')
    pyautogui.hotkey('ctrl', 't')
    pyautogui.typewrite('sn')
    pyautogui.hotkey('down')
    pyautogui.hotkey('enter')
    time.sleep(3)

    # use the webpage
    for i in range(3):
        pyautogui.hotkey('down')
    pyautogui.click(x=579, y=580)
    fillTown(origin)
    fillTown(destination)
    input("Type enter to resume. ")
    pyautogui.hotkey('winleft', '1')
    pyautogui.click(x=668, y=785)
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.typewrite('13:00')
    pyautogui.hotkey('enter')
