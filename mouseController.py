import time
from pynput import mouse as Mouse

class MouseController:
    def __init__(self, cooldown, delay):
        self.cooldown = cooldown
        self.mouse = Mouse.Controller()
        self.delay = delay

    def holdLeftClick(self, secs = 0.1):
        self.mouse.press(Mouse.Button.left)
        time.sleep(secs+self.delay*3) # as buffer
        self.mouse.release(Mouse.Button.left)
        time.sleep(self.cooldown)

    def vMove(self, value):
        self.mouse.move(0, value)

    def hMove(self, value):
        self.mouse.move(value, 0)

    def turnLeft(self):
        self.mouse.move(-400, 0)

    def turnRight(self):
        self.mouse.move(400, 0)
