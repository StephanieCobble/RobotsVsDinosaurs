# (/10 points): As a developer, I want a Robot to have a name, health, and a Weapon (this needs to be its own 
#               class and object) with a name (i.e. sword) and attack power. 

# ((/10 points): As a developer, I want the created Robot objects to be stored in a Fleet and the created 
#               Dinosaur objects to be stored in a Herd (the Fleet and Herd must use a List to store the objects).)
# (/10 points): As a developer, I want a Robot to have the ability to attack a Dinosaur and a Dinosaur 
#               to have the ability to attack a Robot on a Battlefield. 
# (/10 points): As a developer, I want a Robot/Dinosaur to lose health points (loss based on attack power) 
#               when another Robot/Dinosaur successfully attacks it. 
# Bonus Points: 
# (/5 points): As a developer, I want a Robot to have the ability to choose from a List of different weapons 
#              that will be then assigned as its own weapon.  
# (/2 points): As a developer, I want a Robot to have a power level and a Dinosaur to have an energy, which 
#              will decrease by 10 every time they attack.

from Weapon import Weapon


class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 100   #health status to 100 (full)
        self.weapon = Weapon()  #added (). Is it just () or do I also put in the name & attack power params? 
    
    def attack(self, dinosaur):
        self.attack = input('Enter 0 to select laser canon or enter 1 to select android crush: ')
        if self.attack == 'laser canon':
            self.attack_power = -5
        elif self.attack == 'android crush':
            self.attack_power == -10
       # self.attack = Weapon().attack_power

