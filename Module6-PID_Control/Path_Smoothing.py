# Author: zhao-zh10
# -----------
# User Instructions
#
# Define a function smooth that takes a path as its input
# (with optional parameters for weight_data, weight_smooth,
# and tolerance) and returns a smooth path. The first and
# last points should remain unchanged.
#
# Smoothing should be implemented by iteratively updating
# each entry in newpath until some desired level of accuracy
# is reached. The update should be done according to the
# gradient descent equations given in the instructor's note
# below (the equations given in the video are not quite
# correct).
# The formula you need to use in the exercise is as follows.
# Note that it is a little different from the ones in the video.
# y[i] <- y[i] + alpha (x[i] - y[i]) + beta (y[i+1] + y[i-1] - 2 * y[i])
# -----------

from copy import deepcopy
import matplotlib.pyplot as plt  # import this lib to visualize the result


# thank you to EnTerr for posting this on our discussion forum
def printpaths(path, newpath):
    for old, new in zip(path, newpath):
        print('[' + ', '.join('%.3f' % x for x in old) + '] -> [' + ', '.join('%.3f' % x for x in new) + ']')


# Don't modify path inside your function.
path = [[0, 0],
        [0, 1],
        [0, 2],
        [1, 2],
        [2, 2],
        [3, 2],
        [4, 2],
        [4, 3],
        [4, 4]]


def smooth(path, weight_data=0.5, weight_smooth=0.1, tolerance=0.000001):
    # Make a deep copy of path into newpath
    newpath = deepcopy(path)

    #######################
    ### ENTER CODE HERE ###
    #######################
    change = tolerance
    while change >= tolerance:
        change = 0.0
        for i in range(1, len(path) - 1):
            for j in range(len(path[0])):
                move_step = weight_data * (path[i][j] - newpath[i][j]) + weight_smooth * (
                            newpath[i + 1][j] + newpath[i - 1][j] - 2.0 * newpath[i][j])
                newpath[i][j] += move_step
                change += abs(move_step)
    return newpath  # Leave this line for the grader!


# Define this function plotpaths to visualize the result. But it cannot run in the Udacity code editor
# Because the Udacity code editor for this question doesn't have a display environment.
# I only use this function to generate visualization on my local computer.
def plotpaths(path, newpath):
    path_row = []
    path_col = []
    newpath_row = []
    newpath_col = []
    for i in range(len(path)):
        path_row.append(path[i][0])
        path_col.append(path[i][1])
        newpath_row.append(newpath[i][0])
        newpath_col.append(newpath[i][1])
    ax = plt.subplot(1, 1, 1)
    line1, = ax.plot(path_col, path_row, 'r-o', label='Original Path')
    line2, = ax.plot(newpath_col, newpath_row, 'b--x', label='Smooth Path')
    ax.legend()
    plt.gca().invert_yaxis()
    plt.show()


printpaths(path, smooth(path))
# plotpaths(path, smooth(path))  # You should comment this if you use the Udacity code editor to test the code.
