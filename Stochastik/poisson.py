import numpy as np
import matplotlib.pyplot as plt


def poisson_dist(l, k):
    return np.exp(-l) * np.math.pow(l, k) / np.math.factorial(k)


x = [x for x in range(0, 150)]
y1 = [poisson_dist(10, k) for k in x]
y2 = [poisson_dist(50, k) for k in x]
y3 = [poisson_dist(70, k) for k in x]
y4 = [poisson_dist(80, k) for k in x]
y5 = [poisson_dist(90, k) for k in x]
y6 = [poisson_dist(100, k) for k in x]
y7 = [poisson_dist(30, k) for k in x]

plt.plot(x, y1)
plt.plot(x, y2)
plt.plot(x, y3)
plt.plot(x, y4)
plt.plot(x, y5)
plt.plot(x, y6)
plt.plot(x, y7)

plt.show()
