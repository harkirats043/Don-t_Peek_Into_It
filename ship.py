import pygame

class Ship:
    
    def __init__(self,ai_game):
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        self.moving_right = False
        self.moving_left = False
        
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()
        self.x = float(self.rect.x)
       
        
        self.rect.midbottom = self.screen_rect.midbottom
        self.moving_right = False
    
    def update(self):
        if self.moving_right:
            self.x += self.settings.ship_speed
        if self.moving_left:
            self.x -= self.settings.ship_speed
        
        self.rect.x = self.x    
        self.ship_speed = 1.5
    
         
    def blitme(self):
        self.screen.blit(self.image, self.rect)
        
        