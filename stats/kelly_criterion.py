import matplotlib.pyplot as plt
import random

p = 0.6 # probability of winning
q = 1 - p
a = 1.0 # proportion lost on a negative outcome
b = 1.0 # proportion gained on a positive outcome
n = 2000
f = p / a - q / b
print(f)

wealth = [1] * n
for i in range(1, n):
    wealth[i] = wealth[i - 1] * (1 + f * (b if random.random() < p else -a))

plt.figure(1)
plt.subplot(211)
plt.title('Wealth')
plt.plot(wealth)
plt.subplot(212)
plt.plot(wealth)
plt.yscale('log')
plt.show()