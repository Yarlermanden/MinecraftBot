import gym
import minerl
import logging

#logging.basicConfig(level=logging.DEBUG)

env = gym.make('MineRLNavigateDense-v0')
#env.make_interactive(port=6666, realtime=True)

obs = env.reset()
net_reward = 0
#env.render()

done = False
while not done:
    action = env.action_space.sample()
    #print('action: ' + str(action))

    obs,reward,done,info = env.step(action)
    net_reward += reward
    print("Total reward: ", net_reward)
