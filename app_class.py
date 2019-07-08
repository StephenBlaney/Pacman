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
        self.state = 'start' # Set to intro

    def run(self):
        while self.running:
            if self.state == 'start': #True
                self.start_events()
                self.start_update()
                self.start_draw()
            else:
                pass
            self.clock.tick(FPS)
        pygame.quit()
        sys.exit()

########################### HELPER FUNTIONS #################################
    def draw_text(self, words, screen, pos, size, colour, font_name):
        font = pygame.font.SysFont(font_name, size)
        text = font.render(words, False, colour)
        text_size = text.get_size()
        screen.blit(text, pos)

########################### INTRO FUNTIONS #################################

    def start_events(self):
        for event in pygame.event.get(): #Gets a list of all the events that have happend since the last time it has been called
            if event.type == pygame.QUIT: #Player exits and the program is stopped
                self.running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.state = 'playing'

    def start_update(self):
        pass

    def start_draw(self):
        self.screen.fill(BLACK)
        self.draw_text('PUSH SPACE BAR', self.screen, START_TEXT_SIZE,(170, 132, 58),START_FONT)
        pygame.display.update()
