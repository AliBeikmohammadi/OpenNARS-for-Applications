import subprocess
Codes=[
'.\Cliff_Walk_ONA.py',
'.\Cliff_Walk_Q.py',
'flappy_bird_ONA.py',
'flappy_bird_Q.py',
'.\FrozenLake4F_ONA.py',
'.\FrozenLake4F_Q.py',
'.\FrozenLake4T_ONA.py',
'.\FrozenLake4T_Q.py',
'.\FrozenLake8F_ONA.py',
'.\FrozenLake8F_Q.py',
'.\FrozenLake8T_ONA.py',
'.\FrozenLake8T_Q.py',
'.\Taxi_ONA.py',
'.\Taxi_Q.py']

for C in Codes:
    for Seed in range(10):
        #subprocess.call(" python "+ C +" "+str(Seed)+ " 100", shell=True)
        subprocess.call(" python "+ C +" "+str(Seed), shell=True)