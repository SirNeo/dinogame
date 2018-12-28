# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
VIOLET = (98, 0, 255)
GRAY = (111, 111, 111)

# Dimensions
SCREEN_X = 600
SCREEN_Y = 200
SCREEN_X_GAME = 600
SCREEN_Y_GAME = 200
SCREEN_X_LOG = 0  # Set to any value > 0 for display log section

TITLE = 'Dinosaurus'
SPEED = [7, 8, 9, 10, 10, 11, 12, 13]
SCORE_X_LEVEL = 3
ENEMIES_X_LEVEL = [3, 5, 7, 9, 11, 13, 15, 100]
RANGE_TIME_NEXT_ENEMY = [
    [2, 4],
    [2, 3],
    [1, 2],
    [0.9, 1.5],
    [0.8, 1.3],
    [0.9, 1.2],
    [0.8, 1.2],
    [0.6, 0.8]
]
# TYPE_ENEMY = ['CACTUS', 'FLIER']
# Add X columns for each enemy type
WEIGHTS_ENEMY = [
    [1, 0, 0, 0],
    [0.8, 0.2, 0, 0],
    [0.6, 0.2, 0.1, 0.1],
    [0.5, 0.2, 0.2, 0.1],
    [0.4, 0.2, 0.2, 0.2],
    [0.3, 0.2, 0.3, 0.2],
    [0.2, 0.4, 0.2, 0.2],
    [0.1, 0.3, 0.3, 0.3],
]

TYPE_ENEMY = [{'name': 'CACTUS',
               'x': SCREEN_X_GAME + 10,
               'y': SCREEN_Y_GAME - 50,
               'w': 20,
               'h': 40
               },
              {'name': 'FLIER_UP',
               'x': SCREEN_X_GAME + 10,
               'y': SCREEN_Y_GAME - 80,
               'w': 40,
               'h': 30
               },
              {'name': 'FLIER_DOWN',
               'x': SCREEN_X_GAME + 10,
               'y': SCREEN_Y_GAME - 60,
               'w': 40,
               'h': 30
               },
              {'name': 'CACTUS_WIDE',
               'x': SCREEN_X_GAME + 10,
               'y': SCREEN_Y_GAME - 50,
               'w': 60,
               'h': 40
               }
              ]
