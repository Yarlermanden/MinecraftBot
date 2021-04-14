import gym
import minerl
import PIL
import cv2
import _thread
import random
import math
import numpy as np
import csv
import os

#import logging
#logging.basicConfig(level=logging.DEBUG)


def training():
    linux = False

    actionToInt = {'attack':0, 'back':1, 'forward':2, 'jump':3, 'left':4, 'right':5, 'sneak':6, 'sprint':7}
    intToAction = {0:'attack', 1:'back', 2:'forward', 3:'jump', 4:'left', 5:'right', 6:'sneak', 7:'sprint'}

    filename = 'QTable'
    folder = './outputs/navigationQlearning'
    n = 0
    while os.path.exists(folder + "%s" % n):
        n += 1
    try:
        os.mkdir(folder + str(n))
    except OSError:
        print ("Failed creating directory: " + path + str(n))



    env = gym.make('MineRLNavigateDense-v0')
    env.STEP_OPTIONS=300
    #env.make_interactive(port=6666, realtime=True)


    observation_space_size = len(env.observation_space.spaces)
    action_space_size = len(env.action_space.spaces)
    QTable = np.zeros((361, 8))

    num_episodes = 1000
    max_steps_pr_episode = 1000

    learning_rate = 0.01
    discount_rate = 0.2

    exploration_rate = 1 #epsilon
    max_exploration_rate = 1
    min_exploration_rate = 0.01
    exploration_decay_rate = 0.01

    rewards_all_episodes= []

    #Q learning
    for episode in range(num_episodes):
        print('new episode!!!')
        print('episode number: ' + str(episode))
        state = env.reset()

        stateInt = int(state['compassAngle']) + 180

        done = False
        rewards_current_episode = 0

        for step in range(max_steps_pr_episode):
            #Exploration-exploitation trade-off
            #This changes more and more towards exploitation the more we train where as we mostly explore in the beginning
            exploration_rate_threshold = random.uniform(0,1)
            if exploration_rate_threshold > exploration_rate:
                #exploitation
                #action = np.argmax(QTable[stateInt,:])
                maxActionIndex = np.argmax(QTable[stateInt,:])
                print('maxIndex from QTable: ' + str(maxActionIndex))
            else:
                #explore
                action = env.action_space.sample()
                attack = float(action['attack'])
                back = float(action['back'])
                forward = float(action['forward'])
                jump = float(action['jump'])
                left = float(action['left'])
                right = float(action['right'])
                sneak = float(action['sneak'])
                sprint = float(action['sprint'])

                maxValue = attack
                maxActionIndex = 0
                if back > maxValue:
                    maxValue = back
                    maxActionIndex = 1
                if forward > maxValue:
                    maxValue = forward
                    maxActionIndex = 2
                if jump > maxValue:
                    maxValue = jump
                    maxActionIndex = 3
                if left > maxValue:
                    maxValue = left
                    maxActionIndex = 4
                if right > maxValue:
                    maxValue = right
                    maxActionIndex = 5
                if sneak > maxValue:
                    maxValue = sneak
                    maxActionIndex = 6
                if sprint > maxValue:
                    maxValue = sprint
                    maxActionIndex = 7

            action['camera'] = (0,1)
            action['attack'] = 0
            action['back'] = 0
            action['forward'] = 0
            action['jump'] = 0
            action['left'] = 0
            action['right'] = 0
            action['sneak'] = 0
            action['sprint'] = 0
            action[intToAction[maxActionIndex]] = 1

            new_state, reward, done, info = env.step(action)


            newStateInt = int(new_state['compassAngle'])+180
            actionInt = maxActionIndex


            #Update QTable for Q(s,a)
            QTable[stateInt, actionInt] = QTable[stateInt, actionInt] * (1 - learning_rate) + learning_rate * (reward + discount_rate * np.max(QTable[newStateInt, :]))
            #QTable[stateList, actionList] = QTable[stateList, actionList] * (1 - learning_rate) + learning_rate * (reward + discount_rate * np.max(QTable[new_stateList, :]))
            #QTable[stateList, actionList] = QTable[stateList, actionList] * 2

            state = new_state
            stateInt = newStateInt
            rewards_current_episode += reward

            if done == True:
                break;

        print(rewards_current_episode)

        if episode % 10 == 0 and episode != 0:
            nn = episode/10
            with open(folder + str(n) + '/' + filename + str(nn) + '.csv', "w+") as my_csv:
                csvWriter = csv.writer(my_csv, delimiter=',')
                csvWriter.writerows(QTable)

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
    with open("latestQTable.csv", "w+") as my_csv:
        csvWriter = csv.writer(my_csv, delimiter=',')
        csvWriter.writerows(QTable)

def test():
    env = gym.make('MineRLNavigateDense-v0')
    env.STEP_OPTIONS=300
    env.make_interactive(port=6666, realtime=True)
    #QTable = pd.read_csv(r'./outputs/navigationQlearning5/QTable50.0.csv')
    with open('./outputs/navigationQlearning5/QTable50.0.csv', newline='') as csvfile:
        QTable = list(csv.reader(csvfile))
        QTable = np.array(QTable)
        print(QTable)
    #Load QTable

    actionToInt = {'attack':0, 'back':1, 'forward':2, 'jump':3, 'left':4, 'right':5, 'sneak':6, 'sprint':7}
    intToAction = {0:'attack', 1:'back', 2:'forward', 3:'jump', 4:'left', 5:'right', 6:'sneak', 7:'sprint'}

    done = False
    totalReward = 0

    state = env.reset()
    stateInt = int(state['compassAngle']) + 180

    while not done:
        maxActionIndex = np.argmax(QTable[stateInt,:])
        action = env.action_space.noop()
        action[intToAction[maxActionIndex]] = 1
        action['camera'] = (0,1)
        new_state, reward, done, info = env.step(action)

        newStateInt = int(new_state['compassAngle'])+180
        stateInt = newStateInt

        totalReward += reward

if __name__ == '__main__':
    #train()
    test()
