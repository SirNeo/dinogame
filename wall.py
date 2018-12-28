import pygame
from constants import BLACK, SCREEN_X_GAME


class Wall(pygame.sprite.Sprite):

    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.scroll_x = 0

    def update(self):
        self.rect.x -= self.scroll_x
        if self.rect.x < -50:
            self.rect.x = SCREEN_X_GAME
