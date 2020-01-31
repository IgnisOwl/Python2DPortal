class Render:
    def __init__(self, screen, pygame):
        self.screen = screen
        self.pygame = pygame
    
    def render(self, objects):
        self.pygame.display.update()
        