# As a developer, I want the created Robot objects to be stored in a Fleet (the Fleet and Herd must use a List to store the objects)

from Robot import Robot

class Fleet:
    def __init__(self):
        self.robots = []
        self.health = 100
        self.power = 100
        self.create_fleet()
        

    def create_fleet(self):
        robot1 = Robot('Bender')
        self.robots.append(robot1)
        robot2 = Robot('Scarecrow')
        self.robots.append(robot2)
        robot3 = Robot('Data')
        self.robots.append(robot3)
        self.health = (robot1 and robot2 and robot3)
        