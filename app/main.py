import bottle
import os
import random
import math
#import king_codera.py

FOOD = 1
WALL = 2
HEADS = 3
BODIES = 4
TAILS = 5
EMPTY = 0

OUR_NAME = "boa-conscriptor"
OUR_HEAD = 97

board_width
board_height


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
    headPos = ourSnake[0];
    x = headPos[0];
    y = headPos[1];
    
    return [[x+1,y],[x-1,y],[x,y+1],[x,y-1]]; #right, left, down, up


def checkBody(directions):
    directions.remove(adjDirection(ourSnake[0],ourSnake[1]))
    adjCoords = adjCoords(ourSnake);
    i = 0;
    if (adjCoords[0] in ourSnake):
        directions.remove('right');
    if (adjCoords[1] in ourSnake):
        directions.remove('left');
    if (adjCoords[2] in ourSnake):
        directions.remove('down');
    if (adjCoords[3] in ourSnake):
        directions.remove('up');
    return
        
def checkWall( ourSnake, board_height, board_width, directions):
    no_gos = adjCoords(ourSnake) #right, left, down, up
    L = []
    for x in range(0, 4):
        for y in range(0,2):
            if(no_gos[x][y] < 0 or no_gos[x][y] > board_width-1 or no_gos[x][y] > board_height-1):
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




@bottle.route('/static/<path:path>')
def static(path):
    return bottle.static_file(path, root='static/')

@bottle.get('/')
def index():
    return {
        "Hello World": ""
    }


@bottle.post('/start')
def start():
    data = bottle.request.json
    game_id = data['game_id']
    board_width = data['width']
    board_height = data['height']

    head_url = '%s://%s/static/head.png' % (
        bottle.request.urlparts.scheme,
        bottle.request.urlparts.netloc
    )

    # TODO: Do things with data

    return {
        'color': '#00FF00',
        'taunt': '{} ({}x{})'.format(game_id, board_width, board_height),
        'head_url': head_url,
        'name': 'BoaConSCRIPTOR'
    }


@bottle.post('/move')
def move():
    data = bottle.request.json
    grid, ourSnake = creategrid(data)

    directions = ['up', 'down', 'left', 'right']
    
    return {
        'move': 'down',
        'taunt': 'conscript!'
    }


# Expose WSGI app (so gunicorn can find it)
application = bottle.default_app()
if __name__ == '__main__':
    bottle.run(application, host=os.getenv('IP', '0.0.0.0'), port=os.getenv('PORT', '8080'))
    
    #comment
