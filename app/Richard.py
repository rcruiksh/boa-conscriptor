import bottle
import os
import random
import math

#creategrid, 

OUR_NAME = "boa-conscriptor"
OUR_HEAD = 97

def varAdjCoords(ourSnake, i): #returns a list of coordinates at a distance of i from our snake head
    headPos = ourSnake['coords'][0];
    x = headPos[0];
    y = headPos[1];
    L1 = []
    L2 = []
    L = []
    R = []
    U = []
    D = []
   
    for c in range (0,(3+2*i)):
        for inc in range(-(i+1),(i+2)):
            c+=1
            L1.append(x+inc)
            L2.append(y+inc)
    
    for ind in range(0, (3+2*i)):
        L.append([L1[0],L2[ind]])#LEFT
        R.append([L1[-1],L2[ind]])#RIGHT
        U.append([L1[ind],L2[0]])#UP
        D.append([L1[ind],L2[-1]])#DOWN
        U.pop(0)
        U.pop(-1)
        D.pop(0)
        D.pop(-1)
    return L, R, U, D

def checkBodies(ourSnake, data, directions):
    buf = 1
    L, R, U, D = varAdjCoords(ourSnake, buf)
    for snakes in data['snakes']:
        for pts in snakes['coords']:
            
            if len(directions) == 1
                return
            
            elif pts in R and 'right' in directions:
                directions.remove('right')
            elif pts in L and 'left' in directions:
                directions.remove('left')
            elif pts in D and 'down' in directions:
                directions.remove('down')
            elif pts in U and 'up' in directions:
                directions.remove('up')
    return
                
                
    
def checkHeads(ourSnake, data, directions):
    buf = 3
    L, R, U, D = varAdjCoords(ourSnake, buf)
    for snakes in data['snakes']:
        if len(directions) == 1
            return
            
        elif snakes['coords'][0] in R and 'right' in directions:
            directions.remove('right')
        elif snakes['coords'][0] in L and 'left' in directions:
            directions.remove('left')
        elif snakes['coords'][0] in D and 'down' in directions:
            directions.remove('down')
        elif snakes['coords'][0] in U and 'up' in directions:
            directions.remove('up')
    return

width = data['width']
height = data['height']

def

def checkWall(grid, ourSnake, height, width, directions):
    no_gos = adjCoords(ourSnake) #right, left, down, up
    L = []
    for x in range(0, 4):
        for y in range(0,2):
            if(no_gos[x][y] < 0 or no_gos[x][y] > width-1 or no_gos[x][y] > height-1):
                L.append(x)
    if 0 in L:
        directions.remove('right')
    if 1 in L:
        directions.remove('left')
    if 2 in L:
        directions.remove('down')
    if 3 in L:
        directions.remove('up')
    return
                
        

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
