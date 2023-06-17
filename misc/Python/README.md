# ONA vs. $Q$-Learning
Implementation of **ONA vs. $Q$-Learning**, as presented in:
* Comparing NARS and Reinforcement Learning: An Analysis of ONA and $Q$-Learning Algorithms. Submitted to the 16th AGI Conference (AGI-23), Stockholm, Sweden, June 16 - June 19, 2023.


# Usage
* Our implementation is entirely compatible with ONA since it is developed based on. Find the instructions [here](https://github.com/opennars/OpenNARS-for-Applications).

## How to Run Experiments
### [CliffWalking-v0](https://gymnasium.farama.org/environments/toy_text/cliff_walking/)
> The script below runs a new test using Q-Learning on the CliffWalking-v0 environment with customized seed and iteration number.
```
python Cliff_Walk_Q.py [seed number] [iteration number]
```
> The script below runs a new test using ONA on the CliffWalking-v0 environment with customized seed and iteration number.
```
python Cliff_Walk_ONA.py [seed number] [iteration number]
```
### [Taxi-v3](https://gymnasium.farama.org/environments/toy_text/taxi/)
> The script below runs a new test using Q-Learning on the Taxi-v3 environment with customized seed and iteration number.
```
python Taxi_Q.py [seed number] [iteration number]
```
> The script below runs a new test using ONA on the Taxi-v3 environment with customized seed and iteration number.
```
python Taxi_ONA.py [seed number] [iteration number]
```
### [FrozenLake-v1 4x4](https://gymnasium.farama.org/environments/toy_text/frozen_lake/)
> The script below runs a new test using Q-Learning on the FrozenLake-v1 4x4 environment with customized seed and iteration number.
```
python FrozenLake4F_Q.py [seed number] [iteration number]
```
> The script below runs a new test using ONA on the FrozenLake-v1 4x4 environment with customized seed and iteration number.
```
python FrozenLake4F_ONA.py [seed number] [iteration number]
```
### [FrozenLake-v1 4x4 Slippery](https://gymnasium.farama.org/environments/toy_text/frozen_lake/)
> The script below runs a new test using Q-Learning on the FrozenLake-v1 4x4 Slippery environment with customized seed and iteration number.
```
python FrozenLake4T_Q.py [seed number] [iteration number]
```
> The script below runs a new test using ONA on the FrozenLake-v1 4x4 Slippery environment with customized seed and iteration number.
```
python FrozenLake4T_ONA.py [seed number] [iteration number]
```
### [FrozenLake-v1 8x8](https://gymnasium.farama.org/environments/toy_text/frozen_lake/)
> The script below runs a new test using Q-Learning on the FrozenLake-v1 8x8 environment with customized seed and iteration number.
```
python FrozenLake8F_Q.py [seed number] [iteration number]
```
> The script below runs a new test using ONA on the FrozenLake-v1 8x8 environment with customized seed and iteration number.
```
python FrozenLake8F_ONA.py [seed number] [iteration number]
```
### [FrozenLake-v1 8x8 Slippery](https://gymnasium.farama.org/environments/toy_text/frozen_lake/)
> The script below runs a new test using Q-Learning on the FrozenLake-v1 8x8 Slippery environment with customized seed and iteration number.
```
python FrozenLake8T_Q.py [seed number] [iteration number]
```
> The script below runs a new test using ONA on the FrozenLake-v1 8x8 Slippery environment with customized seed and iteration number.
```
python FrozenLake8T_ONA.py [seed number] [iteration number]
```
### [FlappyBird-v0](https://github.com/Talendar/flappy-bird-gym)
> The script below runs a new test using Q-Learning on the FlappyBird-v0 environment with customized seed and iteration number.
```
python flappy_bird_Q.py [seed number] [iteration number]
```
> The script below runs a new test using ONA on the FlappyBird-v0 environment with customized seed and iteration number.
```
python flappy_bird_ONA.py [seed number] [iteration number]
```
        
# Reproduce Results
## Produce CSV files
### Run All Tasks
* The script below runs both ONA and Q-Learning on all the environments with the same settings mentioned in the paper (i.e., 10 different seed numbers and 100000 iterations).
```
python RunEnvswithSeeds.py 
```
As a result of executing the above script, 10 CSV files are generated for each environment-algorithm.
### Generate the Final CSV Files
* The script below gets previously generated CSV files. Then it generates a new single CSV file for each algorithm-environment.
```
python GenerateCSV.py 
```
As a result of executing the above script, a single CSV file containing the mean and standard deviation of 10 runs on each algorithm-environment is generated.

## Plots
* Use the scripts below to generate the figures mentioned in the paper.
```
python plotresults_v3.py
```

# Citation
* submitted to the 16th AGI Conference (AGI-23), Stockholm, Sweden, June 16 - June 19, 2023.


Please cite the accompanied paper, if you find this useful:
```
To be completed
```
