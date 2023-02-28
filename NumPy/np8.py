import numpy as np
import pandas as pd

data = pd.read_csv("height.csv")
dt = np.array(data, dtype="int64")
age = np.bincount(dt[:, 0])
height = np.bincount(dt[:, 1])

age_dict = {}
height_dict ={}
for i in range(len(age)):
    if age[i] != 0:
        age_dict[f"{i+1}"] = age[i]

for i in range(len(height)):
    if height[i] != 0:
        height_dict[f"{i+1}"] = height[i]

print("年龄统计结果：\n", age_dict)
print("身高统计结果：\n", height_dict)