class Settings: 
    """ A class to store all settings for Alien Invasion""" 
 
    def __init__(self): 
        """ Initialize the game's settings""" 
        # Screen settings 
        self.screen_width = 1200 
        self.screen_height = 800 
        #self.bg_color = (255, 255, 255) 
 
        # Ship settings 
        self.ship_speed = 3 
        self.ship_limit = 3 
 
        # Bullet settings - dark grey bullets that a re 3 pixels wide and 15 pixels high.  Bullets travel slower than the ship.
        ## CT - changed the color of the bullets to red to see them better on the dark background & made them faster
        self.bullet_speed = 15 
        self.bullet_width = 3 
        self.bullet_height = 15 
        #self.bullet_color = (60, 60, 60)
        self.bullet_color = (255, 0, 0) 
        self.bullets_allowed = 3 
 
        # alien settings 
        self.alien_speed = 5.0 
        self.fleet_drop_speed = 10 
        # fleet direction of 1 represents right; -1 represents left. 
        self.fleet_direction = 1 