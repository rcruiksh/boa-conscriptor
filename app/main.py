from flask import Flask, json, request
import os
import random
import math
app = Flask(__name__)
#import king_codera.py

FOOD = 1
WALL = 2
HEADS = 3
BODIES = 4
TAILS = 5
EMPTY = 0

OUR_NAME = "boa-conscriptor"
OUR_HEAD = 97

board_width = 0
board_height = 0


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

#THIS FUNCTION RETURNS A LIST OF COORDINATES COORESPONDING TO DIRECTIONS AROUND OUR HEAD
#ORDER: right, left, down, up.
def adjCoords(ourSnake): #returns a list of 4 coordinates to check for extra snake body
    headPos = ourSnake['coords'][0];
    x = headPos[0];
    y = headPos[1];
    
    return [[x+1,y],[x-1,y],[x,y+1],[x,y-1]]; #right, left, down, up

#Removes our neck from possible directions to move and searches for other body
#parts around our head as to not hit ourselves
def checkBody(directions):
    directions.remove(adjDirection(ourSnake[0],ourSnake[1]))
    adjCoords = adjCoords(ourSnake);
    i = 0;
    if (directions.length == 1):
        return;
    else:
        if (adjCoords[0] in ourSnake):
            if 'right' in directions:
                directions.remove('right');
        if (adjCoords[1] in ourSnake):
            if 'left' in directions:
                directions.remove('left');
        if (adjCoords[2] in ourSnake):
            if 'down' in directions:
                directions.remove('down');
        if (adjCoords[3] in ourSnake):
            if 'up' in directions:
                directions.remove('up');
        return
        
def checkWall( ourSnake, board_height, board_width, directions):
    no_gos = adjCoords(ourSnake) #right, left, down, up
    L = []
    for x in range(0, 4):
        for y in range(0,2):
            if(no_gos[x][y] < 0 or no_gos[x][y] > board_width-1 or no_gos[x][y] > board_height-1):
                L.append(x)
    
    if (directions.length == 1):
        return;
    else:
        if 0 in L and 'right' in directions:
            directions.remove('right')
        if 1 in L and 'left' in directions:
            directions.remove('left')
        if 2 in L and 'down' in directions:
            directions.remove('down')
        if 3 in L and 'up' in directions:
            directions.remove('up')
        return
        
    
def firstCheck(directions):
    checkBody();
    checkWall();
    checkSnakes(); #within here: checkBodies with buffer 1, checkHeads with buffer 3
    if(directions.length==1):
        return directions[0];
    else:
        return directions;

def creategrid(data):
    grid = [[0 for col in range(data['width'])] for row in range(data['height'])]
    #FOOD
    for eats in data['food']:
        grid[eats[0]][eats[1]] = FOOD
    
    for snakes in data['snakes']:
        if snakes['id'] == data['you']:
            ourSnake = snakes
        for pts in snakes['coords']:
            grid[pts[0]][pts[1]] = BODIES
            grid[snakes['coords'][0]][snakes['coords'][1]] = HEADS
            if snakes == ourSnake:
                grid[snakes['coords'][0]][snakes['coords'][1]] = OUR_HEAD
    return grid, ourSnake


@app.route('/', methods=["GET"])
def index():
    return json.dumps({
        "Hello World": ""
    })


@app.route('/start', methods=["POST"])
def start():
    data = request.get_json()
    game_id = data['game_id']
    board_width = ['board_width']
    board_height = ['board_height']

    #head_url = '%s://%s/static/head.png' % ()

    return json.dumps({
        'color': '#0000FF',
        'taunt': 'Conscript',
        #'head_url': head_url,
        'name': 'Boa-Conscriptor'
        'head_type': "shades",
        'tail-type': "fat-rattle"
        })


@app.route('/move', methods=["POST"])
def move():
    data = request.get_json()

    directions = ['up', 'down', 'left', 'right']

    creategrid()
    directions = firstCheck(directions)
    mov = approachFood(grid, directions, ourSnake, data)
    
    return json.dumps({
        'move': mov,
        'taunt': 'conscript!'
    })



if __name__ == '__main__':
    # Get port or default if running locally
    port = int(os.environ.get("PORT", 5000))
    app.run(port=port, host="0.0.0.0")
    
    #comment
