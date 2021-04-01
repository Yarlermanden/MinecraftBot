#from pynput.keyboard import Key, Controller, Listener
from pynput import mouse as Mouse
import pyautogui
import time

class Controller():
    def __init__(self, cooldown, delay):
        self.mouse = Mouse.Controller()
        self.secPrBlockWalk = 1/4.317
        self.delay = delay
        self.cooldown = cooldown

    def moveForwardSec(self, secs):
        self.move('w', secs)

    def moveBackwardsSec(self, secs):
        self.move('s', secs)

    def moveLeftSec(self, secs):
        self.move('a', secs)

    def moveRightSec(self, secs):
        self.move('d', secs)

    def moveForwardBlocks(self, blocks = 1):
        self.move('w', blocks*self.secPrBlockWalk)

    def moveBackwardsBlocks(self, blocks = 1):
        self.move('s', blocks*self.secPrBlockWalk)

    def moveLeftBlocks(self, blocks = 1):
        self.move('a', blocks*self.secPrBlockWalk)

    def moveRightBlocks(self, blocks = 1):
        self.move('d', blocks*self.secPrBlockWalk)

    def move(self, key, secs):
        pyautogui.keyDown(key)
        time.sleep(secs-self.delay)
        pyautogui.keyUp(key)
        time.sleep(self.cooldown)

    def changeItem(self, itemSlot):
        pyautogui.keyDown(itemSlot)
        pyautogui.keyUp(itemSlot)
        time.sleep(self.cooldown)
