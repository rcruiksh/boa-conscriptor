from flask import Flask, json, request
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
    #Return the coordinates of those foods in a list
def findSafeFood(grid, data):
    meals = []
    for eats in data['food']:
        minDistance = 9999
        minToUs = 9999
        closestSnake = ""

        for snek in data['snakes']:
            headpt = snek['coords'][0]
            if findDistance(grid, eats, headpt) < minDistance:
                minDistance = findDistance(grid, eats, headpt)
                closestSnake = snek['id']
        
        if closestSnake == data['you']:
            if(findDistance(grid, eats, closestSnake[0]) < minToUs)
                minToUs = findDistance(grid, eats, closestSnake[0])
                meals[0] = eats


    #sort(meals, key = findDistance(grid, this, data['snakes']['coords'][0])) #There's almost no way in hell that this should work
    return meals

#Finds the distance between the food and head coordinates
#TODO: Take other snake bodies into account
def findDistance(grid, food, head):
    dx = abs(food[0] - head[0])
    dy = abs(food[1] - head[1])
    return dx + dy