import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt


def func(x, p):
    """
    数据拟合所用的函数: y=a*np.exp(-(x-b)**2/(2*c**2))
    """
    a, b, c = p
    return a * np.exp(-(x - b) ** 2 / (2 * c ** 2))


def residuals(p, y, x):
    """
    实验数据x, y和拟合函数之间的差，p为拟合需要找到的系数
    """
    return y - func(x, p)


def func2(x, a, b, c):
    return a * np.exp(-(x - b) ** 2 / (2 * c ** 2))


x = np.linspace(0, 10, 100)
a, b, c = 1, 5, 2
y0 = func(x, [a, b, c])
np.random.seed(10)
y1 = y0 + 2 * np.random.randn(len(x))
p0 = [1, 1, 1]

# 使用curve_fit
popt, pcov = optimize.curve_fit(func2, x, y1, p0=p0)
print("真实参数:", [a, b, c])
print("拟合参数", popt)

# 使用leastsq
plsq = optimize.leastsq(residuals, p0, args=(y1, x))
print("真实参数:", [a, b, c])
print("拟合参数:", plsq[0])  # 实验数据拟合后的参数

plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
plt.rcParams['axes.unicode_minus'] = False

fig, ax = plt.subplots(1, 2)
ax[0].plot(x, y0)
ax[0].plot(x, y1, "o")
ax[0].plot(x, func(x, plsq[0]))
ax[0].legend(["真实数据", "带噪声的实验数据", "leastsq 拟合数据"])
ax[1].plot(x, y0)
ax[1].plot(x, y1, "o")
ax[1].plot(x, func(x, popt))
ax[1].legend(["真实数据", "带噪声的实验数据", "curve_fit 拟合数据"])
plt.show()
