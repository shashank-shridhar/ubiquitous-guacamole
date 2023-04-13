import pygame
from pygame import *
import sys
import os

class Shooter:
    def __init__(self):
        pygame.init()
        self.SCREEN_WIDTH = 600
        self.SCREEN_HEIGHT = 600
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH,self.SCREEN_HEIGHT))
        pygame.display.set_caption('ShooterGame')
        self.clock = pygame.time.Clock()

    def draw(self):
        self.screen.fill('gray')
    
    def update(self):
        pygame.display.flip()
        self.clock.tick(60)

    def check(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
    
    def run(self):
        while True:
            self.check()
            self.update()
            self.draw()
    
if __name__ == '__main__':
    shooter = Shooter()
    shooter.run()