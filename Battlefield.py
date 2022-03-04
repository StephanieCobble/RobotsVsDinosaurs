
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
        self.show_dino_opponent_oppositions
        self.robo_turn()
        self.show_robo_opponent_oppositions

    def dino_turn(self, dinosaur):
        print("Dinos, you're up!")
        random_robot = random.choice(self.fleet.robots)
        dino_attack = random.choice(self.herd.dinosaurs)
        attack_damage = Dinosaur.attack(dino_attack, random_robot)

    def robo_turn(self, robot):
        

    def show_dino_opponent_oppositions(self):
        

    def show_robo_opponent_oppositions(self):
        

    def display_winners(self):
    

