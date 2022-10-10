import numpy as np
import matplotlib.pyplot as plt


def hy_ge(N, K, n, k):
    return np.random.binomial(K, k) * np.random.binomial(N - K,
                                                         n - k) / np.random.binomial(
        N, n)

N = 10
K = 5

x = [n for n in range(1,N)]

y1 = [hy_ge(N,K,n,2) for n in x]

plt.plot(x,y1)
plt.show()