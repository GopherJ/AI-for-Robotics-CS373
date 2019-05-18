# Author: zhao-zh10
# ----------
# User Instructions:
#
# Create a function compute_value which returns
# a grid of values. The value of a cell is the minimum
# number of moves required to get from the cell to the goal.
#
# If a cell is a wall or it is impossible to reach the goal from a cell,
# assign that cell a value of 99.
# ----------

grid = [[0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0]]
# grid = [[0, 0, 1, 0, 0, 0],
#         [0, 0, 1, 0, 0, 0],
#         [0, 0, 1, 0, 0, 0],
#         [0, 0, 0, 0, 1, 0],
#         [0, 0, 1, 1, 1, 0],
#         [0, 0, 0, 0, 1, 0]]
# grid = [[0, 0, 1, 0, 0, 0],
#         [0, 0, 1, 0, 0, 0],
#         [0, 0, 1, 0, 0, 0],
#         [0, 0, 1, 0, 1, 0],
#         [0, 0, 1, 1, 1, 0],
#         [0, 0, 0, 0, 1, 0]]
goal = [len(grid) - 1, len(grid[0]) - 1]
cost = 1  # the cost associated with moving from a cell to an adjacent one

delta = [[-1, 0],  # go up
         [0, -1],  # go left
         [1, 0],  # go down
         [0, 1]]  # go right

delta_name = ['^', '<', 'v', '>']

# # My Solution
# def compute_value(grid, goal, cost):
#     # ----------------------------------------
#     # insert code below
#     # ----------------------------------------
#
#     # make sure your function returns a grid of values as
#     # demonstrated in the previous video.
#     x = goal[0]
#     y = goal[1]
#     g = 0
#     open = [[g, x, y]]
#     closed = [[0 for col in range(len(grid[0]))] for row in range(len(grid))]
#     closed[x][y] = 1
#     value = [[99 for col in range(len(grid[0]))] for row in range(len(grid))]
#     value[x][y] = 0
#
#     while len(open) > 0:
#         open.sort()
#         open.reverse()
#         next = open.pop()
#         x = next[1]
#         y = next[2]
#         g = next[0]
#
#         for i in range(len(delta)):
#             x2 = x - delta[i][0]
#             y2 = y - delta[i][1]
#             if 0 <= x2 < len(grid) and 0 <= y2 < len(grid[0]):
#                 if grid[x2][y2] == 0 and closed[x2][y2] == 0:
#                     g2 = g + cost
#                     value[x2][y2] = g2
#                     closed[x2][y2] = 1
#                     open.append([g2, x2, y2])
#
#     for k in range(len(value)):
#         print(value[k])
#
#     return value


# Udacity Sebastian Thrun's Solution
def compute_value(grid, goal, cost):
    # ----------------------------------------
    # insert code below
    # ----------------------------------------

    # make sure your function returns a grid of values as
    # demonstrated in the previous video.
    value = [[99 for col in range(len(grid[0]))] for row in range(len(grid))]

    change = True
    while change:
        change = False

        for x in range(len(grid)):
            for y in range(len(grid[0])):

                if goal[0] == x and goal[1] == y:
                    if value[x][y] > 0:
                        value[x][y] = 0
                        change = True

                elif grid[x][y] == 0:
                    for a in range(len(delta)):
                        x2 = x + delta[a][0]
                        y2 = y + delta[a][1]

                        if 0 <= x2 < len(grid) and 0 <= y2 < len(grid[0]) and grid[x2][y2] == 0:
                            v2 = value[x2][y2] + cost

                            if v2 < value[x][y]:
                                change = True
                                value[x][y] = v2
    for i in range(len(value)):
        print(value[i])

    return value


compute_value(grid, goal, cost)