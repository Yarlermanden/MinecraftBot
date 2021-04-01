#from pynput.keyboard import Key, Controller, Listener
#import keyboard as kkeyboard
#from pynput import mouse as Mouse
import pynput
import time
import pyautogui

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.dirname('Enums/')))

from miner import Miner
from controller import Controller
from mouseController import MouseController
from block import Block
from material import Material
from tool import Tool
from screenReader import ScreenReader

def strip_mine():
    i = 0
    while(True):
        #miner.strip_mine(i, 1, 3, 3)
        img = screenReader.capture_screen(True)
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

cooldown = 0.1
delay = 0.101
mouseController = MouseController(cooldown, delay)
controller = Controller(cooldown, delay)
miner = Miner(cooldown, controller, mouseController)
screenReader = ScreenReader()
time.sleep(5)

strip_mine()
