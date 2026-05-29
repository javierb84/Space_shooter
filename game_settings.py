
class Settings:
    # This class saves all the settings for our game

    def __init__(self):
        self.screen_width = 1080
        self.screen_height = 760
        self.bg_color = (230, 230, 230)

        # spaceship settings
        self.ship_speed = 1.7
        self.ship_limit = 5

        # bullet settings
        self.bullet_speed = 1.3
        self.bullet_width = 5
        self.bullet_height = 10
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 6

        self.alien_speed = 0.8
        self.fleet_drop_speed = 9
        self.fleet_direction = 1
