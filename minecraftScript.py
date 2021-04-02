#from pynput.keyboard import Key, Controller, Listener
#import keyboard as kkeyboard
#from pynput import mouse as Mouse
import pynput
import time
import pyautogui

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.dirname('Enums/')))

from agent import Agent
from screenReader import ScreenReader

def strip_mine():
    i = 0
    while(True):
        agent.strip_mine(i)
        #img = screenReader.capture_screen(True)
        i = 1 + i

def record_screen():
    while(True):
        img = screenReader.capture_screen(True)

def move_mouse_with_keyboard():
    while(True):
        time.sleep(0.01)
        if kkeyboard.is_pressed('k'):
            mouse.move(0, -10)
        elif kkeyboard.is_pressed('j'):
            mouse.move(0, 10)
        elif kkeyboard.is_pressed('h'):
            mouse.move(-10, 0)
        elif kkeyboard.is_pressed('l'):
            mouse.move(10, 0)

agent = Agent()
screenReader = ScreenReader()
time.sleep(5)

strip_mine()
