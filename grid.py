import numpy as np
from copy import deepcopy


# All possible actions and states.

EMPTY = 'o'
WALL = '|'
ROBOT = '*'
HOME = 'Δ'
FLAG = 'ƒ'
LAVA = '†'

UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3

grid = [[EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
        [WALL, WALL, EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
        [HOME, EMPTY, ROBOT, LAVA, EMPTY],
        [EMPTY, EMPTY, WALL, EMPTY, FLAG]]

actions = [UP, DOWN, LEFT, RIGHT]

n_actions = len(actions)
max_x = len(grid[0])
max_y = len(grid)

def find_robot_pos(currrent_grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '*':
                return [i, j]

def make_move(possible_moves, action, current_grid):
    possible_moves = find_possible_moves(current_grid)
    coordinates = find_robot_pos(current_grid)
    x = coordinates[0]
    y = coordinates[1]

    if action == LEFT and LEFT in possible_moves:
        grid[x][y] = "o"
        grid[x][y-1] = "*"
    elif action  == RIGHT and RIGHT in possible_moves:
        grid[x][y] = "o"
        grid[x][y+1] = "*"
    elif action == UP and UP in possible_moves:
        grid[x][y] = "o"
        grid[x-1][y] = "*"
    elif action == DOWN and DOWN in possible_moves:
        grid[x][y] = "o"
        grid[x+1][y] = "*"
    elif action not in possible_moves:
        grid[x][y] = "*"
        print("Invalid move. Try another one.")

    current_grid = grid
    return current_grid


def find_possible_moves(current_grid):

    coordinates = find_robot_pos(grid)
    x = coordinates[0]
    y = coordinates[1]

    possible_moves = []

    for i in range(n_actions):
        if i == 0 and grid[x][y-1] == "o":
            possible_moves.append(LEFT)
        elif i == 1 and grid[x][y+1] == "o":
            possible_moves.append(RIGHT)
        elif i == 2 and grid[x-1][y] == "o":
            possible_moves.append(UP)
        elif i == 3 and grid[x+1][y] == "o":
            possible_moves.append(DOWN)

    return possible_moves

for row in grid:
    print(" ".join(row))
print("")

possible_moves = find_possible_moves(current_grid=grid)
make_move(possible_moves, action=UP, current_grid=grid)

for row in grid:
    print(" ".join(row))
