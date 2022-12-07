import gym
import NAR
import sys
import pandas as pd

max_steps = -1
try:
    max_steps = int(sys.argv[1])
except:
    None

#Configure NARS:
NAR.AddInput("*volume=0")
#NAR.AddInput("*motorbabling=0.3")
NAR.AddInput("*babblingops=4")
actions = {"^up" : 0, "^right" : 1, "^down" : 2, "^left" : 3} #gym encoding
for i, x in enumerate(actions):
    NAR.AddInput("*setopname " + str(i+1) + " " + x) #NAR encoding *setopname 1 ^left *setopname 2 ^down  *setopname 3 ^right *setopname 4 ^up
goal = "G"

#Each time step incurs -1 reward, and stepping into the cliff incurs -100 reward. done=True if reach the goal    
#Setup environment:
env =gym.make('CliffWalking-v0') 
#env.reset() #v1

#Local grid vector to Narsese event:
def observationToEvent(cells):
    return str(cells) + ". :|:"   

successes = 0
timestep = 0
random_act= 0
episode_count=1
reward_episode=0
successes_episode=0
iteration = 0
results = []
#Similate for 100000 steps:
obs = env.reset(seed=1) #v1
NAR.AddInput(observationToEvent(obs)) #v1
for i in range(0, 100000):
    default_action = env.action_space.sample()  # random action  ###!!
    action = default_action
    chosenAction = False
    executions = NAR.AddInput(goal + "! :|:", Print=True)["executions"]
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
    if reward == -1:
        successes += 1
    if done: #reward > 0:
        NAR.AddInput(goal + ". :|:")
        successes_episode += 1
    #print("successes=" + str(successes) + ", episode_count=" + str(episode_count) + ", random_act=" + str(random_act) + ", time="+str(timestep))
    if done or reward==-100: #reset the game
        print("iteration= "+ str(iteration), " successes= " + str(successes) + ", successes_episode= "+ str(successes_episode)+ ", reward_episode= " + str(reward_episode) + ", episode_count= " + str(episode_count) + ", random_act= " + str(random_act) + ", timestep= "+str(timestep))
        results.append([iteration, successes, successes_episode, reward_episode, episode_count, random_act, timestep])  
        episode_count += 1
        reward_episode = 0
        iteration = 0
        NAR.AddInput("20") #don't temporally relate observations across reset
        #env.seed(1337+i) #v1
        #env.reset() #v1
        obs = env.reset(seed=1) #v1
        NAR.AddInput(observationToEvent(obs)) #v1
    #env.render()
    if (timestep+2 >= max_steps and max_steps != -1):
        break
env.close()
data = pd.DataFrame(results)
data.columns = ["iteration", "successes", "successes_episode", "reward_episode" , "episode_count", "random_act", "timestep"]
data.to_csv('CW_v1_ONA.csv', index = False)
print("The results saved")