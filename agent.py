from torch import nn
import torch

import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.optimizers import Adam

from rl.agents import DQNAgent
from rl.policy import BoltzmannQPolicy
from rl.memory import SequentialMemory

from environment import Environment

class Agent:
    #def __init__(self):
    #def __init__(self, env, conv_list, dense_list, util_list):
    def __init__(states, actions, bot):
        self.environment = Environment(bot)
        #self.states = self.environment.observation_space
        self.states = self.environment.observation_space.shape[0]
        self.actions = self.environment.action_space.n
        #self.env = env
        #self.conv_list = conv_list
        #self.dense_list = dense_list
        #self.conv2d = torch.nn.Conv2d(
        #self.GAMMA=0.99
        #self.BATCH_SIZE=32
        #self.BUFFER_SIZE=50000
        #self.MIN_REPLAY_SIZE=1000
        #self.EPSILON_START=1.0
        #self.EPSILON_END=0.02
        #self.EPSILON_DECAY=10000
        #self.TARGET_UPDATE_FREQ=1000
        self.model = build_model(states, actions)
        self.dqn = build_agent(self.model, actions)
        self.dqn.compile(Adam(learning_rate=1e-3), metrics=['mae'])
        self.dqn.fit(self.environment, nb_steps=50000, visualize=False, verbose=1) #Use when we want to train
        #self.load() #Use when we want to load instead

    def build_model(self, states, actions):
        model = Sequential()
        model.add(Flatten(input_shape=(1,states)))
        model.add(Dense(24, activation='relu'))
        model.add(Dense(24, activation='relu'))
        model.add(Dense(actions, activation='linear'))
        return model

    def build_agent(self, model, actions):
        policy = BoltzmannQPolicy()
        memory = SequentialMemory(limit=50000, window_length=1)
        dqn = DQNAgent(model=model, memory=memory, policy=policy, nb_actions=actions, nb_steps_warmup=10, target_model_update=1e-2)
        return dqn

    def dqn_compile(self):
        self.dqn.compile(Adam(lr=1e-3), metrics=['mae'])

    def train(self, state, q_values):
        #self.dqn.fit(
        self.model.fit(state, q_values, verbose=0)

    def predict(self, state):
        return self.model.predict(state)

    def save(self):
        self.dqn.save_weights('dqn_weights.h5f', overwrite=True)

    def load(self):
        self.sqn.load_weights('dqn_weights.h5f')
