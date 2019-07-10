import pygame
from settings import *
vec = pygame.math.Vector2

class Player:
    def __init__ (self, app, pos):
        self.app = app
        self.grid_pos= pos
        self.pix_pos = self.get_pix_pos()
        self.direction = vec(1,0)
        self.stored_direction = None

    def update(self):
        self.pix_pos += self.direction
        if self.time_to_move():
            if self.stored_direction != None:
                self.direction = self.stored_direction

        # Setting grid positon in reference to pixel position
        self.grid_pos[0] = (self.pix_pos[0]-TOP_BOTTOM_BUFFER+self.app.cell_width//2)//self.app.cell_width +1
        self.grid_pos[1] = (self.pix_pos[1]-TOP_BOTTOM_BUFFER+self.app.cell_height//2)//self.app.cell_height +1

    def draw (self):
        pygame.draw.circle(self.app.screen, PLAYER_COLOUR, (int(self.pix_pos.x) , int(self.pix_pos.y)), self.app.cell_width//2 - 2)

        # Drawing the grid pos rect
        pygame.draw.rect(self.app.screen,RED,(self.grid_pos[0]*self.app.cell_width + TOP_BOTTOM_BUFFER//2,
        self.grid_pos[1]*self.app.cell_height+ TOP_BOTTOM_BUFFER//2, self.app.cell_width,self.app.cell_height), 1)

    def move(self, direction):
        self.stored_direction = direction

    def get_pix_pos(self):
        return vec((self.grid_pos.x*self.app.cell_width)+TOP_BOTTOM_BUFFER//2 +self.app.cell_width//2,
        (self.grid_pos.y*self.app.cell_height)+ TOP_BOTTOM_BUFFER//2 +self.app.cell_height//2)
        print(self.grid_pos, self.pix_pos)

    def time_to_move(self):
        if int(self.pix_pos.x +TOP_BOTTOM_BUFFER//2) % self.app.cell_width == 0:
            if self.direction ==vec(1,0) or self.direction ==vec(-1,0):
                return True

        if int(self.pix_pos.y + TOP_BOTTOM_BUFFER//2) % self.app.cell_height == 0:
            if self.direction ==vec(0,1) or self.direction ==vec(0,-1):
                return True
