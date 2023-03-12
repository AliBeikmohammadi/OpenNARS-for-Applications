# ONA vs. $Q$-Learning
Implementation of **ONA vs. $Q$-Learning**, as presented in:
* Comparing NARS and Reinforcement Learning: An Analysis of ONA and $Q$-Learning Algorithms. Submitted to the 16th AGI Conference (AGI-23), Stockholm, Sweden, June 16 - June 19, 2023.


# Usage
* Our implementation is entirely compatible with ONA since it is developed based on. Find the instructions [here](https://github.com/opennars/OpenNARS-for-Applications).

## How to Run Experiments
### CliffWalking-v0
> The script below runs a new test using Q-Learning on the CliffWalking-v0 environment with customized seed and iteration number.
```
python Cliff_Walk_Q.py [seed number] [iteration number]
```
> The script below runs a new test using ONA on the CliffWalking-v0 environment with customized seed and iteration number.
```
python Cliff_Walk_ONA.py [seed number] [iteration number]
```
### Taxi-v3
> The script below runs a new test using Q-Learning on the Taxi-v3 environment with customized seed and iteration number.
```
python Taxi_Q.py [seed number] [iteration number]
```
> The script below runs a new test using ONA on the Taxi-v3 environment with customized seed and iteration number.
```
python Taxi_ONA.py [seed number] [iteration number]
```
### FrozenLake-v1 4x4
> The script below runs a new test using Q-Learning on the FrozenLake-v1 4x4 environment with customized seed and iteration number.
```
python FrozenLake4F_Q.py [seed number] [iteration number]
```
> The script below runs a new test using ONA on the FrozenLake-v1 4x4 environment with customized seed and iteration number.
```
python FrozenLake4F_ONA.py [seed number] [iteration number]
```
### FrozenLake-v1 4x4 Slippery
> The script below runs a new test using Q-Learning on the FrozenLake-v1 4x4 Slippery environment with customized seed and iteration number.
```
python FrozenLake4T_Q.py [seed number] [iteration number]
```
> The script below runs a new test using ONA on the FrozenLake-v1 4x4 Slippery environment with customized seed and iteration number.
```
python FrozenLake4T_ONA.py [seed number] [iteration number]
```
### FrozenLake-v1 8x8
> The script below runs a new test using Q-Learning on the FrozenLake-v1 8x8 environment with customized seed and iteration number.
```
python FrozenLake8F_Q.py [seed number] [iteration number]
```
> The script below runs a new test using ONA on the FrozenLake-v1 8x8 environment with customized seed and iteration number.
```
python FrozenLake8F_ONA.py [seed number] [iteration number]
```
### FrozenLake-v1 8x8 Slippery
> The script below runs a new test using Q-Learning on the FrozenLake-v1 8x8 Slippery environment with customized seed and iteration number.
```
python FrozenLake8T_Q.py [seed number] [iteration number]
```
> The script below runs a new test using ONA on the FrozenLake-v1 8x8 Slippery environment with customized seed and iteration number.
```
python FrozenLake8T_ONA.py [seed number] [iteration number]
```
### FlappyBird-v0
> The script below runs a new test using Q-Learning on the FlappyBird-v0 environment with customized seed and iteration number.
```
python flappy_bird_Q.py [seed number] [iteration number]
```
> The script below runs a new test using ONA on the FlappyBird-v0 environment with customized seed and iteration number.
```
python flappy_bird_ONA.py [seed number] [iteration number]
```
        
        
### OPTIMAL CONTROL PROBLEMS WITH CONSTRAINTS: Optimal Temperature Control with Constraint
> The script below runs a new test on the Optimal Temperature Control with Constraint environment with customized settings.
```
python Optimal_Temperature_Control_with_Constraint.py -h


usage: Optimal_Temperature_Control_with_Constraint.py [-h] [--e E] [--b B] [--E E] [--w W] [--save_dir SAVE_DIR] [--d [D ...]]

optional arguments:
  -h, --help           show this help message and exit
  --e E                Total episodes to train through all environments; default 8000
  --b B                initial_beta; default 1 if 0: only R^T, if (0, 1] adaptive_beta*R^A + (1-adaptive_beta)*R^T where beta = max((E-e)*initial_beta/E),0)
  --E E                Episode in which the beta is zero; default 4000
  --w W                omega, weighting values to the control objective; default 1
  --save_dir SAVE_DIR  Save Directory; default ./Results/Temperature_Control/
  --d [D ...]          debug_level; default False False:nothing print True:print result per each episode
```
### OPTIMAL CONTROL PROBLEMS WITH CONSTRAINTS: A Coupled Four Tank MIMO System
> The script below runs a new test on the Coupled Four Tank MIMO System environment with customized settings.
```
python A_Coupled_Four_Tank_MIMO_System.py -h


usage: A_Coupled_Four_Tank_MIMO_System.py [-h] [--e E] [--b B] [--E E] [--w W] [--save_dir SAVE_DIR] [--d [D ...]]

optional arguments:
  -h, --help           show this help message and exit
  --e E                Total episodes to train through all environments; default 30000
  --b B                initial_beta; default 0.5 if 0: only R^T, if (0, 1] adaptive_beta*R^A + (1-adaptive_beta)*R^T where beta = max((E-e)*initial_beta/E),0)
  --E E                Episode in which the beta is zero; default 3000
  --w W                omega, weighting values to the control objective; default 1
  --save_dir SAVE_DIR  Save Directory; default ./Results/Four_Tank/
  --d [D ...]          debug_level; default False False:nothing print True:print result per each episode
```
# Examples
## Plots
### Random Walk
* Use the scripts below to generate the Random Walk environment figures mentioned in the paper.
```
python plot_results.py --Env RW --O_RT True --O_RA True --input_dir ./Results/RandomWalk/RW_s5_r100_e100.csv --save_dir ./Results/RandomWalk/ 
python plot_results.py --Env RW --O_RT True --O_RA False --input_dir ./Results/RandomWalk/RW_s11_r100_e150.csv --save_dir ./Results/RandomWalk/ 
python plot_results.py --Env RW --O_RT True --O_RA False --input_dir ./Results/RandomWalk/RW_s33_r100_e500.csv --save_dir ./Results/RandomWalk/ 
```
### Optimal Temperature Control with Constraint
* Use the scripts below to generate the Optimal Temperature Control with Constraint environment figures mentioned in the paper.
```
python plot_results.py --Env TC --x_min 0 --x_max 8000 --TA_dir ./Results/Temperature_Control/Temperature_Control_e8000_omega100_beta1.0_E4000.csv --baseline_dir ./Results/Temperature_Control/Temperature_Control_e8000_omega100_beta0.0_E4000.csv --save_dir ./Results/Temperature_Control/
python plot_results.py --Env TC --x_min 0 --x_max 5000  --TA_dir ./Results/Temperature_Control/Temperature_Control_e8000_omega10_beta1.0_E4000.csv --baseline_dir ./Results/Temperature_Control/Temperature_Control_e8000_omega10_beta0.0_E4000.csv --save_dir ./Results/Temperature_Control/
python plot_results.py --Env TC --x_min 0 --x_max 1200 --TA_dir ./Results/Temperature_Control/Temperature_Control_e8000_omega1_beta1.0_E4000.csv --baseline_dir ./Results/Temperature_Control/Temperature_Control_e8000_omega1_beta0.0_E4000.csv --save_dir ./Results/Temperature_Control/
```
### A Coupled Four Tank MIMO System environment
* Use the scripts below to generate the Coupled Four Tank MIMO System environment figures mentioned in the paper.
```
python plot_results.py --Env FT  --x_min 0 --x_max 30000 --TA_dir ./Results/Four_Tank/Four_Tank_e30000_omega1_beta0.5_E3000.csv --baseline_dir ./Results/Four_Tank/Four_Tank_e30000_omega1_beta0.0_E3000.csv --save_dir ./Results/Four_Tank/ 
```
## Experiments
### Random Walk
* The scripts below run the test on the Random Walk environment with the same settings mentioned in the paper
```
python RandomWalk.py --N 7 --E 100 --R 100 --b 0 1 100 --l 0.1 0.5 0.9 --d 0 --save_dir ./Results/RandomWalk/
python RandomWalk.py --N 11 --E 150 --R 100 --b 0 1 100 --l 0.1 0.5 0.9 --d 0 --save_dir ./Results/RandomWalk/
python RandomWalk.py --N 33 --E 500 --R 100 --b 0 1 --l 0.1 0.5 --d 0 --save_dir ./Results/RandomWalk/
```
### Optimal Temperature Control with Constraint
* The scripts below run the test on the Optimal Temperature Control with Constraint environment with the same settings mentioned in the paper.
```
python Optimal_Temperature_Control_with_Constraint.py --e 8000 --b 1 --E 4000 --w 1 --d False --save_dir ./Results/Temperature_Control/
python Optimal_Temperature_Control_with_Constraint.py --e 8000 --b 0 --E 4000 --w 1 --d False --save_dir ./Results/Temperature_Control/
python Optimal_Temperature_Control_with_Constraint.py --e 8000 --b 1 --E 4000 --w 10 --d False --save_dir ./Results/Temperature_Control/
python Optimal_Temperature_Control_with_Constraint.py --e 8000 --b 0 --E 4000 --w 10 --d False --save_dir ./Results/Temperature_Control/
python Optimal_Temperature_Control_with_Constraint.py --e 8000 --b 1 --E 4000 --w 100 --d False --save_dir ./Results/Temperature_Control/
python Optimal_Temperature_Control_with_Constraint.py --e 8000 --b 0 --E 4000 --w 100 --d False --save_dir ./Results/Temperature_Control/
```
### A Coupled Four Tank MIMO System environment
* The scripts below run the test on the Coupled Four Tank MIMO System environment with the same settings mentioned in the paper.
```
python A_Coupled_Four_Tank_MIMO_System.py --e 30000 --b 0.5 --E 3000 --w 1 --d False --save_dir ./Results/Four_Tank/
python A_Coupled_Four_Tank_MIMO_System.py --e 30000 --b 0 --E 3000 --w 1 --d False --save_dir ./Results/Four_Tank/
```

# Citation
* In Proc. of the 22nd International Conference on Autonomous Agents and Multiagent Systems (AAMAS 2023), London, United Kingdom, May 29 – June 2, 2023.
* submitted to the International Joint Conference on Neural Networks 2023 (IJCNN 2023), Queensland, Australia, June 18 - June 23, 2023.


Please cite the accompanied paper, if you find this useful:
```
To be completed
```
