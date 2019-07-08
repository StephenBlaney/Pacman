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
        self.cell_width =WIDTH//28
        self.cell_height = HEIGHT//30
        self.load() #loads the images before the game starts

    def run(self):
        while self.running:
            if self.state == 'start': #True
                self.start_events()
                self.start_update()
                self.start_draw()
            elif self.state =='playing':
                self.playing_events()
                self.playing_update()
                self.playing_draw()
            else:
                self.running = False
            self.clock.tick(FPS)
        pygame.quit()
        sys.exit()

########################### HELPER FUNTIONS #################################
    def draw_text(self, words, screen, pos, size, colour, font_name, centered =False):
        font = pygame.font.SysFont(font_name, size)
        text = font.render(words, False, colour)
        text_size = text.get_size()
        if centered:
            pos[0] = pos[0] -text_size[0]//2
            pos[1] = pos[1] -text_size[1]//2
        screen.blit(text, pos)

    def load(self):
        self.background = pygame.image.load('background.png')
        self.background = pygame.transform.scale(self.background,(WIDTH,HEIGHT))

    def draw_grid(self):
        for x in range(WIDTH//self.cell_width):
            pygame.draw.line(self.screen, GREY,(x*self.cell_width, 0),( x*self.cell_width,HEIGHT)) #Paints the vertical grid
        for x in range(HEIGHT//self.cell_height):
            pygame.draw.line(self.screen, GREY,(0, x*self.cell_height),(WIDTH,x*self.cell_height)) # Paints the horizontal grid

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
        self.draw_text('PUSH SPACE BAR', self.screen, [WIDTH//2, HEIGHT//2-50], START_TEXT_SIZE,(170, 132, 58),START_FONT, centered = True)
        self.draw_text('1 PLAYER ONLY', self.screen, [WIDTH//2, HEIGHT//2+50], START_TEXT_SIZE,(44, 167, 198),START_FONT, centered= True)
        self.draw_text('HIGH SCORE', self.screen, [4,0], START_TEXT_SIZE,(255,255,255),START_FONT)
        pygame.display.update()


########################## PLAYING FUNTIONS ##################################

    def playing_events(self):
        for event in pygame.event.get(): #Gets a list of all the events that have happend since the last time it has been called
            if event.type == pygame.QUIT: #Player exits and the program is stopped
                self.running = False

    def playing_update(self):
        pass

    def playing_draw(self):
        self.screen.blit(self.background,(0,0))
        self.draw_grid() # function that will draw the grid in which pacman will traverse
        pygame.display.update()
