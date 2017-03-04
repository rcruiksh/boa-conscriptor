import bottle
import os
import random
import math

OUR_NAME = "boa-conscriptor"
OUR_HEAD = 97

def creategrid(data):
    grid = [[0 for col in range(data['width'])] for row in range(data['height'])]
    #FOOD
    for eats in data['food']:
        grid[eats[0]][eats[1]] = FOOD
    
    for snakes in data['snakes']:
        if snakes['name'] == OUR_NAME:
            ourSnake = snakes
        for pts in snakes['coords']:
            grid[pts[0]][pts[1]] = BODIES
            grid[snakes['coords'][0]][snakes['coords'][1]] = HEADS
            if snakes == ourSnake:
                grid[snakes['coords'][0]][snakes['coords'][1]] = OUR_HEAD
    return grid, ourSnake
