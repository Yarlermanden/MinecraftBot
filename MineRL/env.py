import gym
import minerl
import PIL
import cv2
import random
import math
import numpy as np
#import logging
#logging.basicConfig(level=logging.DEBUG)

linux = True

#env = gym.make('MineRLTreechopVectorObf-v0')
env = gym.make('MineRLNavigateDense-v0')
env.STEP_OPTIONS=300
#Q = np.zeros([env.observation_space.n, env.action_space.n])
Q = np.zeros([len(env.observation_space.spaces), len(env.action_space.spaces)])
print(len(env.observation_space.spaces))
#Q = np.zeros([env.observation_space.shape[0], env.action_space.shape[0]])
#Q = np.zeros([len(env.observation_space), len(env.action_space)])
#env.make_interactive(port=6666, realtime=True)

eta = 0.628
gma = .9
epis = 5
rev_list = []

for i in range(epis):
    #obs = env.reset()
    s = env.reset()
    print(s)
    rAll = 0
    done = False
    j = 0
    net_reward = 0

    while not done:
        if linux:
            img = env.render('rgb_array')
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            cv2.imshow('h', img)
            cv2.waitKey(1)
        else:
            env.render()
        action = np.argmax(Q[s,:] + np.random.randn(1, len(env.action_space.spaces))*(1./(i+1)))
        #action = np.argmax(Q[s,:] + np.random.randn(1, env.action_space.n)*(1./(i+1)))
        s1, reward, done, info = env.step(action)
        Q[s,action] = Q[s,action] + eta*(r + gma*np.max(Q[s1,:]) - Q[s,action])
        rAll += reward
        s = s1

        net_reward += reward
        print("Total reward: ", net_reward)

    rev_list.append(rAll)
    env.render()

print("reward sum on all episodes " + str(sum(rev_list)/epis))
print("final values Q-table")
print(Q)
