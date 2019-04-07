# coding: utf-8
# Author: zhao-zh10
# The function localize takes the following arguments:
# 
# colors:
#        2D list, each entry either 'R' (for red cell) or 'G' (for green cell). The environment is cyclic.
#
# measurements:
#        list of measurements taken by the robot, each entry either 'R' or 'G'
#
# motions:
#        list of actions taken by the robot, each entry of the form [dy,dx],
#        where dx refers to the change in the x-direction (positive meaning
#        movement to the right) and dy refers to the change in the y-direction
#        (positive meaning movement downward)
#        NOTE: the *first* coordinate is change in y; the *second* coordinate is
#              change in x
#
# sensor_right:
#        float between 0 and 1, giving the probability that any given
#        measurement is correct; the probability that the measurement is
#        incorrect is 1-sensor_right
#
# p_move:
#        float between 0 and 1, giving the probability that any given movement
#        command takes place; the probability that the movement command fails
#        (and the robot remains still) is 1-p_move; the robot will NOT overshoot
#        its destination in this exercise
#
# The function should RETURN (not just show or print) a 2D list (of the same
# dimensions as colors) that gives the probabilities that the robot occupies
# each cell in the world.
#
# Compute the probabilities by assuming the robot initially has a uniform
# probability of being in any cell.
#
# Also assume that at each step, the robot:
# 1) first makes a movement,
# 2) then takes a measurement.
#
# Motion:
#  [0,0] - stay
#  [0,1] - right
#  [0,-1] - left
#  [1,0] - down
#  [-1,0] - up
# For the purpose of this homework assume that the robot can move only left, right, up, or down. It cannot move diagonally. 
# Also, for this assignment, the robot will never overshoot its destination square; it will either make the movement or it will remain stationary.

def localize(colors,measurements,motions,sensor_right,p_move):
    # initializes p to a uniform distribution over a grid of the same dimensions as colors
    pinit = 1.0 / float(len(colors)) / float(len(colors[0]))
    p = [[pinit for col in range(len(colors[0]))] for row in range(len(colors))]
    
    assert(len(motions) == len(measurements))
    for i in range(len(motions)):
        p = move(p, motions[i], p_move)
        p = sense(p, colors, measurements[i], sensor_right)
        
    return p

def show(p):
    rows = ['[' + ','.join(map(lambda x: '{0:.5f}'.format(x),r)) + ']' for r in p]
    print('[' + ',\n '.join(rows) + ']')


def sense(probability, colors, measurement, sensor_right):
    prob = [[0.0 for col in range(len(colors[0]))] for row in range(len(colors))]
    sum_prob = 0.0
    sensor_wrong = 1.0 - sensor_right
    for i in range(len(colors)):
        for j in range(len(colors[0])):
            hit = (measurement == colors[i][j])
            prob[i][j] = probability[i][j] * (hit * sensor_right + (1 - hit) * sensor_wrong)
            sum_prob += prob[i][j]
    for i in range(len(colors)):
        for j in range(len(colors[0])):
            prob[i][j] /= sum_prob
    return prob


def move(probability, motion, p_move):
    dy, dx = motion[0], motion[1]
    prob = [[0.0 for col in range(len(colors[0]))] for row in range(len(colors))]
    p_stay = 1.0 - p_move
    for i in range(len(colors)):
        for j in range(len(colors[0])):
            prob[i][j] = probability[i][j] * p_stay + probability[(i-dy)%len(colors)][(j-dx)%len(colors[0])] * p_move
    return prob


if __name__ == '__main__':
    #################################################################################
    #Test Case

    # # test 1
    # colors = [['G', 'G', 'G'],
    #           ['G', 'R', 'G'],
    #           ['G', 'G', 'G']]
    # measurements = ['R']
    # motions = [[0,0]]
    # sensor_right = 1.0
    # p_move = 1.0
    # p = localize(colors,measurements,motions,sensor_right,p_move)
    # correct_answer = (
    #     [[0.0, 0.0, 0.0],
    #      [0.0, 1.0, 0.0],
    #      [0.0, 0.0, 0.0]])
    # show(p)

    # # test 2
    # colors = [['G', 'G', 'G'],
    #           ['G', 'R', 'R'],
    #           ['G', 'G', 'G']]
    # measurements = ['R']
    # motions = [[0,0]]
    # sensor_right = 1.0
    # p_move = 1.0
    # p = localize(colors,measurements,motions,sensor_right,p_move)
    # correct_answer = (
    #     [[0.0, 0.0, 0.0],
    #      [0.0, 0.5, 0.5],
    #      [0.0, 0.0, 0.0]])
    # show(p)

    # # test 3
    # colors = [['G', 'G', 'G'],
    #           ['G', 'R', 'R'],
    #           ['G', 'G', 'G']]
    # measurements = ['R']
    # motions = [[0,0]]
    # sensor_right = 0.8
    # p_move = 1.0
    # p = localize(colors,measurements,motions,sensor_right,p_move)
    # correct_answer = (
    #     [[0.06666666666, 0.06666666666, 0.06666666666],
    #      [0.06666666666, 0.26666666666, 0.26666666666],
    #      [0.06666666666, 0.06666666666, 0.06666666666]])
    # show(p)

    # # test 4
    # colors = [['G', 'G', 'G'],
    #           ['G', 'R', 'R'],
    #           ['G', 'G', 'G']]
    # measurements = ['R', 'R']
    # motions = [[0,0], [0,1]]
    # sensor_right = 0.8
    # p_move = 1.0
    # p = localize(colors,measurements,motions,sensor_right,p_move)
    # correct_answer = (
    #     [[0.03333333333, 0.03333333333, 0.03333333333],
    #      [0.13333333333, 0.13333333333, 0.53333333333],
    #      [0.03333333333, 0.03333333333, 0.03333333333]])
    # show(p)

    # # test 5
    # colors = [['G', 'G', 'G'],
    #           ['G', 'R', 'R'],
    #           ['G', 'G', 'G']]
    # measurements = ['R', 'R']
    # motions = [[0,0], [0,1]]
    # sensor_right = 1.0
    # p_move = 1.0
    # p = localize(colors,measurements,motions,sensor_right,p_move)
    # correct_answer = (
    #     [[0.0, 0.0, 0.0],
    #      [0.0, 0.0, 1.0],
    #      [0.0, 0.0, 0.0]])
    # show(p)

    # # test 6
    # colors = [['G', 'G', 'G'],
    #           ['G', 'R', 'R'],
    #           ['G', 'G', 'G']]
    # measurements = ['R', 'R']
    # motions = [[0,0], [0,1]]
    # sensor_right = 0.8
    # p_move = 0.5
    # p = localize(colors,measurements,motions,sensor_right,p_move)
    # correct_answer = (
    #     [[0.0289855072, 0.0289855072, 0.0289855072],
    #      [0.0724637681, 0.2898550724, 0.4637681159],
    #      [0.0289855072, 0.0289855072, 0.0289855072]])
    # show(p)

    # # test 7
    # colors = [['G', 'G', 'G'],
    #           ['G', 'R', 'R'],
    #           ['G', 'G', 'G']]
    # measurements = ['R', 'R']
    # motions = [[0,0], [0,1]]
    # sensor_right = 1.0
    # p_move = 0.5
    # p = localize(colors,measurements,motions,sensor_right,p_move)
    # correct_answer = (
    #     [[0.0, 0.0, 0.0],
    #      [0.0, 0.33333333, 0.66666666],
    #      [0.0, 0.0, 0.0]])
    # show(p)
    #############################################################
    # For the following test case, your output should be 
    # [[0.01105, 0.02464, 0.06799, 0.04472, 0.02465],
    #  [0.00715, 0.01017, 0.08696, 0.07988, 0.00935],
    #  [0.00739, 0.00894, 0.11272, 0.35350, 0.04065],
    #  [0.00910, 0.00715, 0.01434, 0.04313, 0.03642]]
    # (within a tolerance of +/- 0.001 for each entry)
    colors = [['R','G','G','R','R'],['R','R','G','R','R'],['R','R','G','G','R'],['R','R','R','R','R']]
    measurements = ['G','G','G','G','G']
    motions = [[0,0],[0,1],[1,0],[1,0],[0,1]]
    p = localize(colors,measurements,motions,sensor_right = 0.7, p_move = 0.8)
    show(p) # displays your answer

