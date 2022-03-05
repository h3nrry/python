####2.2.1. 長度(magnitude) : 計算公式歐幾里得距離(Euclidean distance) 
import math
import numpy as np

#向量(Vector)
v = np.array([2,1])
print(v)

#向量長度 (magnitude)計算
(v[0]**2 + v[1]**2)**(1/2)

#使用np.linalg.norm()計算向量長度(magnitude)
magnitude = np.linalg.norm(v)
print(magnitude)

