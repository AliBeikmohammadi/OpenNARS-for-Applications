import gym
import sys
import pandas as pd
import numpy as np
import random
import flappy_bird_gym
import time

max_steps = -1
try:
    max_steps = int(sys.argv[1])
except:
    None

#Setting the hyperparameters          
alpha = 0.7 #learning rate                 
discount_factor = 0.618               
epsilon = 1                  
max_epsilon = 1
min_epsilon = 0.01         
decay = 0.01         

#Fixing seed for reproducibility
np.random.seed(1) 
#Loading and rendering the gym environment
#Setup environment:
#obs:
#1: horizontal distance to the next pipe;
#2: difference between the player's y position and the next hole's y position
env = flappy_bird_gym.make("FlappyBird-v0")
#env.reset() #v1

#Getting the state space
print("Action Space {}".format(env.action_space))
print("State Space {}".format(env.observation_space))
Q = np.zeros((1000, env.action_space.n))

#Local grid vector to Narsese event:
def observationToEvent(cells):
    # round_obs= [10*cells[0], 100*cells[1]] #v1
    round_obs= [100*cells[0], 1000*cells[1]] #v2
    round_obs = [round(i, 0) for i in round_obs]
    #round_obs = [int(item) for item in round_obs]
    #stateconcat = lambda state: str(state).replace(",","").replace("[","").replace("]","").replace(" ","")
    #NARSESE_EVENT = stateconcat(round_obs)
    NARSESE_EVENT = abs(round_obs[0])+abs(round_obs[1])
    NARSESE_EVENT = int(NARSESE_EVENT)
    #print('NARSESE_EVENT',NARSESE_EVENT)
    return NARSESE_EVENT


#Training the agent
successes = 0
timestep = 0
random_act = 0
episode_count = 1
reward_episode = 0
iteration = 0
results = []
#Similate for 100000 steps:
env.seed(1) #v1
obs = env.reset() #v1
obs = observationToEvent(obs)
for i in range(0, 100000):   
    #Choosing an action given the states based on a random number
    exp_exp_tradeoff = random.uniform(0, 1) 
    #If the random number is larger than epsilon: employing exploitation and selecting best action 
    if exp_exp_tradeoff > epsilon:
        action = np.argmax(Q[obs,:])      
        timestep += 1
    #Otherwise, employing exploration: choosing a random action 
    else:
        action = env.action_space.sample()
        random_act += 1
    iteration += 1    
    #Taking the action and getting the reward and outcome state
    new_obs, reward, done, info = env.step(action)
    new_obs = observationToEvent(new_obs)
    #Updating the Q-table using the Bellman equation
    Q[obs, action] = Q[obs, action] + alpha * (reward + discount_factor * np.max(Q[new_obs, :]) - Q[obs, action]) 
    #Increasing our total reward and updating the state
    reward_episode += reward     
    obs = new_obs  
    if reward > 0: ####????????
        successes += 1
        reward_episode+= 1       
    #Ending the episode
    if done:
        print("iteration= "+ str(iteration), " successes= " + str(successes) + ", reward_episode= " + str(reward_episode) + ", episode_count= " + str(episode_count) + ", random_act= " + str(random_act) + ", timestep= "+str(timestep)+ ", epsilon= "+str(epsilon))
        results.append([iteration, successes, reward_episode, episode_count, random_act, timestep, epsilon])  
        #Cutting down on exploration by reducing the epsilon 
        epsilon = min_epsilon + (max_epsilon - min_epsilon)*np.exp(-decay*episode_count)
        episode_count += 1
        reward_episode = 0
        iteration = 0
        env.seed(1) #v3
        obs = env.reset() #v1
        obs = observationToEvent(obs)
    #env.render()
    #time.sleep(1 / 30)  # FPS
    if (timestep+2 >= max_steps and max_steps != -1):
        break
env.close()
data = pd.DataFrame(results)
data.columns = ["iteration", "successes", "reward_episode" , "episode_count", "random_act", "timestep", "epsilon"]
data.to_csv('FB_v1_Q.csv', index = False)
print("The results saved")