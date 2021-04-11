from gym import Env
from gym.spaces import Discrete, Box
import numpy as np
import random

class Environment(Env):
    def __init__(self, bot):
        self.action_space = Discrete(5)
        self.bot = bot
        #low = np.zeros((14400,1))
        #high = np.empty((14400,1))
        #high[:] = 255
        #self.observation_space = Box(low=low, high=high)
        self.observation_space = Box(low=0, high=255, shape(14400,1), dtype=np.uint8)
        #self.state = 0 + random.randint(0,5)
        self.state = np.zeros((14400, 1))
        self.length = 600

    def step(self, action):
        #Run everytime we take a step in the environment

        #take action
        self.bot.action()

        #reduce length
        self.length -=1

        #validate bot action
        if self.bot.validate_action():
            reward = 1
        else:
            reward = -1

        #check if done
        if length == 0:
            done = True
        else:
            done = False

        #self.state += random.randint(-1,1)
        info = {}

        return self.state, reward, done, info

    def reset(self):
        #self.state = random.randint(0,5)
        self.state = np.zeros((14400, 1))
        self.length = 600
        return self.state
