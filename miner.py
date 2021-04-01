import time
from pynput import mouse as Mouse
from block import Block
from material import Material
from tool import Tool

class Miner:
    def __init__(self, cooldown, controller, mouseController):
        self.blockTool = self.init_block_tool_dictionary()
        self.materialSpeed = self.init_material_speed_increase()
        self.blockHardness = self.init_block_hardness()
        self.controller = controller
        self.mouseController = mouseController
        self.cooldown = cooldown

    def init_block_tool_dictionary(self):
        dic = {}
        dic[Block.STONE] = Tool.PICKAXE
        dic[Block.DIRT] = Tool.SHOVEL
        dic[Block.SAND] = Tool.SHOVEL
        dic[Block.COAL] = Tool.PICKAXE
        dic[Block.DIAMOND] = Tool.PICKAXE
        dic[Block.IRON] = Tool.PICKAXE
        return dic

    def init_material_speed_increase(self):
        dic = {}
        dic[Material.NONE] = 1
        dic[Material.WOOD] = 2
        dic[Material.STONE] = 4
        dic[Material.IRON] = 6
        dic[Material.DIAMOND] = 8
        dic[Material.NETHERITE] = 9
        dic[Material.GOLD] = 12
        return dic

    def init_block_hardness(self):
        dic = {}
        dic[Block.STONE] = 1.5
        dic[Block.DIRT] = 0.5
        dic[Block.SAND] = 0.5
        dic[Block.COAL] = 3
        dic[Block.DIAMOND] = 3
        dic[Block.IRON] = 3
        dic[Block.GOLD] = 3
        return dic

    def mining_speed(self, block, tool, material):
        hardness = self.blockHardness[block]
        if self.blockTool[block] == tool and material != Material.NONE:
            speedIncrease = self.materialSpeed[material]
            return hardness*1.5/speedIncrease
        else:
            return hardness*5

    def mine_block(self, block, tool, material):
        secs = self.mining_speed(block, tool, material)
        self.mouseController.holdLeftClick(secs)

    def strip_mine2x1(self, block, tool, material):
        self.controller.moveForwardBlocks()
        self.mouseController.vMove(200)
        self.mine_block(block, tool, material)
        time.sleep(self.cooldown)

        self.mouseController.vMove(-200)
        self.mine_block(block, tool, material)
        time.sleep(self.cooldown)


    def strip_mine(self, i, block, tool, material):
        self.strip_mine2x1(block, tool, material)
        if i%8 ==7:
            self.place_torch('2','1')

    def place_torch(self, torchKey, toolKey):
        self.mouseController.turnLeft()
        self.controller.changeItem(torchKey)
        self.mouseController.holdRightClick()
        self.mouseController.turnRight()
        self.controller.changeItem(toolKey)
