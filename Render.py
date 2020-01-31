class Render:
    def __init__(self, screen, pygame, colors, spriteSize, sizeMultiplier):
        self.screen = screen
        self.pygame = pygame
        self.colors = colors
        self.size_multiplier = sizeMultiplier
        self.sprite_size = spriteSize
    
    def render(self, objects, sprite_image_paths):
        self.screen.fill(self.colors["WHITE"])
        
        #get the current object we are handling in all the objects provided
        for object in objects:
            #if the object is a player, get the sprite based on the facing, and gun position
            if(object[0][0:6] == "player"):
                if(object[3] == "right"): #facing right
                    objectImg = self.pygame.image.load(sprite_image_paths["player_1"])
                elif(object[3] == "left"):
                    objectImg = self.pygame.image.load(sprite_image_paths["player_2"])
                    
            objectX = object[1]
            objectY = object[2]
            
            objectImg = self.pygame.transform.scale(objectImg, (self.sprite_size * self.size_multiplier, self.sprite_size * self.size_multiplier))
            self.screen.blit(objectImg, (objectX, objectY))
            
        self.pygame.display.update()
        