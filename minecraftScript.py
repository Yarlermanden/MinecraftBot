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

def strip_mine():
    miner.strip_mine(1, 3, 3)

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
time.sleep(5)

strip_mine()
