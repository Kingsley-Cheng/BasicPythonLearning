import numpy as np

# 输入系数矩阵
A = np.array([[3, 6, -5], [1, -3, 2], [5, -1, 4]])
# 输入方程组的向量
b = np.array([12, -2, 10])
y = np.linalg.solve(A, b)
print(y)
