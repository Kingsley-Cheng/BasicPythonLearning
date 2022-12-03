import numpy as np
from scipy import integrate


def func1(x):
    return (np.cos(np.exp(x))) ** 2


def func2(x, y):
    return 16 * x * y


result1 = integrate.quad(func1, 0, 3)
result2 = integrate.dblquad(func2, 0, 0.5, 0, lambda y: np.sqrt(1 - 4 * y ** 2))
print(result1)
print(result2)
