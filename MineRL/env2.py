import gym
import minerl
import PIL
import cv2
import _thread
import random
import math
#import logging
#logging.basicConfig(level=logging.DEBUG)

linux = False

#env = gym.make('MineRLTreechopVectorObf-v0')
env = gym.make('MineRLNavigateDense-v0')
env.STEP_OPTIONS=300
#env.port=6666
#env.seed(420)
env.make_interactive(port=6666, realtime=True)
obs = env.reset()
#env.render()

net_reward = 0
same = 0
stuck = 0

done = False
while not done:
    if linux:
        img = env.render('rgb_array')
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        cv2.imshow('h', img)
        cv2.waitKey(1)
    else:
        env.render()
        pass
    action = env.action_space.sample()
    #action = env.action_space.noop()

    if same>10:
        action['camera'] = [0, 2]
        print('rotate')
        same -= 2
        stuck += 1
    else:
        #action['camera'] = [0, 0.03*obs['compass']['angle']]
        action['camera'] = [0, 0.03*obs['compassAngle']]
    action['attack'] = 1
    action['back'] = 0
    action['forward'] = 1
    action['jump'] = 1
    #print('action: ' + str(action))

    if stuck > 50 and net_reward > 50:
        action['camera'] = [40, 0]
        action['forward'] = 0
        action['back'] = 0
        action['jump'] = 0
        action['left'] = 0
        action['right'] = 0
    elif stuck > 50:
        action['camera'] = [10, 0]
        stuck = 0

    obs,reward,done,info = env.step(action)
    net_reward += reward
    if reward < 0.01 and reward > -0.01:
        print('same')
        same += 1
    print("Total reward: ", net_reward)

