#from flask import Flask, json, request
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

# needs to be called when we are 1/6th of our snake length away
# from target food
def circleFood(grid, moves, ourSnake, data, target):
    sideLength = len(ourSnake)/3

    square = []
    for coord in range (target[0] - sideLength * 1/2, target[0] + sideLength * 1/2):
        square.append([coord][target[1 + 1/2 * sideLength]])

    for coord in range (target[0] - sideLength * 1/2, target[0] + sideLength * 1/2):
        square.append([coord][target[1 - 1/2 * sideLength]])

    for coord in range (target[1] - sideLength * 1/2, target[1] + sideLength * 1/2):
        square.append([target[0] + 1/2 * sideLength][coord])

    for coord in range (target[1] - sideLength * 1/2, target[1] + sideLength * 1/2):
        square.append([target[0] - 1/2 * sideLength][coord])