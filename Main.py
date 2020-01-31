import pygame
import Render

SCREEN_X = 960
SCREEN_Y = 540

FPS = 60

pygame.display.set_caption("Portal")

COLORS = {
    "BLACK" : (0,0,0),
    "RED" : (255,0,0),
    "BLUE" : (0,0,255),
    "GREEN" : (0,255,0),
    "WHITE" : (255,255,255)
}

SPRITE_SIZE = 50
SIZE_MULTIPLIER = 1 #size multiplier, to make bigger or smaller

#NOTE: The item list is like: [["portal_orange", x, y, facing], ["player", x, y, facing]]    #Type, x, y, optional things... NOTE: portal can be facing 4 directions, floor, leftwall, ceiling, rightwall
DEFAULT_ITEMS = [["player", 0, SCREEN_Y-SPRITE_SIZE, "right", 0]] #name, x, y, facing, gun_position(0-4)

#dictionary of all the paths to sprites
IMAGE_PATHS = {
    "player_1" : "player_1.png"
}

class Main:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_X, SCREEN_Y))
        self.clock = pygame.time.Clock()
        self.renderer = Render.Render(self.screen, pygame, COLORS, SIZE_MULTIPLIER)
        self.items = DEFAULT_ITEMS
        
    def mainLoop(self):
        while True:
            self.renderer.render(self.items, IMAGE_PATHS)
            self.clock.tick(FPS)
            
if __name__ == "__main__":
    main = Main()
    main.mainLoop()