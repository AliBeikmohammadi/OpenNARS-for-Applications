import sys
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import csv
#import argparse
#import pathlib
#np.set_printoptions(precision=3, suppress=True)

ONA_csv = {"CW" : "CW_v1_ONA.csv", "FL4F" : "FL_4F_v1_ONA.csv", "FL4T" : "FL_4T_v1_ONA.csv", "FL8F" : "FL_8F_v1_ONA.csv", "FL8T" : "FL_8T_v1_ONA.csv", "Taxi" : "Taxi_v1_ONA.csv", "FB" : "FB_v1_ONA.csv"}
Q_csv = {"CW" : "CW_v1_Q.csv", "FL4F" : "FL_4F_v1_Q.csv", "FL4T" : "FL_4T_v1_Q.csv", "FL8F" : "FL_8F_v1_Q.csv", "FL8T" : "FL_8T_v1_Q.csv", "Taxi" : "Taxi_v1_Q.csv", "FB" : "FB_v1_Q.csv"}
Full_name = {"CW" : "CliffWalking-v0", "FL4F" : "FrozenLake-v1 4x4", "FL4T" : "FrozenLake-v1 4x4 Slippery", "FL8F" : "FrozenLake-v1 8x8", "FL8T" : "FrozenLake-v1 8x8 Slippery", "Taxi" : "Taxi-v3", "FB" : "FlappyBird-v0"}
y_label= {"iteration":"Episode Length", "successes":"Cumulative Episode Length", "successes_episode":"Cumulative Successful Episodes", "reward_episode":"Reward" , "episode_count":"Episodes", "random_act":"Cumulative Random Action", "timestep":"Cumulative Non-Random Action", "epsilon":"Epsilon"}
x_label= {"successes":"Time Step", "episode_count":"Episodes"}

def myplot(env, metric_X, metric_Y, input_file_dir, save_fig_dir):
    if env=="FB" and metric_Y=="successes_episode":
      print("Ploting Cumulative Successful Episodes for Flappy Bird Environment is not available!")
      return
    isExist = os.path.exists(save_fig_dir)
    if not isExist:
        os.makedirs(save_fig_dir)
    ona = pd.read_csv(input_file_dir+ONA_csv[env])
    q = pd.read_csv(input_file_dir+Q_csv[env])
    plt.figure(figsize=[10, 5], dpi=72)
    ax = plt.gca()
    if metric_Y != "epsilon":
      ona.plot(x=metric_X, y=metric_Y,ax=ax,label='ONA', linewidth=3, c='k')
    q.plot(x=metric_X, y=metric_Y,ax=ax, label='$Q$-Learning',linewidth=3, c='red')
    plt.title(Full_name[env])
    plt.ylabel(y_label[metric_Y])
    plt.xlabel(x_label[metric_X])
    #plt.xlim((x_min, x_max)) 
    plt.rcParams.update({'font.size': 15})
    plt.savefig(save_fig_dir+y_label[metric_Y]+'_vs_'+x_label[metric_X]+'_'+Full_name[env]+'.png', dpi=144, format=None, metadata=None, bbox_inches=None, pad_inches=0.1,
            facecolor='auto', edgecolor='auto', backend=None)
    #plt.show()
    print("The figures saved in: "+save_fig_dir)
    return

Metrics_X=["successes", "episode_count"]
Metrics_Y=["iteration","successes", "successes_episode", "reward_episode" , "episode_count",  "random_act", "timestep", "epsilon"] 
Envs=["CW","FL4F","FL4T","FL8F","FL8T", "Taxi", "FB"]
input_file_dir= './'
save_fig_dir= './plots/'


Metrics_X=["successes"]
Metrics_Y=["iteration", "successes_episode", "reward_episode" , "episode_count",  "random_act", "timestep", "epsilon"] 
for env in Envs:
  for metric_X in Metrics_X:
    for metric_Y in Metrics_Y:
      myplot(env, metric_X, metric_Y, input_file_dir, save_fig_dir)
  
Metrics_X=["episode_count"]
Metrics_Y=["iteration", "successes" , "successes_episode", "reward_episode",  "random_act", "timestep", "epsilon"] 
for env in Envs:
  for metric_X in Metrics_X:
    for metric_Y in Metrics_Y:
      myplot(env, metric_X, metric_Y, input_file_dir, save_fig_dir)
#metric_X=Metrics_X[4]
#metric_Y=Metrics_Y[2]
#env= Envs[6]
#myplot(env, metric_X, metric_Y, input_file_dir, save_fig_dir)