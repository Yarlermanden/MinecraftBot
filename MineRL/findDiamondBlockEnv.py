import gym
import minerl
import PIL
import cv2
import _thread
import random
import math
import numpy as np
#import logging
#logging.basicConfig(level=logging.DEBUG)

linux = False

env = gym.make('MineRLNavigateDense-v0')
env.STEP_OPTIONS=300

#env.make_interactive(port=6666, realtime=True)


observation_space_size = len(env.observation_space.spaces)
action_space_size = len(env.action_space.spaces)
#QTable = np.zeros((observation_space_size, action_space_size))
QTable = np.zeros((3, action_space_size))

num_episodes = 100
max_steps_pr_episode = 100

learning_rate = 0.1
discount_rate = 0.99

exploration_rate = 1 #epsilon
max_exploration_rate = 1
min_exploration_rate = 0.01
exploration_decay_rate = 0.001

rewards_all_episodes= []

#Q learning
for episode in range(num_episodes):
    state = env.reset()

    stateList = []
    stateList.append(state['compassAngle'])
    stateList.append(0)
    stateList.append(0)

    done = False
    rewards_current_episode = 0

    for set in range(max_steps_pr_episode):
        #Exploration-exploitation trade-off
        #This changes more and more towards exploitation the more we train where as we mostly explore in the beginning
        exploraion_rate_threshold = random.uniform(0,1)
        if exploraion_rate_threshold > exploration_rate:
            #exploitation
            action = np.argmax(QTable[stateList,:])
        else:
            #explore
            action = env.action_space.sample()

        new_state, reward, done, info = env.step(action)

        #We need some way of translating the different values to straight Dict
        new_stateList = []
        new_stateList.append(float(new_state['compassAngle']))
        new_stateList.append(0)
        new_stateList.append(0)

        actionList = []
        actionList.append(int(action['attack']))
        actionList.append(int(action['back']))
        cam = action['camera']
        actionList.append(cam[0])
        actionList.append(cam[1])
        actionList.append(int(action['forward']))
        actionList.append(int(action['jump']))
        actionList.append(int(action['left']))
        #actionList.append(action['place'])
        actionList.append(int(action['right']))
        actionList.append(int(action['sneak']))
        actionList.append(int(action['sprint']))


        #Update QTable for Q(s,a)
        #QTable[state, action] = QTable[state, action] * (1 - learning_rate) + learning_rate * (reward + discount_rate * np.max(Qtable[new_state, action]))
        #QTable[stateList, actionList] = QTable[stateList, actionList] * (1 - learning_rate) + learning_rate * (reward + discount_rate * np.max(QTable[new_stateList, :]))
        #QTable[stateList, actionList] = QTable[stateList, actionList] * 2
        for i in range(len(stateList)):
            for j in range(len(actionList)):
                QTable[i, j] = QTable[i, j] * (1 - learning_rate) + learning_rate * (reward + discount_rate * np.max(QTable[i,:]))

        state = new_state
        stateList = new_stateList
        rewards_current_episode += reward

        if done == True:
            break;

    #Exploration rate decay
    #increase chance of exploitation
    exploration_rate = min_exploration_rate + (max_exploration_rate - min_exploration_rate) * np.exp(-exploration_decay_rate*episode)

    rewards_all_episodes.append(rewards_current_episode)

#Calculate and print the average reward per thousand episodes
rewards_per_thousand_episodes = np.split(np.array(rewards_all_episodes), num_episodes/10)
count = 10
for r in rewards_per_thousand_episodes:
    print(count, ": ", str(sum(r/10)))
    count += 10


print("QTABLE")
print(QTable)
