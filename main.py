import pygame
from game import Game
from constants import SCREEN_X, SCREEN_Y, SCREEN_X_LOG, TITLE


def main():
    pygame.init()
    dimensions = [SCREEN_X + SCREEN_X_LOG, SCREEN_Y]
    screen = pygame.display.set_mode(dimensions)
    pygame.display.set_caption(TITLE)
    pygame.mouse.set_visible(False)
    request_exit = False
    clock = pygame.time.Clock()
    game = Game()
    while not request_exit:
        request_exit = game.event_handler()
        game.run()
        game.display_frame(screen)
        clock.tick(60)
    pygame.quit()


if __name__ == "__main__":
    main()
