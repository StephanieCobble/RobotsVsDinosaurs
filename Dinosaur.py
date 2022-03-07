# (/10 points): As a developer, I want a Dinosaur to have a name, health, and attack power.
# (/10 points): As a developer, I want to instantiate three Robot objects and three Dinosaur objects and 
#               assign the appropriate values to all the objects.  
# (/10 points): As a developer, I want the created Robot objects to be stored in a Fleet and the created 
#               Dinosaur objects to be stored in a Herd (the Fleet and Herd must use a List to store the objects).
# (/10 points): As a developer, I want a Robot to have the ability to attack a Dinosaur and a Dinosaur 
#               to have the ability to attack a Robot on a Battlefield. 
# (/10 points): As a developer, I want a Robot/Dinosaur to lose health points (loss based on attack power) 
#               when another Robot/Dinosaur successfully attacks it. 
# Bonus Points:
# # (/5 points): As a developer, I want a Dinosaur to have the ability to choose its attack name from a tuple 
#              of different attack names before attacking a Robot in battle. 
# (/2 points): As a developer, I want a Robot to have a power level and a Dinosaur to have an energy, which 
#              will decrease by 10 every time they attack.

import random

class Dinosaur:
    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = attack_power
        self.health = 100
        self.energy = 100

    def attack(self, robot):
        attack_moves = ['tail slah', 'stomp', 'bite']
        if robot.health > 0:
            robot.health = robot.health - self.attack_power
            self.energy = self.energy - 10
            print(f'{self.name} has used {random.choice(attack_moves)} on {robot.name}, inflicting {self.attack_power} damage!')
        else:
            pass
