from farmer import Farmer
from miner import Miner
from controller import Controller
from mouseController import MouseController
from block import Block
from material import Material
from tool import Tool
from screenReader import ScreenReader


class Agent:
    def __init__(self):
        self.cooldown = 0.1
        self.delay = 0.101
        self.controller = Controller(self.cooldown, self.delay)
        self.mouseController = MouseController(self.cooldown, self.delay)
        self.miner = Miner(self.cooldown, self.controller, self.mouseController)
        self.farmer = Farmer(self.cooldown, self.mouseController)

    def strip_mine(self, i):
        self.miner.strip_mine(i, Block.STONE, Tool.PICKAXE, Material.STONE)

    def farm(self):
        self.farmer.farm()
