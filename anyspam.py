import time, os, pynput

from time import sleep
from pynput.keyboard import Key, Controller
from pyautogui import keyUp, keyDown, press, write
from time import sleep
from os import system

keyboard = Controller()

link = input("What link u finna spam cuz? ")

sleep(5)

while True:
    write(link)
    sleep(0.09)
    keyboard.press(Key.enter)
    sleep(0.08)
    keyboard.release(Key.enter)
    sleep(0.09)