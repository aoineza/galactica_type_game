
import pygame
import g_mechanics
import math
import copy

class GameView():
    def __init__(self):
        self.player = g_mechanics.player()
        self.running = True
        self.rocks = []
        self.bullets = []
    
    def run(self):
        pygame.init()
        clock = pygame.time.Clock()
        surface = pygame.display.set_mode((600,600))
        i = 0
        clock = pygame.time.Clock()
        while self.running:
            clock.tick(25)
            self.handle_events(i)
            self.draw()
            i += 1
        pygame.quit()

    def draw(self):
        surface = pygame.display.get_surface()
        surface.fill(pygame.Color(250,250,250))
        for rock in self.rocks:
            pygame.draw.circle(surface,(0,0,0),rock.get_pos(),10,0)
        for bullet in self.bullets:
            pygame.draw.circle(surface,(250,0,0),bullet.get_pos(),5,0)
        pygame.draw.circle(surface,(0,250,0),self.player.get_pos(),8,0)
        pygame.display.flip()

    def handle_events(self,i):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_LEFT]:
            self.player.move_left()
        if keys_pressed[pygame.K_RIGHT]:
            self.player.move_right()
        if i % 2 == 0:
            self.drop_rock()
        if i % 8 == 0:
            self.shoot()
        self.move_bullets()
        self.move_rocks()
        self.remove_rocks()
        self.remove_player()
        self.remove_bullets()

    def move_bullets(self):
        for bullet in self.bullets:
            bullet.move_up()

    def remove_bullets(self):
        bullets_copy = copy.copy(self.bullets)
        for bullet in bullets_copy:
            x1,y1 = bullet.get_pos()
            if y1 <= 0:
                self.bullets.remove(bullet)

    def move_rocks(self):
        for rock in self.rocks:
            rock.move_down()

    def remove_player(self):
        x1,y1 = self.player.get_pos()
        for rock in self.rocks:
            x2,y2 = rock.get_pos()
            if math.sqrt((x1-x2)**2 + (y1 - y2)**2) <= 7:
                self.running = False 

    def remove_rocks(self):
        rocks_copy = copy.copy(self.rocks)
        for rock in rocks_copy:
            x1,y1 = rock.get_pos()
            for bullet in self.bullets:
                x2,y2 = bullet.get_pos()
                if math.sqrt((x1-x2)**2 + (y1-y2)**2) <= 7:
                    self.rocks.remove(rock)
            if y1 > 600:
                self.rocks.remove(rock)
                    
    def drop_rock(self):
        self.rocks.append(g_mechanics.rock())

    def shoot(self):
        self.bullets.append(g_mechanics.bullet(self.player.get_pos()))


game = GameView()
game.run()
                            
