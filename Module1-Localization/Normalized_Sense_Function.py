# Modify your code so that it normalizes the output for
# the function sense. This means that the entries in q
# should sum to one.


p = [0.2, 0.2, 0.2, 0.2, 0.2]
world = ['green', 'red', 'red', 'green', 'green']
Z = 'red'
pHit = 0.6
pMiss = 0.2


def sense(p, Z):
    q = []
    for i in range(len(p)):
        hit = (Z == world[i])
        q.append(p[i] * (hit * pHit + (1 - hit) * pMiss))
    sum_q = sum(q)
    for i in range(len(q)):
        q[i] /= sum_q
    return q


print(sense(p, Z))

