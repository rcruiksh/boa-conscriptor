import bottle
import os
import random
import math
import king_codera.py

def adjDirection(headPos,bodyPos):
    if(headPos[0]-bodyPos[0] == 0): #if no difference in x direction
        if(headPos[1]-bodypos[1] < 0): #if body is  below head
            return 'down'; #down is to be removed from directions list
        else:
            return 'up'; #up is to be removed from directions list
        else: #if there is a difference in the x direction
        if(headPos[0] - bodyPos[0] < 0): #if body is to the right of head
            return 'right'; #right is to be removed from directions list
        else:
            return 'left'; #left is to be removed from directions list


#THIS FUNCTION RETURNS A LIST OF COORDINATES COORESPONDING TO DIRECTIONS
#ORDER: right, left, down, up.
def adjCoords(ourSnake): #returns a list of 4 coordinates to check for extra snake body
    headPos = ourSnake['coords'][0];
    x = headPos[0];
    y = headPos[1];
    
    return [[x+1,y],[x-1,y],[x,y+1],[x,y-1]]; #right, left, down, up

def varAdjCoords(ourSnake,buff):
    headPos = ourSnake['coords'][0];
    x = headPos[0];
    y = headPos[1];

    if(buff==0)
        return list;
    for inc in range(-(i+1),(i+2)):
        for c in range (0,(3+2i)):
            L1[c] = x+inc
            L2[c] = y+inc
    return L1.remove(varAdjCoords(ourSnake,buff-1)),L2.remove(varAdjCoords(ourSnake,buff-1));


def checkBody(directions):
    directions.remove(adjDirection(ourSnake[0],ourSnake[1]))
    adjCoords = adjCoords(ourSnake);
    i = 0;
    if (adjCoords[0] in ourSnake and directions.length > 0):
        if 'right' is in directions:
            directions.remove('right');
    if (adjCoords[1] in ourSnake and directions.length > 0):
        if 'left' is in directions:
            directions.remove('left');
    if (adjCoords[2] in ourSnake and directions.length > 0):
        if 'down' is in directions:
            directions.remove('down');
    if (adjCoords[3] in ourSnake and directions.length > 0):
        if 'up' is in directions:
            directions.remove('up');

def firstCheck(directions):
    checkBody();
    checkWall();
    checkSnakes(); #within here: checkBodies with buffer 1, checkHeads with buffer 3
    if(directions.length==1):
        return directions[0];
    else:
        return directions;

