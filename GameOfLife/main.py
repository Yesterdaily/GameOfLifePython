import numpy as np
import tests as testing
import pygame
import sys

BLACK = (76, 31, 122)
WHITE = (255, 128, 0)
WINDOW_HEIGHT = 700
WINDOW_WIDTH = 700


def random_state(width, height):
    board_state = np.random.choice([0, 1], size=(height, width), p=[0.95, 0.05])
    return board_state

def dead_state(width, height):
    board_state = np.empty((width,height), dtype=int)
    board_state.fill(0)
    return board_state

def render(array):
    array_o = array.astype(object)
    for x, sub in enumerate(array_o):
        for y, element in enumerate(sub):
            if element == 1:
                array_o[x][y] = '#'
            else:
                array_o[x][y] = ' '
    return array_o

def check_neighbors(array, x, y):
    neighbors = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            if x+i >=0 and x+i < len(array) and y+j >=0 and y+j < len(array[0]) and array[x+i][y+j] == 1:
                neighbors += 1
    return neighbors

def next_board_state(initial_state):
    for x, sub in enumerate(initial_state):
        for y, element in enumerate(sub):
            neighbors = check_neighbors(initial_state, x, y)
            if element == 1 and neighbors < 2:
                initial_state[x][y] = 0
            elif element == 1 and neighbors > 3:
                initial_state[x][y] = 0
            elif element == 0 and neighbors == 3:
                initial_state[x][y] = 1
    return initial_state

def drawGrid(board_state):
    blockSize = 5 #Set the size of the grid block
    for x, sub in enumerate(board_state):
        for y, element in enumerate(sub):
            rect = pygame.Rect(x*blockSize, y*blockSize, blockSize, blockSize)
            pygame.draw.rect(SCREEN, BLACK, rect, element)

def main():
    board_state = random_state(140,140)
    global SCREEN, CLOCK
    pygame.init()
    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    CLOCK = pygame.time.Clock()
    SCREEN.fill(WHITE)

    while True:
        next_state = next_board_state(board_state)
        drawGrid(next_state)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        SCREEN.fill(WHITE)
     

if __name__ == "__main__":
    main()
    #testing.testThing()