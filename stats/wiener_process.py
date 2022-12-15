import matplotlib.pyplot as plt
import random
import numpy as np


n = 1000
x = [1.0] * n
mu = -0.02
stdev = 1.0
t_int = 10

for i in range(1, n):
    x[i] = x[i - 1] * (mu + np.exp(np.random.randn()) * stdev)

plt.subplot(211)
plt.plot(x)
plt.subplot(212)
plt.yscale('log')
plt.plot(x)
plt.show()