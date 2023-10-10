import sys
from settings import Settings
from ship import Ship
import pygame

class AlienInvasion:
    
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        
        self.screen = pygame.display.set_mode(self.settings.screen_width,
                                              self.settings.screen_height)
        pygame.display.set_caption("Alien Invasion")
        self.ship=Ship(self)
        
        #Set the background color
        self.bg_color=(230,230,230)
      
    def run_game(self):
        while True:
            self.check_events()
            self.ship.update()
            self._update_screen()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.ship.moving_right = True
                    elif event.key == pygame.K_LEFT:
                        self.ship.moving_left = True
                        
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        self.ship.moving_right = False
                    elif event.key == pygame.K_LEFT:
                        self.ship.moving_left = False
                    
                    
            # Redraw the screen during each pass through the loop
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()
            
            def _check_events(self):
                for event in pygame.event.get():
                    if event.type == pygame.QUIT
                    sys.exit()
                    
            def _update_screen(self):
               pygame.display.flip()
               self.clock.tick(60)
            
if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()   