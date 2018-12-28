import pygame
from constants import GRAY, SCREEN_Y_GAME


SIZE_DINO_INIT = [40, 60]
POS_DINO_INIT = [40, SCREEN_Y_GAME - 160]
SIZE_DINO_SITTING = [40, 30]
POS_DINO_SITTING = [40, SCREEN_Y_GAME - 32]


class Dinosaur(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface(SIZE_DINO_INIT)
        self.image.fill(GRAY)
        self.rect = self.image.get_rect()
        self.change_x = 0
        self.change_y = 0
        self.walls = None
        self.rect.x = POS_DINO_INIT[0]
        self.rect.y = POS_DINO_INIT[1]
        self.is_down = False
        self.is_jumping = False
        self.impacted = False
        self.enemies_list = pygame.sprite.Group()

    def update(self):
        self.calc_gravity()
        self.rect.x += self.change_x

        wall_impact_list = pygame.sprite.spritecollide(self, self.walls, False)
        for wall in wall_impact_list:
            if self.change_x > 0:
                self.rect.right = wall.rect.left
            else:
                self.rect.left = wall.rect.right

        self.rect.y += self.change_y

        wall_impact_list = pygame.sprite.spritecollide(self, self.walls, False)
        for wall in wall_impact_list:
            self.is_jumping = False
            if self.change_y > 0:
                self.rect.bottom = wall.rect.top + 2
            else:
                self.rect.top = wall.rect.bottom - 2

        self.impacted = True if len(pygame.sprite.spritecollide(self, self.enemies_list, False)) > 0 else False

    def calc_gravity(self):
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += .35

        if self.rect.y >= SCREEN_Y_GAME - self.rect.height - 2 and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = SCREEN_Y_GAME - self.rect.height - 2

    def jump(self):
        self.is_jumping = True
        self.rect.y += 2
        self.rect.y -= 2
        if self.rect.bottom >= SCREEN_Y_GAME - 2:
            self.change_y = - 7

    def stand_down(self):
        if not self.is_jumping:
            self.image = pygame.transform.scale(self.image, (int(self.image.get_size()[0]), int(self.image.get_size()[1] / 2)))
            self.image.fill(GRAY)
            self.rect = self.image.get_rect()
            self.rect.x = POS_DINO_SITTING[0]
            self.rect.y = SCREEN_Y_GAME - 2 - self.image.get_size()[1]
            self.is_down = True

    def stand_up(self):
        if self.is_down:
            self.image = pygame.transform.scale(self.image, (int(self.image.get_size()[0]), int(self.image.get_size()[1] * 2)))
            self.image.fill(GRAY)
            self.rect = self.image.get_rect()
            self.rect.x = POS_DINO_SITTING[0]
            self.rect.y = SCREEN_Y_GAME - 2 - self.image.get_size()[1]
            self.is_down = False

    def stop(self):
        self.change_x = 0
