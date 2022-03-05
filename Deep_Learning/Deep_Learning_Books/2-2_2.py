####2-2.2. 方向(direction): 使用tan-1()函數計算

import math
import numpy as np

#向量(Vector)
v = np.array([2,1])

vTan = v[1]/v[0]
print('tan (theta) = 1/2')

theta = math.atan(vTan)
print('長度(radian) = ', round(theta,4))
print('角度(degree) = ', round(theta*180/math.pi,2))

#也可以用math.degree() 轉換角度
print('角度(degree) = ', round(math.degrees(theta),2))
