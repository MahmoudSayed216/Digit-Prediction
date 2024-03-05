import pygame as pg
pg.init()
pg.font.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW_KINDOF = (200, 200, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


FPS = 120

WIDTH, HEIGHT = 420, 500

ROWS = COLS = 28

TOOLBAR_HEIGHT = HEIGHT - WIDTH

PIXEL_SIZE = WIDTH//COLS

BG_COLOR = (160, 160, 160)

DRAW_GRID_LINES = True

def get_font(size):
    return pg.font.SysFont('comicsans', size)