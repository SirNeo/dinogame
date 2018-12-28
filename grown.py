import pygame
from wall import Wall
from constants import SCREEN_Y_GAME


class Grown(object):

    def __init__(self):
        self.scroll_x = 0
        self.objects_list = pygame.sprite.Group()

        # LINE
        self.objects_list.add(Wall(0, SCREEN_Y_GAME - 10, 50, 1))
        self.objects_list.add(Wall(50, SCREEN_Y_GAME - 10, 50, 1))
        self.objects_list.add(Wall(100, SCREEN_Y_GAME - 10, 50, 1))
        self.objects_list.add(Wall(150, SCREEN_Y_GAME - 10, 50, 1))
        self.objects_list.add(Wall(200, SCREEN_Y_GAME - 10, 50, 1))
        self.objects_list.add(Wall(250, SCREEN_Y_GAME - 10, 50, 1))
        self.objects_list.add(Wall(300, SCREEN_Y_GAME - 11, 1, 1))
        self.objects_list.add(Wall(301, SCREEN_Y_GAME - 12, 1, 1))
        self.objects_list.add(Wall(302, SCREEN_Y_GAME - 13, 1, 1))
        self.objects_list.add(Wall(303, SCREEN_Y_GAME - 14, 2, 1))
        self.objects_list.add(Wall(305, SCREEN_Y_GAME - 15, 4, 1))
        self.objects_list.add(Wall(309, SCREEN_Y_GAME - 14, 2, 1))
        self.objects_list.add(Wall(311, SCREEN_Y_GAME - 13, 1, 1))
        self.objects_list.add(Wall(312, SCREEN_Y_GAME - 12, 1, 1))
        self.objects_list.add(Wall(313, SCREEN_Y_GAME - 11, 1, 1))
        self.objects_list.add(Wall(314, SCREEN_Y_GAME - 10, 10, 1))
        self.objects_list.add(Wall(324, SCREEN_Y_GAME - 9, 1, 1))
        self.objects_list.add(Wall(325, SCREEN_Y_GAME - 8, 1, 1))
        self.objects_list.add(Wall(326, SCREEN_Y_GAME - 7, 16, 1))
        self.objects_list.add(Wall(342, SCREEN_Y_GAME - 8, 1, 1))
        self.objects_list.add(Wall(343, SCREEN_Y_GAME - 9, 2, 1))
        self.objects_list.add(Wall(345, SCREEN_Y_GAME - 10, 5, 1))
        self.objects_list.add(Wall(350, SCREEN_Y_GAME - 10, 50, 1))
        self.objects_list.add(Wall(400, SCREEN_Y_GAME - 10, 50, 1))
        self.objects_list.add(Wall(450, SCREEN_Y_GAME - 10, 50, 1))
        self.objects_list.add(Wall(500, SCREEN_Y_GAME - 10, 50, 1))
        self.objects_list.add(Wall(550, SCREEN_Y_GAME - 10, 50, 1))
        self.objects_list.add(Wall(600, SCREEN_Y_GAME - 10, 50, 1))
        self.objects_list.add(Wall(650, SCREEN_Y_GAME - 10, 50, 1))
        self.objects_list.add(Wall(700, SCREEN_Y_GAME - 10, 50, 1))

        x = 0
        for i in range(10):
            self.objects_list.add(Wall(x + 10, SCREEN_Y_GAME - 5, 1, 1))
            self.objects_list.add(Wall(x + 12, SCREEN_Y_GAME - 7, 4, 1))
            self.objects_list.add(Wall(x + 28, SCREEN_Y_GAME - 5, 4, 1))
            self.objects_list.add(Wall(x + 38, SCREEN_Y_GAME - 5, 1, 1))
            self.objects_list.add(Wall(x + 50, SCREEN_Y_GAME - 5, 1, 1))
            self.objects_list.add(Wall(x + 55, SCREEN_Y_GAME - 5, 1, 1))
            self.objects_list.add(Wall(x + 66, SCREEN_Y_GAME - 7, 4, 1))
            x += 70
