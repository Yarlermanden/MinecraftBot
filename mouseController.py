import time
from pynput import mouse as Mouse

class MouseController:
    def __init__(self, cooldown, delay):
        self.cooldown = cooldown
        self.mouse = Mouse.Controller()
        self.delay = delay

    def holdLeftClick(self, secs = 0.1):
        self.holdMouseButton(secs+self.delay*3, Mouse.Button.left)

    def holdRightClick(self, secs = 0.1):
        self.holdMouseButton(secs, Mouse.Button.right)

    def holdMouseButton(self, secs, button):
        self.mouse.press(button)
        time.sleep(secs)
        self.mouse.release(button)
        time.sleep(self.cooldown)

    def vMove(self, value):
        self.mouse.move(0, value)

    def hMove(self, value):
        self.mouse.move(value, 0)

    def turnLeft(self):
        self.mouse.move(-400, 0)

    def turnRight(self):
        self.mouse.move(400, 0)
