import matplotlib.pyplot as plt
import random
import numpy as np



cur = 0
n = 100
path = [0] * n

for i in range(n):
    path[i] = path[i - 1] + random.choice([1, -1])


# E[Xt] = 0, variance = t
# in the limit it becomes a gaussian because the
# values are the values of Pascal's triangle

plt.plot(path)
plt.show()