import numpy as np
# 生成 1-5 的数组
array1 = np.arange(1, 6)
# 生成需要插入的 0 数组
array2 = np.zeros(5)
# 先将 0 数组堆叠到 1-5 数组下面，在进行维度变换，之后在展平
array3 = np.ravel(np.vstack((array1,array2)).swapaxes(0,1))
print(array3)