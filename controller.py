#from pynput.keyboard import Key, Controller, Listener
from pynput import mouse as Mouse
import pyautogui
import time

class Controller():
    def __init__(self, cooldown, delay, board):
        self.mouse = Mouse.Controller()
        self.secPrBlockWalk = 1/4.317
        self.delay = delay
        self.cooldown = cooldown
        self.board = board

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
        self.board.move_x(blocks)

    def moveBackwardsBlocks(self, blocks = 1):
        self.move('s', blocks*self.secPrBlockWalk)
        self.board.move_x(-blocks)

    def moveLeftBlocks(self, blocks = 1):
        self.move('a', blocks*self.secPrBlockWalk)
        self.board.move_y(-blocks)

    def moveRightBlocks(self, blocks = 1):
        self.move('d', blocks*self.secPrBlockWalk)
        self.board.move_y(blocks)

    def move(self, key, secs):
        pyautogui.keyDown(key)
        time.sleep(secs-self.delay)
        pyautogui.keyUp(key)
        time.sleep(self.cooldown)

    def changeItem(self, itemSlot):
        pyautogui.keyDown(itemSlot)
        pyautogui.keyUp(itemSlot)
        time.sleep(self.cooldown)
