import sys
from settings import Settings
import pygame

class AlienInvasion:
    
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        
        self.screen = pygame.display.set_mode(self.settings.screen_width,
                                              self.settings.screen_height)
        pygame.display.set_caption("Alien Invasion")
        
        #Set the background color
        self.bg_color=(230,230,230)
      
    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            # Redraw the screen during each pass through the loop
            self.screen.fill(self.settings.bg_color)
                    
            pygame.display.flip()
            self.clock.tick(60)
            
if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()   