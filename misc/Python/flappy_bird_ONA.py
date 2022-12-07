import gym
import NAR
import sys
import time
import flappy_bird_gym
import pandas as pd

max_steps = -1
try:
    max_steps = int(sys.argv[1])
except:
    None

#Configure NARS:
NAR.AddInput("*volume=0")
#NAR.AddInput("*motorbabbling=0.3")
NAR.AddInput("*babblingops=2")
actions = {"^do_nothing" : 0, "^flap" : 1} #gym encoding The action taken by the agent. 0 means "do nothing" and 1 means "flap".
for i, x in enumerate(actions):
    NAR.AddInput("*setopname " + str(i+1) + " " + x) #NAR encoding *setopname 1 ^left *setopname 2 ^down  *setopname 3 ^right *setopname 4 ^up
goal = "G"
    
#Setup environment:
#obs:
#1: horizontal distance to the next pipe;
#2: difference between the player's y position and the next hole's y position
env = flappy_bird_gym.make("FlappyBird-v0")  
#env.reset()  #v3

#Local grid vector to Narsese event:
def observationToEvent(cells):
    # round_obs= [10*cells[0], 100*cells[1]] #v1
    round_obs= [100*cells[0], 1000*cells[1]] #v2
    round_obs = [round(i, 0) for i in round_obs]
    round_obs = [int(item) for item in round_obs]
    stateconcat = lambda state: str(state).replace(",","").replace("[","").replace("]","").replace(" ","_")
    NARSESE_EVENT = stateconcat(round_obs)
    return NARSESE_EVENT + ". :|:"   #just forward and left and right side of agent (( 100r &| 200l ) &| 200f ). :|:



successes = 0
timestep = 0
random_act= 0
episode_count = 1
reward_episode = 0
iteration = 0
results = []
#Similate for 100000 steps:
obs = env.reset() #v3
NAR.AddInput(observationToEvent(obs)) #v3
for i in range(0, 100000):
    default_action = 0 #env.action_space.sample()  # random action  ###!!
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
    if reward > 0: ####????????
        #NAR.AddInput(goal + ". :|:") #v3
        successes += 1
        reward_episode+= 1
    #print("successes=" + str(successes) + ", score_episode=" + str(score_episode) + ", episode_count=" + str(episode_count) + ", random_act=" + str(random_act) + ", time="+str(timestep))
    if done:
        print("iteration= "+ str(iteration), " successes= " + str(successes) + ", reward_episode= " + str(reward_episode) + ", episode_count= " + str(episode_count) + ", random_act= " + str(random_act) + ", timestep= "+str(timestep))
        results.append([iteration, successes, reward_episode, episode_count, random_act, timestep])  
        episode_count+=1
        reward_episode= 0
        iteration = 0
    if done:
        NAR.AddInput("20") #don't temporally relate observations across reset
        #env.seed(1337+i) #v3
        #env.reset() #v3
        env.seed(1) #v3
        obs = env.reset() #v3
        NAR.AddInput(observationToEvent(obs)) #v3
    #env.render()
    #time.sleep(1 / 30)  # FPS
    if (timestep+2 >= max_steps and max_steps != -1):
        break
env.close()
data = pd.DataFrame(results)
data.columns = ["iteration", "successes", "reward_episode" , "episode_count", "random_act", "timestep"]
data.to_csv('FB_v1_ONA.csv', index = False)
print("The results saved")