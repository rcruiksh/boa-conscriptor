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


def checkBody(directions):
    directions.remove(adjDirection(ourSnake[0],ourSnake[1]))

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




@bottle.route('/static/<path:path>')
def static(path):
    return bottle.static_file(path, root='static/')


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
    checkBody();
    

    return {
        'move': 'down',
        'taunt': 'conscript!'
    }


# Expose WSGI app (so gunicorn can find it)
application = bottle.default_app()
if __name__ == '__main__':
    bottle.run(application, host=os.getenv('IP', '0.0.0.0'), port=os.getenv('PORT', '8080'))
    
    #comment
