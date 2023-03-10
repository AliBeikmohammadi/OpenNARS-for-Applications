import gym
import NAR
import sys
import pandas as pd

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

#Configure NARS:
NAR.AddInput("*volume=0")
#NAR.AddInput("*motorbabling=0.3")
NAR.AddInput("*babblingops=4")
actions = {"^left" : 0, "^down" : 1, "^right" : 2, "^up" : 3} #gym encoding
for i, x in enumerate(actions):
    NAR.AddInput("*setopname " + str(i+1) + " " + x) #NAR encoding *setopname 1 ^left *setopname 2 ^down  *setopname 3 ^right *setopname 4 ^up
goal = "G"
    
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
env = gym.make('FrozenLake-v1', desc=None, map_name="4x4", is_slippery=False) #is_slippery=False! deterministic env 
#env = gym.make('FrozenLake-v1', desc=None, map_name="8x8", is_slippery=False) #is_slippery=False! deterministic env
#env = gym.make('FrozenLake-v1', desc=None, map_name="4x4", is_slippery=True) #is_slippery=True! agent will move in intended direction with probability of 1/3 else will move in either perpendicular direction with equal probability of 1/3 in both directions   
#env = gym.make('FrozenLake-v1', desc=None, map_name="8x8", is_slippery=True) #is_slippery=True! agent will move in intended direction with probability of 1/3 else will move in either perpendicular direction with equal probability of 1/3 in both directions  
#env.reset() #v1

#Local grid vector to Narsese event:
def observationToEvent(cells):
    return str(cells) + ". :|:"   

successes = 0
timestep = 0
random_act = 0
episode_count = 1
reward_episode = 0
successes_episode = 0
iteration = 0
results = []
#Similate for 100000 steps:
obs = env.reset(seed=seed_num) #v3) #v1
NAR.AddInput(observationToEvent(obs)) #v1
for i in range(0, 100000):
    default_action = env.action_space.sample()  # random action  ###!!
    action = default_action
    chosenAction = False
    executions = NAR.AddInput(goal + "! :|:", Print=True)["executions"]
    #for i in range(0,5):
    #    executions += NAR.AddInput(goal + "! :|:", Print=True)["executions"]
    executions += NAR.AddInput("5", Print=False)["executions"]
    if executions:
        chosenAction = True
        action = actions[executions[0]["operator"]] if executions[0]["operator"] in actions else default_action
        timestep += 1 #
    if not chosenAction:
        action = default_action
        print('random action:', list(actions.keys())[action])
        random_act += 1 
    iteration += 1
    obs, reward, done, info = env.step(action)
    #print('obs:', obs)
    #print('observationToEvent(obs):', observationToEvent(obs))
    NAR.AddInput(observationToEvent(obs))
    env.step_count = 0 #avoids episode max_time reset cheat
    reward_episode += reward
    successes += 1
    if reward > 0:
        NAR.AddInput(goal + ". :|:")
        successes_episode += 1
    if done:
        print("iteration= "+ str(iteration), " successes= " + str(successes) + ", successes_episode= "+ str(successes_episode)+ ", reward_episode= " + str(reward_episode) + ", episode_count= " + str(episode_count) + ", random_act= " + str(random_act) + ", timestep= "+str(timestep))
        results.append([iteration, successes, successes_episode, reward_episode, episode_count, random_act, timestep])  
        episode_count+=1
        reward_episode = 0
        iteration = 0
        
    if done:
        NAR.AddInput("20") #don't temporally relate observations across reset
        #env.seed(1337+i) #v1
        #env.reset() #v1
        obs = env.reset(seed=seed_num) #v1
        NAR.AddInput(observationToEvent(obs)) #v1
    #env.render()
    if (timestep+2 >= max_steps and max_steps != -1):
        break
env.close()
data = pd.DataFrame(results)
data.columns = ["iteration", "successes", "successes_episode", "reward_episode" , "episode_count", "random_act", "timestep"]
data.to_csv('FL_4F_v1_ONA_'+str(seed_num)+'.csv', index = False)
print("The results saved")
