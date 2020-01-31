import pygame
import Render

SCREEN_X = 950
SCREEN_Y = 550
#this means the level map is SPRITE_SIZE*AmountOfWalls = SCREEN_X or SCREEN_Y

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
DEFAULT_ITEMS = [["player", 0, SCREEN_Y-(SPRITE_SIZE*SIZE_MULTIPLIER), "right", 0]]
#format for player: [name, x, y, facing, gun_position(0-4)]
#format for portal: ["portal_orange", x, y, facing]
#format for walls: ["wall", x, y]

#dictionary of all the paths to sprites
IMAGE_PATHS = {
    "player_1" : "player_1.png"
}

mouseX=0
mouseY=0


#SIDESCROLL_BOUNDS = 50 #how many pixels the player can move before sidescrolling takes place

class Main:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_X, SCREEN_Y))
        self.clock = pygame.time.Clock()
        self.renderer = Render.Render(self.screen, pygame, COLORS, SPRITE_SIZE, SIZE_MULTIPLIER)
        self.items = DEFAULT_ITEMS
        
    def mousePos(self):
        return pygame.mouse.get_pos()

    def mainLoop(self):
        while True:
            self.renderer.render(self.items, IMAGE_PATHS)
            self.clock.tick(FPS)
            mouseX,mouseY=self.mousePos()
            print(mouseX)
            print(mouseY)
            
if __name__ == "__main__":
    main = Main()
    main.mainLoop()