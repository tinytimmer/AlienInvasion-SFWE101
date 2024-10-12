import sys 
 
import pygame 
 
class AlienInvasion: 
    #Overall class to manage game assets and behavior 
 
    def __init__(self): 
        #Initialize the game, and create game resources 
 
        pygame.init() 
        self.screen = pygame.display.set_mode((1200, 800)) 
        self.bg_image = pygame.image.load('images/starfield.png')
        pygame.display.set_caption ("Sharons Alien Invasion") 
        #testing: setting starry background
        
    def run_game(self): 
        #Start the main loop for the game 
 
        while True: 
            # Watch for keyboard and mouse events 
            for event in pygame.event.get(): 
                if event.type ==pygame.QUIT: 
                    sys.exit() 
            # Make the most recently drawn screen visible 
            #pygame.display.flip() 
            # Drawing image at position (0,0)
            self.screen.blit(self.bg_image, (0, 0))
            pygame.display.update()

         
if __name__ == '__main__': 
    # Make a game instance, and run the game 
    ai = AlienInvasion() 
    ai.run_game() 
 
quit() 