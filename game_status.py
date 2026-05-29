class GameStats:
    def __init__(self, game_stats):
        self.settings = game_stats.settings
        self.reset_stats()
        self.game_active = True

    def reset_stats(self):
        self.ships_left = self.settings.ship_limit
