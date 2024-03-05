from utils import *
from utils.gaussian import gaussian_blur
import pickle
import numpy as np

model = pickle.load(open("model2.pkl", "rb"))

WIN = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Predicting Hand Written Digit")
clock = pg.time.Clock()
btn_y_pos = HEIGHT - TOOLBAR_HEIGHT/2 - 25
PREDICT_BUTTON = Button(20, btn_y_pos, 70, 50, GREEN, "Predict", BLACK)
CLEAR_BUTTON = Button(95, btn_y_pos, 70, 50, YELLOW_KINDOF, "Clear", BLACK)
CLOSE_BUTTON = Button(170, btn_y_pos, 70, 50, RED, "Close", BLACK)

# its a button but it acts as an output textbox
OUTPUT_BUTTON_ISH = Button(250, btn_y_pos, 160, 50, WHITE, "", BLACK)


def init_grid(rows, cols, color):
    grid = []
    for i in range(rows):
        grid.append([])
        for _ in range(cols):
            grid[i].append((color))
    return grid

def draw_grid(win, grid):
    for i, row in enumerate(grid):
        for j, pixel in enumerate(row):
            pg.draw.rect(win, pixel, (j*PIXEL_SIZE, i*PIXEL_SIZE, PIXEL_SIZE, PIXEL_SIZE))
    ## placing lines vertically and horizontally between the rectangles to make it look like a grid             
    if DRAW_GRID_LINES:
        for i in range(ROWS+1):
            pg.draw.line(win, BLACK, (0, i*PIXEL_SIZE),
                         (WIDTH, i*PIXEL_SIZE))
        for i in range(COLS+1):
            pg.draw.line(win, BLACK, (i*PIXEL_SIZE, 0), (i*PIXEL_SIZE, HEIGHT- TOOLBAR_HEIGHT))

def clear_grid():
    for i in range(ROWS):
        for j in range(COLS):
            grid[i][j] = WHITE

def get_row_col_from_pos(pos):
    x, y = pos
    row = y // PIXEL_SIZE
    col = x // PIXEL_SIZE
    if row >= ROWS or col >= COLS or row < 0 or col < 0:
        raise IndexError
    return row, col


def draw(win, grid):
    win.fill(BG_COLOR)
    draw_grid(win, grid)
    PREDICT_BUTTON.draw(win)
    CLEAR_BUTTON.draw(win)
    CLOSE_BUTTON.draw(win)
    OUTPUT_BUTTON_ISH.draw(win)
    pg.display.update()






def make_prediction():
    num_array = np.array(grid)
    num_array = num_array[:, :, 1] # all channels basically have the exact same values since the color is black,
                                   #so one channel is enough
    blurred_image = gaussian_blur(num_array)
    # grid = downsampled_image
    print(blurred_image.shape)
    num_array = blurred_image.reshape(784)
    inv_digit = -1*num_array + 255 
    print(inv_digit.shape)
    prediction = model.predict([inv_digit/255])[0]
    OUTPUT_BUTTON_ISH.text = f"The Digit is: {prediction}"

grid = init_grid(ROWS, COLS, WHITE)


run = True
while run:
    clock.tick(FPS)
    draw(WIN, grid)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        if pg.mouse.get_pressed()[0]:
            pos = pg.mouse.get_pos()
            if PREDICT_BUTTON.clicked(pos):
                make_prediction()
            if CLEAR_BUTTON.clicked(pos):
                clear_grid()
            if CLOSE_BUTTON.clicked(pos):
                run = False
            try:
                row_, col_ = get_row_col_from_pos(pos)
                grid[row_][col_] = BLACK
            except IndexError:
                pass
 
pg.quit()