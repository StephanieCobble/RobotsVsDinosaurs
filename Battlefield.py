
from Dinosaur import Dinosaur
from Fleet import Fleet
from Herd import Herd
from Robot import Robot
import random

class Battlefield:
    def __init__(self):
        self.fleet = Fleet()       #added ()
        self.herd = Herd()         #added ()
        self.game = self.run_game()

    def run_game(self):
       Battlefield.display_welcome(self)
       Battlefield.battle(self)
       Battlefield.display_winners(self)

    def display_welcome(self):
        print('Welcome to Robots vs Dinos! Get ready for the ultimate prehistoric - post-apocalyptic show down!')
        

    def battle(self):
        self.dino_turn()
        self.show_dino_opponent_oppositions()
        self.robo_turn()
        self.show_robo_opponent_oppositions()

    def dino_turn(self):
        print("Dinos, you're up!")
        random_robot = random.choice(self.fleet.robots)
        dino_attack = random.choice(self.herd.dinosaurs)
        attack_damage = Dinosaur.attack(dino_attack, random_robot)
        
    def show_dino_opponent_oppositions(self):
        print(f'{self.herd.dinosaurs[0].name} has {self.herd.dinosaurs[0].health} health left! Energy level is now at {self.herd.dinosaurs[0].energy}')
        print(f'{self.herd.dinosaurs[1].name} has {self.herd.dinosaurs[1].health} health left! Energy level is now at {self.herd.dinosaurs[1].energy}')
        print(f'{self.herd.dinosaurs[2].name} has {self.herd.dinosaurs[2].health} health left! Energy level is now at {self.herd.dinosaurs[2].energy}')

    def robo_turn(self):   
        print("Robots, you're up next!")
        random_dino = random.choice(self.herd.dinosaurs)
        robo_attack = random.choice(self.fleet.robots)
        attack_damage = Robot.attack(robo_attack, random_dino)
        # power_level = Robot.power - 10

    def show_robo_opponent_oppositions(self):
        print(f'{self.fleet.robots[0].name} has {self.fleet.robots[0].health} health left! Power level is now at {self.fleet.robots[0].power}')
        print(f'{self.fleet.robots[1].name} has {self.fleet.robots[1].health} health left! Power level is now at {self.fleet.robots[1].power}')
        print(f'{self.fleet.robots[2].name} has {self.fleet.robots[2].health} health left! Power level is now at {self.fleet.robots[2].power}')

    def display_winners(self):
        game_complete = False
        while game_complete == False:
            if ((self.herd.dinosaurs[0].health or self.herd.dinosaurs[0].energy) <= 0) and ((self.herd.dinosaurs[1].health or self.herd.dinosaurs[1].energy) <= 0) \
                and ((self.herd.dinosaurs[2].health or self.herd.dinosaurs[2].energy) <= 0):
                game_complete = True
                print('The dinos have been defeated! Robots are the winners!')
                break
            elif ((self.fleet.robots[0].health or self.fleet.robots[0].power) <= 0) and ((self.fleet.robots[1].health or self.fleet.robots[0].power) <= 0) \
                and ((self.fleet.robots[2].health or self.fleet.robots[0].power) <= 0):
                game_complete = True
                print('The robots have been defeated! Robots are the winners!')
                break
            else:
                Battlefield.battle(self)


#if self.herd.dinosaurs[0, 1, 2].health <= 0: