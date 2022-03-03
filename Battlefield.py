
from Dinosaur import Dinosaur
from Fleet import Fleet
from Herd import Herd
from Robot import Robot

class Battlefield:
    def __init__(self):
        self.fleet = Fleet().create_fleet()        #added ()
        self.herd = Herd().create_herd()          #added ()
    
    def run_game(self):
        self.run_game = self.display_welcome()
        self.run_game = self.battle()
        self.run_game = self.dino_turn()
        self.run_game = self.robo_turn()
        self.run_game = self.show_dino_opponent_oppositions()
        self.run_game = self.show_robo_opponent_oppositions()
        self.run_game = self.display_winners()

    def display_welcome(self):
        self.display_welcome = 'Welcome to Robots vs Dinos! Get ready for the ultimate prehistoric - post-apocalyptic show down!'
        print(self.display_welcome)

    def battle(self):
        self.battle = 'Prepare to battle!'
        print(self.battle)
        while (Fleet.health >= 1 and Herd.health >=1):
            for i in range(len(Fleet.robots)):
                Robot.attack
            for i in range(len(Herd.dinosaurs)):
                Dinosaur.attack

    def dino_turn(self, dinosaur):
        self.dino_turn = Dinosaur.attack
        Robot.health -= Dinosaur.attack      #????   #need to subtract the damage dealt by dino from the overall robot health

    def robo_turn(self, robot):
        self.robo_turn = Robot.attack
        Dinosaur.health -= Robot.attack    #???

    def show_dino_opponent_oppositions(self):
        self.show_dino_opponent_oppositions = print(Herd)

    def show_robo_opponent_oppositions(self):
        self.show_robo_opponent_oppositions = print(Fleet)

    def display_winners(self):
        if Fleet.health == 0 and Herd.health > 0:
            print('Sorry, Robots, you are the losing team! DINOS WIN!!')
        elif Herd.health == 0 and Fleet.health > 0:
            print('Sorry, Dinos you are the losing team! ROBOTS WIN!!')
        else:
            pass

