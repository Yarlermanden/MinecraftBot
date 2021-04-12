import gym
import minerl
import PIL
import cv2
import _thread
import random
#import logging
#logging.basicConfig(level=logging.DEBUG)

linux = False

env = gym.make('MineRLTreechopVectorObf-v0')
#env = gym.make('MineRLNavigateDense-v0')
env.STEP_OPTIONS=300
#env.port=6666
#env.seed(420)
env.reset()
def make_interactive(env, lorteString):
    env.make_interactive(port=6666, realtime=True)
_thread.start_new_thread(make_interactive, (env, 's'))
#env.make_interactive(port=6666, realtime=True)
#env.render()

net_reward = 0

done = False
while not done:
    if linux:
        img = env.render('rgb_array')
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        cv2.imshow('h', img)
        cv2.waitKey(1)
    else:
        print('hi')
        #env.render()
    #action = env.action_space.sample()
    action = env.action_space.noop()
    print(action)

    action['camera'] = [0, 0]
    action['forward'] = 1

    obs,reward,done,info = env.step(action)
    net_reward += reward
    print("Total reward: ", net_reward)

