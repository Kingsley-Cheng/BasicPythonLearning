import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt
x = [-1, 0, 2.0, 1.0]
y = [1.0, 0.3, -0.5, 0.8]
x_inter = np.linspace(-3, 4, 100)
newfunc1 = interpolate.Rbf(x,y,function="multiquadric")
y_multi = newfunc1(x_inter)

newfunc2 = interpolate.Rbf(x, y, function='gaussian')
y_gaussian = newfunc2(x_inter)

newfunc3 = interpolate.Rbf(x, y, function='linear')
y_linear = newfunc3(x_inter)

plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
plt.rcParams['axes.unicode_minus'] = False

fig, ax = plt.subplots(1,3,figsize=(15,10))
ax[0].plot(x_inter,y_multi)
ax[0].plot(x,y,'o')
ax[0].legend(['Multiquadric', '真实数据'])
ax[1].plot(x_inter,y_gaussian)
ax[1].plot(x,y,'o')
ax[1].legend(['Gaussian', '真实数据'])
ax[2].plot(x_inter,y_linear)
ax[2].plot(x,y,'o')
ax[2].legend(['Linear', '真实数据'])
plt.show()

