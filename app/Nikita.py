import bottle
import os
import random
import math

FOOD = 1
WALL = 2
HEADS = 3
BODIES = 4
TAILS = 5
EMPTY = 0


#roughly
#From each piece of food, find the closest snake head
    #Look at difference in X and Y coords
#If there exists a piece of food with our head being the closest
    #Return the coordinates of that food
def findSafeFood(grid, data):
    meals = []
    for eats in data['food']:
        minDistance = 9999
        closestSnake = ""

        for headpt in data['snakes']['coords']:
            if findDistance(grid, eats, headpt[0]) < minDistance:
                minDistance = findDistance(eats, headpt[0])
                closestSnake = data['snakes']['id']
        
        if closestSnake == data['you']:
            meals.append[eats]

    sort(meals, key = findDistance)
    return meals

def findDistance(grid, food, head):
    dx = abs(food[0] - head[0])
    dy = abs(food[1] - head[1])
    return dx + dy