import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt


def func(x):
    return x ** 2 + 10 * np.sin(x)


# fmin_bfgs 方法
y_bfgs = optimize.fmin_bfgs(func, [-1])
print(y_bfgs, func(y_bfgs))
# optimize.fminbound 方法
y_minbound = optimize.fminbound(func, -10, 10)
print(y_minbound, func(y_minbound))
# optimize.brute 方法
y_brute = optimize.brute(func, (slice(-10, 10, 0.01),))
print(y_brute, func(y_brute))
x = np.arange(-10, 10, 0.1)
y = func(x)
plt.plot(x, y)
plt.plot(x, func(y_bfgs) * np.ones(x.shape))
plt.show()
