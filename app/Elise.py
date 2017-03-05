from flask import Flask, json, request
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

#Will move the snake towards the closest safe food
#covers the x displacement first followed by the y
#Returns the move direction that should be output my move
#Input: Grid - current grid setup
#       moves - list of allowed move direction
#       ourSnake - list of ourSnake coordinates
#       data - data
def approachFood(grid, moves, ourSnake, data):
    eats = Nikita.findSafeFood(grid, data)
    if len(eats) == 0:
        if len(moves) == 0:
            print("HOLYSHITITS EMPTY")
            return 'left'
        return moves[0]

    target = eats[0]
    dx = target[0] - ourSnake['coords'][0]
    dy = target[1] - ourSnake['coords'][1]

    if dx < 0 and 'left' in moves:
        return 'left'
    elif dx > 0 and 'right' in moves:
        return 'right'
    elif dy < 0 and 'up' in moves:
        return 'up'
    elif dy > 0 and 'down' in moves:
        return 'down'

    if len(moves) == 0:
            print("HOLYSHITITS EMPTY?!?!??!?!")
            return 'left'
    return moves[0]
