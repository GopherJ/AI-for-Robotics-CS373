# Modify the empty list, p, so that it becomes a UNIFORM probability
# distribution over five grid cells, as expressed in a list of
# five probabilities.

p = []
for i in range(5):
    p.append(1.0/5)
print(p)
