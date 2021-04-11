from farmer import Farmer
from miner import Miner
from controller import Controller
from mouseController import MouseController
from block import Block
from material import Material
from tool import Tool
from screenReader import ScreenReader
from board import Board
from ocr import OCR


class Bot:
    def __init__(self):
        self.cooldown = 0.1
        self.delay = 0.101
        self.board = Board()
        self.controller = Controller(self.cooldown, self.delay, self.board)
        self.mouseController = MouseController(self.cooldown, self.delay)
        self.miner = Miner(self.cooldown, self.controller, self.mouseController)
        self.farmer = Farmer(self.cooldown, self.mouseController)
        self.screenReader = ScreenReader()
        self.ocr = OCR()
        self.previousCount = 0

    def strip_mine(self, i):
        self.miner.strip_mine(i, Block.STONE, Tool.PICKAXE, Material.STONE)

    def farm(self):
        self.farmer.farm()

    def action(self, x):
        if x == 1:
            if self.board.x != self.board.sizeX-1:
                self.controller.moveForwardBlocks()
        elif x == 2:
            if self.board.x != 0:
                self.controller.moveBackwardsBlocks()
        elif x == 3:
            if self.board.y != self.board.sizeY-1:
                self.controller.moveRightBlocks()
        elif x == 4:
            if self.board.y != 0:
                self.controller.moveLeftBlocks()
        elif x == 5:
            self.farm()

    def validate_action(self):
        img = self.screenReader.capture_screen(True, False, 80, 80, 4110, 1330)
        number = self.ocr.read_from_image(img)
        if number > self.previousCount + 50 or number < self.previousCount - 50:
            print('change')

        self.previousCount = number

