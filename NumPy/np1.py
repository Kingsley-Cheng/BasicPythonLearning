from time import perf_counter

import numpy as np

x = np.linspace(0, 2, 1000)


# Method 1
def triangle_wave(x, c, c0, hc):
    x = x - int(x)  # 三角波的周期为1，因此只取x坐标的小数部分进行计算
    if x >= c:
        r = 0.0
    elif x < c0:
        r = x / c0 * hc
    else:
        r = (c - x) / (c - c0) * hc
    return r


start = perf_counter()
y1 = np.array([triangle_wave(t, 0.6, 0.4, 1.0) for t in x])
time1 = perf_counter()
# Method 2
triangle_ufunc1 = np.frompyfunc(triangle_wave, 4, 1)
y2 = triangle_ufunc1(x, 0.6, 0.4, 1.0)
y2 = y2.astype(np.float)
time2 = perf_counter()
# Method 3
triangle_ufunc2 = np.frompyfunc(lambda x: triangle_wave(x, 0.6, 0.4, 1.0), 1, 1)
y3 = triangle_ufunc2(x)
y3 = y3.astype(np.float)
time3 = perf_counter()
# Method 4
triangle_ufunc3 = np.vectorize(triangle_wave, otypes=[np.float])
y4 = triangle_ufunc3(x, 0.6, 0.4, 1.0)
time4 = perf_counter()

print("y1与y2:", np.all(y1 == y2))
print("y2与y3:", np.all(y2 == y3))
print("y3与y4:", np.all(y3 == y4))
print("time of y1:", time1 - start)
print("time of y2:", time2 - time1)
print("time of y3:", time3 - time2)
print("time of y4:", time4 - time3)
