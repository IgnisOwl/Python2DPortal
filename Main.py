import pygame
import Render

SCREEN_X = 960
SCREEN_Y = 540

FPS = 60

COLORS = {
    "BLACK" : (0,0,0),
    "RED" : (255,0,0),
    "BLUE" : (0,0,255),
    "GREEN" : (0,255,0),
    "WHITE" : (255,255,255)
}

class Main:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_X, SCREEN_Y))
        self.clock = pygame.time.Clock()
        self.renderer = Render.Render(self.screen, pygame)
        
    def mainLoop(self):
        while True:
            self.renderer.render()
            self.clock.tick(FPS)
            
if __name__ == "__main__":
    main = Main()
    main.mainLoop()