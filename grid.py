import numpy as np
from copy import deepcopy

# Todo. make all moves valid, just not change the loc of robot.

# Todo.
# 1. gridworld
# 2. generate trajectories (how many, length, optimal policy)
# 3. get feature_matrix
# 4. fetch ground_r rewards for each states
# 5. run irl to get feature expectations (feature_matrix, gw.n_actions, discount, gw.transition_probability, trajectories, epochs, learning_rate)
# 6. plot it

# 1. All possible actions and states.

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

class grid_environment():
    def __init__(self):
        self.current_grid = grid
        self.possible_moves = []
        self.f_vector = np.zeros(max_y * max_x)
        self.time = 0

    def find_robot_pos(self, currrent_grid):

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '*':
                    return [i, j]

    def make_move(self, possible_moves, action, current_grid):

        possible_moves = grid_environment.find_possible_moves(current_grid)
        coordinates = grid_environment.find_robot_pos(current_grid)
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

        self.current_grid = grid
        return current_grid


    def find_possible_moves(self, current_grid):

        coordinates = grid_environment.find_robot_pos(grid)
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

        return self.possible_moves

    def features(self):
        # observables in the states
        # define phi(s_t) = sum of all the feature expectation phi_i at state s
        for i in range(max_y):
            for j in range(max_x):
                f_vector[i + max_y * j] = (grid[i][j] == ROBOT)

        return self.f_vector

    def rewards(self):
        # define r_t = linear combination of feature values phi_1..N at state s
        # w^T * phi(s_t) = w_1 * phi(s_1) + w_2 * phi(s_2) + ...

        pass

    def feature_expectation(self):
        # define mu(pi) = sum of discounted feature values phi(s_t) of a policy pi
        # mu(pi) = sum_t=0 gamma^t * phi(s_t)
        pass

for row in grid:
    print(" ".join(row))
print("")

#possible_moves = find_possible_moves(current_grid=grid)
#make_move(possible_moves, action=UP, current_grid=grid)

#for row in grid:
#    print(" ".join(row)))
