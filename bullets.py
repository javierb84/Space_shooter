import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, game_bullet):
        super().__init__()
        self.screen = game_bullet.screen
        self.settings = game_bullet.settings
        self.color = self.settings.bullet_color

        #Create bullet rectangle at position (0,0)
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = game_bullet.ship.rect.midtop

        self.y = float(self.rect.y)

    def update(self):
        #update position of bullet
        self.y -= self.settings.bullet_speed
        #update the rectangular position
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
