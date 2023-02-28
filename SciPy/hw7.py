from scipy import stats
import numpy as np
import matplotlib.pyplot as plt

X = stats.gamma(1)
x0 = X.rvs(size=1000)
t = np.arange(0, 9, 0.01)

plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
plt.rcParams['axes.unicode_minus'] = False
fig, ax = plt.subplots(1, 1)
ax.plot(t, X.pdf(t))
p, t2 = np.histogram(x0, bins=100, normed=True)
t2 = (t2[:-1] + t2[1:]) / 2
ax.plot(t2, p)
ax.legend(["Gamma 分布的概率密度", "对生成的随机数进行直方图统计的结果"])
plt.show()
