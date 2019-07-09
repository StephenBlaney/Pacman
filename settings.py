from pygame.math import Vector2 as vec


# screen settings
WIDTH, HEIGHT = 560, 620 # Dimesions of the orignal Pacman game
TOP_BOTTOM_BUFFER = 50
MAZE_WIDTH, MAZE_HEIGHT = WIDTH-TOP_BOTTOM_BUFFER, HEIGHT-TOP_BOTTOM_BUFFER
FPS = 60


#colour settings
BLACK = (0,0,0)
RED = (208,22,22)
GREY = (107,107,107)
WHITE = (255,255,255)
PLAYER_COLOUR = (190, 194, 15)

#font settings
START_TEXT_SIZE = 16
START_FONT = 'arial black'

#player settings
PLAYER_START_POS = vec(1,1)

#mob settings
