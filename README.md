![Pacman](https://user-images.githubusercontent.com/22968181/61118352-75cb1480-a490-11e9-8d42-6cc5dc734c00.png)


# Pacman

Pacman game will be devopled using python and the pygame libary The player controls the titular character, as he must eat all the dots inside an enclosed maze while avoiding four colored ghosts. Eating large flashing "Power Pellets" will cause the ghosts to turn blue and reverse direction, allowing Pac-Man to eat them for bonus points. It was the first game to run on the Namco Pac-Man arcade board

This is the template of every game i start with Pygame, 

```Python

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
```
