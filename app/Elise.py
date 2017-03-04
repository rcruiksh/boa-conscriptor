import bottle
import os
import random
import math
import Nikita

FOOD = 1
WALL = 2
HEADS = 3
BODIES = 4
TAILS = 5
EMPTY = 0

def approachFood(grid, moves, ourSnake, data):
    eats = findSafeFood(grid, data)
    if len(eats) == 0:
        return list[0]

    target = eats[0]
    dx = target[0] - ourSnake['coords'[0][0]]
    dy = target[1] - ourSnake['coords'[0][1]]

    if dx < 0 and 'left' in moves:
        return 'left'
    elif dx > 0 and 'right' in moves:
        return 'right'
    elif dy < 0 and 'up' in moves:
        return 'up'
    elif dy > 0 and 'down' in moves:
        return 'down'

    return list[0]