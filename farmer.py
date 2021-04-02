import time

class Farmer:
    def __init__(self, cooldown, mouseController):
        self.seed = '9'
        self.food = '8'
        self.mouseController = mouseController
        self.cooldown = cooldown

    def farm(self):
        self.mouseController.holdLeftClick()
        self.mouseController.holdRightClick()
        time.sleep(self.cooldown)


