"""THIS PROGRAM ONLY USE IS TO GENERATE THE TITLE OF A RANDOM MISSION/QUEST
   FOR POKEMON MYSTERY DUNGEON STYLE GAMES, IT WILL NOT GENERATE ENEMIE
   POKEMON FOR YOU, IT WILL NOT GENERATE DETAILS OF THE MISSION, IT WILL
   NOT GENERATE RANDOM ENCOUNTERS"""

"""Import random functions to the program"""

import random

"""Prints on screen a list of the available commands
   for the user"""

def listcommands():
    print("Hello and welcome to the random mission generator.")
    print("Below you can see a list with the available commands,")
    print("just type the number of the desired command and press Enter to run it")
    print("1 - Generate a complete mission (mission title, client, rank, reward and final enemy)")
    print("2 - Generate a mission name")
    print("3 - Generate a dungeon")
    print("4 - Generate a client")
    print("5 - Generate a random enemy")
    print("6 - Generate a difficult rank")
    print("7 - Generate a reward")
    print("0 - Close the Program")

"""Collect the possible mission names from the mission.txt file"""

def mission():
   mission = list()
   read = 'm'
   f = open(mission.txt,mode = 'r')
   while read != '':
      read = f.readline()
      read = read.rstrip('\n')
      read = read.rstrip('\t')
      if read != '':
         mission.append(read)
   f.close()
   return mission

"""Collect the possible dungeon names from the dungeon.txt file"""

def dungeon():
   dungeon = list()
   read = 'd'
   f = open(dungeon.txt,mode = 'r')
   while read != '':
      read = f.readline()
      read = read.rstrip('\n')
      read = read.rstrip('\t')
      if read != '':
         dungeon.append(read)
   f.close()
   return dungeon

"""Collect the possible clients names from the clients.txt file"""

def client():
   client = list()
   read = 'c'
   f = open(client.txt,mode = 'r')
   while read != '':
      read = f.readline()
      read = read.rstrip('\n')
      read = read.rstrip('\t')
      if read != '':
         client.append(read)
   f.close()
   return client

"""Collect the possible enemies names from the enemies.txt file"""
def enemies():
   enemies = list()
   read = 'e'
   f = open(enemies.txt,mode = 'r')
   while read != '':
      read = f.readline()
      read = read.rstrip('\n')
      read = read.rstrip('\t')
      if read != '':
         enemies.append(read)
   f.close()
   return enemies

"""Collect the possible difficulty ranks from the reward.txt file"""

def rank(f,n):
   rank = list()
   read = 'r'
   read = f.readline()
   read = read.rstrip('\n')
   read = read.rstrip('\t')
   rank.append(read)
   n = n - 1
   while n != 0
      while read != 'end':
         read = f.readline()
         read = read.rstrip('\n')
         read = read.rstrip('\t')
      read = f.readline()
      read = read.rstrip('\n')
      read = read.rstrip('\t')
      rank.append(read)
      n = n - 1
   return rank  
   
"""Collect the possible difficulty rewards from the reward.txt file"""   

def reward(f,n):
   reward = list()
   auxlist - list()
   read = 'r'
   "the first two lines are irrevelant, they contain the number of difficulties and the first difficult name"
   read = f.readline()
   read = f.readline()
   read = f.readline()
   read = read.rstrip('\n')
   read = read.rstrip('\t')
   while n != 0:
      while read != 'end':
         auxlist.append(read)
         read = f.readline()
         read = read.rstrip('\n')
         read = read.rstrip('\t')
      reward.append(auxlist)
      auxlist = list()
      n = n - 1
   return reward

"""Choose random mission title only"""

def randomtitlegenerator(mission):
   x = len(mission) - 1
   y = random.randint(0,x)
   print('Mission' + mission[y])
   
"""Choose a random dungeon for the mission"""

def randomdungeongenerator(dungeon):
   x = len(dungeon) - 1
   y = random.randint(0,x)
   print('Dungeon: ' + dungeon[y])

"""Choose a random mission client"""

def randomclientgenerator(client):
   x = len(client) - 1
   y = random.randint(0,x)
   print('Client' + client[y])
   
"""Choose a random enemy for the mission"""

def randomenemygenerator(enemies):
   x = len(enemies) - 1
   y = random.randint(0,x)
   print('Enemy: ' + enemies[y])

"""Choose a random difficult rank for the mission"""

def randomrankgenerator(rank):
   x = len(rank) - 1
   y = random.randint(0,x)
   print('Rank: ' + rank[y])
   return y

"""Choose a random reward for the mission"""

def randomrewardgenerator(reward,n):
   x = len(reward[n]) - 1
   y = random.randint(0,x)
   print('Reward: ' + reward[n][y])

"""START OF THE MAIN PROGRAM"""
"""Flow control variables"""
end = 0
command = '8'
"""Stores in lists the data provided by the user"""
mission = mission()
dungeon = dungeon()
client = client()
enemies = enemies()
"Instead of opening the reward.txt twice, opens a single time and already save"
"information that will be used for both, ranks and rewards"
f = open(reward.txt,mode = 'r')
n = f.readline()
n = n.rstrip('\n')
n = n.rstrip('\n')
n = int(n)
rank = rank(f,n)
f.seek(0)
reward = reward(f,n)
f.close()
"""Extra variables"""
n = 0
x = 1
"""Print the user commands on screen"""
listcommands()

while end != 1:
   command = input()
   if command == '0':
      end = 1
   elif command == '1':
      randomtitlegenerator(mission)
      randomdungeongenerator(dungeon)
      randomclientgenerator(client)
      randomenemygenerator(enemies)
      n = randomrankgenerator(rank)
      randomrewardgenerator(reward,n)
      print('\n\n')
   elif command == '2':
      randomtitlegenerator(mission)
      print('\n\n')
   elif command == '3':
      randomdungeongenerator(dungeon)
      print('\n\n')
   elif command == '4':
      randomclientgenerator(client)
      print('\n\n')
   elif command == '5':
      randomenemygenerator(enemies)
      print('\n\n')
   elif command == '6':
      n = randomrankgenerator(rank)
      print('\n\n')
   elif command == '7':
      "Index starts at 0, thus x-1 will provide the correct placement of the item on the list"
      for item in rank:
         print(x + ' - ' + rank[x-1])
         x = x + 1
      n = input("Type the number of the difficult of the mission: ")
      n = n - 1
      randomrewardgenerator(reward,n)
   else:
      print("Unidentified command, please try again")
