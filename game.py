import pygame
import time
import random
from wall import Wall
from dinosaur import Dinosaur
from grown import Grown
from enemy import Enemy
from constants import SCREEN_X_GAME, SCREEN_Y_GAME, BLACK, WHITE, SPEED, WEIGHTS_ENEMY, TYPE_ENEMY, RANGE_TIME_NEXT_ENEMY, SCORE_X_LEVEL, ENEMIES_X_LEVEL


class Game(object):

    def __init__(self):
        self.score = 0
        self.cont_enemies_x_level = 0
        self.level = 0
        self.over = False
        self.pause = False
        self.messages = []
        self.sprites_list = pygame.sprite.Group()
        self.walls_list = pygame.sprite.Group()
        self.enemies_list = pygame.sprite.Group()
        self.define_borders()
        self.grown = Grown()
        self.sprites_list.add(self.grown.objects_list)
        self.dino = Dinosaur()
        self.dino.walls = self.walls_list
        self.sprites_list.add(self.dino)
        self.last_timestamp = time.time()
        self.next_level_timestamp = time.time()

    def define_borders(self):
        # BORDER LEFT
        wall = Wall(0, 0, 2, SCREEN_Y_GAME)
        self.walls_list.add(wall)
        self.sprites_list.add(wall)

        # BORDER TOP
        wall = Wall(2, 0, SCREEN_X_GAME, 2)
        self.walls_list.add(wall)
        self.sprites_list.add(wall)

        # BORDER RIGHT
        wall = Wall(SCREEN_X_GAME, 0, 2, SCREEN_Y_GAME)
        self.walls_list.add(wall)
        self.sprites_list.add(wall)

        # BORDER BOTTOM
        wall = Wall(0, SCREEN_Y_GAME - 2, SCREEN_X_GAME, 2)
        self.walls_list.add(wall)
        self.sprites_list.add(wall)

    def event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True

            if event.type == pygame.KEYDOWN:
                if self.over:
                    self.reset_game()
                if event.key == pygame.K_p:
                    self.pause = not self.pause
                if not self.pause:
                    if event.key == pygame.K_UP:
                        self.dino.jump()
                    if event.key == pygame.K_DOWN:
                        self.dino.stand_down()

            if event.type == pygame.KEYUP:
                if not self.pause:
                    if event.key == pygame.K_DOWN:
                        self.dino.stand_up()

        return False

    def run(self):
        if not self.over:
            self.sprites_list.update()
            self.check_level()
            if self.pause:
                self.scroll_scene(0)
            else:
                self.scroll_scene(SPEED[self.level])
                self.increment_score()
                self.calculate_next_enemy()
                self.check_dino_impacted()

    def pause_game(self, screen):
        font = pygame.font.SysFont("serif", 25)
        text = font.render("Pause", True, BLACK)
        center_x = (SCREEN_X_GAME // 2) - (text.get_width() // 2)
        center_y = (SCREEN_Y_GAME // 2) - (text.get_height() // 2)
        screen.blit(text, [center_x, center_y])

        self.last_timestamp = time.time()

    def reset_game(self):
        self.score = 0
        self.cont_enemies_x_level = 0
        self.over = False
        self.level = 0
        self.last_timestamp = time.time()
        self.enemies_list.empty()
        sprites_list_temp = pygame.sprite.Group()
        sprites_list_temp.add(enemy for enemy in self.sprites_list if enemy.__module__ != 'enemy' and enemy.__module__ != 'dinosaur')
        self.sprites_list = sprites_list_temp
        self.dino = Dinosaur()
        self.dino.walls = self.walls_list
        self.sprites_list.add(self.dino)

    def check_level_old(self):
        """ deprecated. Not used """
        next_level = int((self.score // SCORE_X_LEVEL))
        self.level = next_level if next_level <= len(SPEED) - 1 else len(SPEED) - 1

    def check_level(self):
        if self.cont_enemies_x_level > ENEMIES_X_LEVEL[self.level]:
            next_level = self.level + 1
            if next_level <= len(SPEED) - 1:
                self.level = next_level
                self.cont_enemies_x_level = 0
                self.next_level_timestamp = time.time()

    def check_dino_impacted(self):
        if self.dino.impacted:
            self.over = True

    def log(self, message):
        """ Only for development propose """
        self.messages.append(message)

    def increment_score(self):
        tot_enemies = len(self.enemies_list)
        tmp_enemies_list = pygame.sprite.Group()
        tmp_enemies_list.add(enemy for enemy in self.enemies_list if not enemy.removable)
        num_enemies = len(tmp_enemies_list)
        self.enemies_list = tmp_enemies_list
        self.score += (tot_enemies - num_enemies)
        self.cont_enemies_x_level += (tot_enemies - num_enemies)

    def add_enemy_to_lists(self, enemy):
        self.enemies_list.add(enemy)
        self.sprites_list.add(enemy)
        self.dino.enemies_list.add(enemy)
        self.grown.objects_list.add(enemy)

    def calculate_next_enemy(self):
        wait = random.uniform(RANGE_TIME_NEXT_ENEMY[self.level][0], RANGE_TIME_NEXT_ENEMY[self.level][1])
        if time.time() - self.last_timestamp > wait:
            self.last_timestamp = time.time()
            result = random.choices(range(len(TYPE_ENEMY)), WEIGHTS_ENEMY[self.level])
            self.create_enemy(TYPE_ENEMY[result[0]])

    def create_enemy(self, enemy_type):
        self.add_enemy_to_lists(Enemy(enemy_type['x'], enemy_type['y'], enemy_type['w'], enemy_type['h']))

    def scroll_scene(self, scroll_x):
        for element in self.grown.objects_list:
            element.scroll_x = scroll_x

    def display_frame(self, screen):
        screen.fill(WHITE)
        self.display_score(screen)
        self.display_log(screen)
        self.display_level(screen)

        if self.over:
            self.display_game_over(screen)

        if self.pause:
            self.pause_game(screen)

        self.sprites_list.draw(screen)
        pygame.display.flip()

    def display_game_over(self, screen):
        font = pygame.font.SysFont("serif", 25)
        text = font.render("Game Over", True, BLACK)
        center_x = (SCREEN_X_GAME // 2) - (text.get_width() // 2)
        center_y = (SCREEN_Y_GAME // 2) - (text.get_height() // 2)
        screen.blit(text, [center_x, center_y])

    def display_score(self, screen):
        font = pygame.font.SysFont("serif", 25)
        text = font.render("Score: " + str(int(self.score)), True, BLACK)
        x = SCREEN_X_GAME - text.get_width() - 20
        screen.blit(text, [x, 10])

    def display_changes(self, screen):
        """ Only for development purpose """
        font = pygame.font.SysFont("serif", 25)
        text1 = font.render("Change X: " + str(self.dino.change_x), True, BLACK)
        x = 10
        screen.blit(text1, [x, 10])
        text2 = font.render("Change Y: " + str(self.dino.change_y), True, BLACK)
        x = text1.get_width() + 20
        screen.blit(text2, [x, 10])

    def display_cords(self, screen):
        """ Only for development purpose """
        font = pygame.font.SysFont("serif", 25)
        text1 = font.render("RECT X: " + str(self.dino.rect.x), True, BLACK)
        x = 10
        screen.blit(text1, [x, 40])
        text2 = font.render("RECT Y: " + str(self.dino.rect.y), True, BLACK)
        x = text1.get_width() + 20
        screen.blit(text2, [x, 40])

    def display_level(self, screen):
        if time.time() - self.next_level_timestamp < 0.5 or (time.time() - self.next_level_timestamp > 1 and time.time() - self.next_level_timestamp < 1.5):
            color = WHITE
        else:
            color = BLACK
        font = pygame.font.SysFont("serif", 25)
        txt_level = font.render("Level: ", True, BLACK)
        num_level = font.render(str(self.level + 1), True, color)
        screen.blit(txt_level, [20, 10])
        screen.blit(num_level, [20 + txt_level.get_width(), 10])

    def display_log(self, screen):
        font = pygame.font.SysFont("serif", 10)
        y = 0
        for message in reversed(self.messages):
            text = font.render(message, True, BLACK)
            x = SCREEN_X_GAME + 10
            screen.blit(text, [x, y])
            y += 12
