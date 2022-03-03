# As a developer, I want the created Dinosaur objects to be stored in a Herd (the Fleet and Herd must use a List to store the objects).

from Dinosaur import Dinosaur


class Herd:
    def __init__(self):
        self.dinosaurs = []
        self.health = 0
    
    def create_herd(self):
        dino1 = Dinosaur('Blue')
        self.dinosaurs.append(dino1)
        dino2 = Dinosaur('Spike')
        self.dinosaurs.append(dino2)
        dino3 = Dinosaur('Yoshi')
        self.dinosaurs.append(dino3)
        self.health = (dino1 + dino2 + dino3)
