import sys 
 
import pygame 
 
class AlienInvasion: 
    #Overall class to manage game assets and behavior 
 
    def __init__(self): 
        #Initialize the game, and create game resources 
 
        pygame.init() 
        self.screen = pygame.display.set_mode((1200, 800)) 
        pygame.display.set_caption ("Sharons Alien Invasion") 
 
        # Set the background color - colors are RBG colors:  amix of red, green, and blue.  Each color range is 0 to 255 
        self.bg_color = (10, 50, 230) 
 
    def run_game(self): 
        #Start the main loop for the game 
 
        while True: 
            # Watch for keyboard and mouse events 
            for event in pygame.event.get(): 
                if event.type ==pygame.QUIT: 
                    sys.exit() 
 
            # Redraw the screen each pass through the loop 
            self.screen.fill(self.bg_color) 
            # Make the most recently drawn screen visible 
            pygame.display.flip() 
         
if __name__ == '__main__': 
    # Make a game instance, and run the game 
    ai = AlienInvasion() 
    ai.run_game() 
 
quit() 