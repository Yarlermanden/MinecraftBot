import time
from pynput import mouse as Mouse
from enum import IntEnum


class Miner:
    def __init__(self):
        self.blockTool = self.init_block_tool_dictionary()
        self.materialSpeed = self.init_material_speed_increase()
        self.blockHardness = self.init_block_hardness()

    def mine_block(self, mouse, block, tool, material):
        mouse.press(Mouse.Button.left)
        time.sleep(self.mining_speed(block, tool, material) + 0.05)
        mouse.release(Mouse.Button.left)
        time.sleep(0.05)

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



class Block(IntEnum):
    STONE = 1
    DIRT = 2
    SAND = 3
    COAL = 4
    DIAMOND = 5
    IRON = 6
    GOLD = 7

class Tool(IntEnum):
    HOE = 1
    SHOVEL = 2
    PICKAXE = 3
    AXE = 4
    SWORD = 5

class Material(IntEnum):
    NONE = 1
    WOOD = 2
    STONE = 3
    IRON = 4
    DIAMOND = 5
    GOLD = 6
    NETHERITE = 7
