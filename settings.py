class Settings():
    """a class to store all the settings for alien invasion"""

    def __init__(self):
        """initialize the game settings"""
        #screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        #ship setting
        self.ship_speed_factor = 1.5