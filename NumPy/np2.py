import numpy as np
arr11 = 5-np.arange(1,13).reshape(4,3)
print("array:",arr11)
print("-------------"*3)
print("\n")
# 所有元素的和
print("所有元素的和:",np.sum(arr11))
# 计算每一列的和
print("计算每一列的和:",np.sum(arr11,axis=0))
# 对每一个元素求累积和
print("对每一个元素求累积和:",np.cumsum(arr11))
# 对每一列求累积和
print("对每一列求累积和:",np.cumsum(arr11,axis=0))
# 计算每一行的累计积
print("计算每一行的累计积:",np.cumprod(arr11,axis=1))
# 计算所有元素的最小值
print("计算所有元素的最小值:",np.min(arr11))
# 计算每一列的最大值
print("计算每一列的最大值:",np.max(arr11,axis=0))
# 计算所有元素的均值
print("计算所有元素的均值:",np.mean(arr11))
# 计算每一行的均值
print("计算每一行的均值:",np.mean(arr11,axis=1))
# 计算所有元素的中位数
print("计算所有元素的中位数:",np.median(arr11))
# 计算每一列的中位数
print("计算每一列的中位数:",np.median(arr11,axis=0))
# 计算所有元素的方差
print("计算所有元素的方差:",np.var(arr11))
# 计算所有元素的方差，每一行的标准差
print("计算所有元素的方差，每一行的标准差:",np.std(arr11,axis=1))
