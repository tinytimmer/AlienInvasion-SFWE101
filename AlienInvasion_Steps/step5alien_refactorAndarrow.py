import sys 
 
import pygame 
 
from settings import Settings 
from ship import Ship 
 
class AlienInvasion: 
    #Overall class to manage game assets and behavior 
 
    def __init__(self): 
        #Initialize the game, and create game resources 
 
        pygame.init() 
        self.settings = Settings() 
 
        self.screen = pygame.display.set_mode ((self.settings.screen_width, self.settings.screen_height)) 
        pygame.display.set_caption ("Sharons Alien Invasion") 
         
        # Set the background color - colors are RBG colors:  amix of red, green, and blue.  Each color range is 0 to 255 
        self.bg_color = (10, 230, 230) 
 
        self.ship = Ship(self) 
 
    def run_game(self): 
        #Start the main loop for the game 
 
        while True: 
            # call a method to check to see if any keyboard events have occurred 
            self._check_events() 
            self.ship.update() 
            self._update_screen() 
 
    def _check_events(self): 
        #Respond to keypresses and mouse events. 
            # Did the player quit the game? 
        for event in pygame.event.get(): 
            if event.type ==pygame.QUIT: 
                sys.exit() 
            #  Did the player press a key? 
            elif event.type == pygame.KEYDOWN: 
                # Is the key the right arrow or is it the left arrow 
                if event.key == pygame.K_RIGHT: 
                    self.ship.moving_right = True 
                elif event.key == pygame.K_LEFT: 
                    self.ship.moving_left = True 
            # Did the player stop holding down the arrow keys? 
            elif event.type == pygame.KEYUP: 
                if event.key == pygame.K_RIGHT: 
                    self.ship.moving_right = False 
                elif event.key ==pygame.K_LEFT: 
                    self.ship.moving_left = False 
 
    def _update_screen(self): 
        #Update images on the screen, and flip to the new screen. 
        # Redraw the screen each pass through the loop 
        self.screen.fill(self.settings.bg_color) 
        self.ship.blitme() 
         # Make the most recently drawn screen visible 
        pygame.display.flip() 
         
if __name__ == '__main__': 
    # Make a game instance, and run the game 
    ai = AlienInvasion() 
    ai.run_game() 
 
quit()