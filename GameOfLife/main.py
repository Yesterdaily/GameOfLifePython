import numpy as np
import tests as testing
import pygame
import sys
import pandas as pd
import time
import asyncio

BLACK = (76, 31, 122)
WHITE = (255, 128, 0)
WINDOW_HEIGHT = 800
WINDOW_WIDTH = 1500
MODE = True


def random_state(width, height):
    board_state = np.random.choice([0, 1], size=(height, width), p=[0.7, 0.3])
    return board_state

def dead_state(width, height):
    board_state = np.empty((height, width), dtype=int)
    board_state.fill(0)
    return board_state

def load_board_state(txt):
    with open(txt, 'r') as file:
        matrix = []
        for line in file:
            # Split each line by spaces or tabs and convert to integers
            row = [int(x) for x in line.split()]
            matrix.append(row)
    
    return np.array(matrix)



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
    for i in range(-1, 2):  # Iterate over the range -1, 0, 1
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue  # Skip the cell itself
            if 0 <= x + i < len(array) and 0 <= y + j < len(array[0]):  # Check bounds
                if array[x + i][y + j] == 1:
                    neighbors += 1
    return neighbors

async def next_board_state(initial_state):
    new_state = dead_state(len(initial_state[0]),len(initial_state))
    for x, sub in enumerate(initial_state):
        for y, element in enumerate(sub):
            neighbors = check_neighbors(initial_state, x, y)
            if element == 1 and neighbors < 2 or neighbors > 3:
                new_state[x][y] = 0
            elif element == 0 and neighbors == 3:
                new_state[x][y] = 1
            elif element == 1 and 2<= neighbors <=3:
                new_state[x][y] = 1
    await asyncio.sleep(0)
    return new_state

async def drawGrid(board_state):
    blockSize = 5 #Set the size of the grid block
    for x, sub in enumerate(board_state):
        for y, element in enumerate(sub):
            rect = pygame.Rect(x*blockSize, y*blockSize, blockSize, blockSize)
            pygame.draw.rect(SCREEN, BLACK, rect, element)
    await asyncio.sleep(0)

async def main():
    if MODE:
        board_state = random_state(160,300)
    else:
        board_state = load_board_state("./test.txt")
    
    
    global SCREEN, CLOCK
    pygame.init()
    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    CLOCK = pygame.time.Clock()
    SCREEN.fill(WHITE)

    while True:

        next_state = await next_board_state(board_state)
        await drawGrid(next_state)


        board_state = next_state
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        SCREEN.fill(WHITE)
        await asyncio.sleep(0.0001) #control speed
     

if __name__ == "__main__":
    asyncio.run(main())
    #testing.testThing()