from scipy.optimize import fsolve
from math import cos, sin

d, L = 140, 156


def f(x):
    x0, x1 = x.tolist()  # x0 表示 a，x1 表示 r
    return [cos(x0) - 1 + d ** 2 / (2 * x1 ** 2), L - x0 * x1]


result1 = fsolve(f, [1, 1])
print(result1)
print(f(result1))


# 下面引入雅可比矩阵
def j(x):
    x0, x1 = x.tolist()
    return [[sin(x0), -19600 / (x1 ** 3)], [-x1, -x0]]


result2 = fsolve(f, [1, 1], fprime=j)
print(result2)
print(f(result2))
