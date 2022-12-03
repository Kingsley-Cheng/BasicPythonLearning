import numpy as np
# 给定的数字
c = 7.1
Z = np.array([[0,1,2,3],[4,5,6,7]])
indx = np.argmin(np.abs(Z-c))
num = np.ravel(Z)[indx]
print(num)