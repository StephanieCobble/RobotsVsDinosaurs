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

from Robot import Robot


class Dinosaur:
    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = attack_power
        self.health = 100

    def attack(self, robot):
        self.attack = robot
        while self.health > 0:          #added while loop
            self.attack = int(input("Enter 0 to select tail slash or enter 1 to select stomp: "))
            if self.attack == 0:
                self.attack_power = 5
                print(f'{self.name} has attacked for {self.attack_power} damage!')
            elif self.attack == 1:
                self.attack_power = 10
                print(f'{self.name} has attacked  for {self.attack_power} damage!')
            else:
                pass
            

        # Robot.health -= self.attack_power
        # print(f"{Robot.name}'s health is now {Robot.health}")
  
     

