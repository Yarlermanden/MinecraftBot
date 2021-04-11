import gym
import minerl
import PIL
import cv2
#import logging
#logging.basicConfig(level=logging.DEBUG)

linux = True

env = gym.make('MineRLNavigateDense-v0')
env.STEP_OPTIONS=300
#env.seed(420)
#env.make_interactive(port=6666, realtime=True)
env.reset()

net_reward = 0

done = False
while not done:
    if linux:
        img = env.render('rgb_array')
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        cv2.imshow('h', img)
        cv2.waitKey(1)
    else:
        env.render()
    action = env.action_space.sample()
    #print('action: ' + str(action))

    obs,reward,done,info = env.step(action)
    net_reward += reward
    print("Total reward: ", net_reward)

