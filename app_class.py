import pygame
import sys
from settings import *

pygame.init()
vec = pygame.math.Vector2

class App:
    def __init__(self):
        self.screen = pygame.display.set_mode ((WIDTH, HEIGHT)) # Screen Setup
        self.clock = pygame.time.Clock() # Frame Setup
        self.running  = True # Game Running
        self.state = 'intro' # Set to intro

    def run(self):
        while self.running:
            if self.state == 'intro': #True
                self.intro_events()
                self.intro_update()
                self.intro_draw()
            else:
                pass
            self.clock.tick(FPS)
        pygame.quit()
        sys.exit()
########################### INTRO FUNTIONS #################################

    def intro_events(self):
        for event in pygame.event.get(): #Gets a list of all the events that have happend since the last time it has been called
            if event.type == pygame.QUIT: #Player exits and the program is stopped
                self.running = False

    def intro_update(self):
        pass

    def intro_draw(self):
        pygame.display.update()
