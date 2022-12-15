import matplotlib.pyplot as plt
import random
import numpy as np


time = 100
n = 50

data = [[0.5] * n]







start = 1
trials = 1000
paths = 50
a = [start] * paths
n = 2
increment = 1
frac = [[a[0] / n] * trials for i in range(paths)]



for i in range(1, trials):
    for j in range(paths):
        if random.random() < frac[j][i - 1]:
            a[j] += increment
        frac[j][i] = a[j] / (n + increment * i)

for f in frac:
    plt.plot(f)
plt.title(f'{paths} realizations of Polya\'s urn\nStarting conditions: {start} out of {n}')
plt.ylabel('Proportion of marbles')
plt.show()