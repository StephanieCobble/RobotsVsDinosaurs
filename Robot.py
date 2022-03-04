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
import random       #added randomization

laser_canon = Weapon('Laser Canon', 20)
android_crush = Weapon('Android Crush', 10)
bend = Weapon('Bend', 5)

weapons_list = [laser_canon, android_crush, bend]
rando_weapon = random.choice(weapons_list)

class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 100   #health status to 100 (full)
        self.weapon = rando_weapon
    
    def attack(self, dinosaur):             #rewrote to better streamline attacks. Changes include specifying weapons & listing them
        if dinosaur.health > 0:
            dinosaur.health = dinosaur.health - (self.weapon.attack_power)
            print(f'{self.name} used {self.weapon.name} on {dinosaur.name} for {self.weapon.attack_power} damage!')
        else:
            pass
  
        

   

