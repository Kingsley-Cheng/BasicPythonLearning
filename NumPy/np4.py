import numpy as np

Z = np.random.random((5,5))
range = np.max(Z) - np.min(Z)
Z1 = np.divide(Z-np.min(Z),np.max(Z))
print(Z1)