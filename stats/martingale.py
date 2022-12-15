import matplotlib.pyplot as plt
import random
import numpy as np



cur = 0
n = 10
path = [0] * n
wealth = [0] * n

p = 0.01

for i in range(1, n):
    path[i] = path[i - 1] + (1 if (random.random() < p) else -1)
    # Y_t = X_t^2 - t
    wealth[i] = ((1 - p) / p) ** path[i]



# E[Xt] = 0, variance = t
# in the limit it becomes a gaussian because the
# values are the values of Pascal's triangle

# plt.plot(path)
plt.plot(wealth)
plt.show()