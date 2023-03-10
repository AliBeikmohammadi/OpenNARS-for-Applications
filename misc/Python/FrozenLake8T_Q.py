import gym
import sys
import pandas as pd
import numpy as np
import random

seed_num = 1
try:
    seed_num = int(sys.argv[1]) 
except:
    None

max_steps = -1
try:
    max_steps = int(sys.argv[2]) #int(sys.argv[1])
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
np.random.seed(seed_num) 
#Loading and rendering the gym environment
#Setup environment:
# "4x4":[
#     "SFFF",
#     "FHFH",
#     "FFFH",
#     "HFFG"
#     ]

# "8x8": [
#     "SFFFFFFF",
#     "FFFFFFFF",
#     "FFFHFFFF",
#     "FFFFFHFF",
#     "FFFHFFFF",
#     "FHHFFFHF",
#     "FHFFHFHF",
#     "FFFHFFFG",
# ]
# desc=["SFFF", "FHFH", "FFFH", "HFFG"]
#env = gym.make('FrozenLake-v1', desc=None, map_name="4x4", is_slippery=False) #is_slippery=False! deterministic env 
#env = gym.make('FrozenLake-v1', desc=None, map_name="8x8", is_slippery=False) #is_slippery=False! deterministic env
#env = gym.make('FrozenLake-v1', desc=None, map_name="4x4", is_slippery=True) #is_slippery=True! agent will move in intended direction with probability of 1/3 else will move in either perpendicular direction with equal probability of 1/3 in both directions   
env = gym.make('FrozenLake-v1', desc=None, map_name="8x8", is_slippery=True) #is_slippery=True! agent will move in intended direction with probability of 1/3 else will move in either perpendicular direction with equal probability of 1/3 in both directions  
#env.reset() #v1

#Getting the state space
print("Action Space {}".format(env.action_space))
print("State Space {}".format(env.observation_space))
Q = np.zeros((env.observation_space.n, env.action_space.n))

#Training the agent
successes = 0
timestep = 0
random_act = 0
episode_count = 1
reward_episode = 0
successes_episode = 0
iteration = 0
results = []
#Similate for 100000 steps:
obs = env.reset(seed=seed_num) #v1
#obs = env.reset() #v1
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
    #Updating the Q-table using the Bellman equation
    Q[obs, action] = Q[obs, action] + alpha * (reward + discount_factor * np.max(Q[new_obs, :]) - Q[obs, action]) 
    #Increasing our total reward and updating the state
    reward_episode += reward     
    obs = new_obs   
    successes += 1      
    if reward > 0:
        successes_episode += 1
    #Ending the episode
    if done:
        print("iteration= "+ str(iteration), " successes= " + str(successes) + ", successes_episode= "+ str(successes_episode)+ ", reward_episode= " + str(reward_episode) + ", episode_count= " + str(episode_count) + ", random_act= " + str(random_act) + ", timestep= "+str(timestep)+ ", epsilon= "+str(epsilon))
        results.append([iteration, successes, successes_episode, reward_episode, episode_count, random_act, timestep, epsilon])  
        #Cutting down on exploration by reducing the epsilon 
        epsilon = min_epsilon + (max_epsilon - min_epsilon)*np.exp(-decay*episode_count)
        episode_count += 1
        reward_episode = 0
        iteration = 0
        obs = env.reset(seed=seed_num) #v1
        #obs = env.reset() #v1
    #env.render()
    if (timestep+2 >= max_steps and max_steps != -1):
        break
env.close()
data = pd.DataFrame(results)
data.columns = ["iteration", "successes", "successes_episode", "reward_episode" , "episode_count", "random_act", "timestep", "epsilon"]
data.to_csv('FL_8T_v1_Q_'+str(seed_num)+'.csv', index = False)
print("The results saved")