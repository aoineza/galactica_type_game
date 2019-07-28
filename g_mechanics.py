
import random

class player():
    def __init__(self):
        self.pos = (300,550)

    def get_pos(self):
        return self.pos
    
    def move_right(self):
        if self.pos[0] > 550:
            return
        self.pos = (self.pos[0] + 5,550)

    def move_left(self):
        if self.pos[0] < 50:
            return
        self.pos = (self.pos[0] - 5,550)

class bullet():
    def __init__(self,start):
        self.pos = start

    def get_pos(self):
        return self.pos

    def move_up(self):
        self.pos = (self.pos[0],self.pos[1] - 5)

class rock():
    def __init__(self):
        self.pos = (random.randint(1,599),1)

    def get_pos(self):
        return self.pos

    def move_down(self):
        self.pos = (self.pos[0] + random.randint(-2,2),self.pos[1]+random.randint(0,5))


        
