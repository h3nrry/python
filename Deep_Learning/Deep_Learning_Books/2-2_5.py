#### 2-2.5向量加減: 乘除一個常數, 長度, 方向均改變

import math
from matplotlib import scale
import numpy as np
import matplotlib.pyplot as plt

#向量(Vector) + 
v  = np.array([2,1])
v1 = np.array([2,1]) * 2
v2 = np.array([2,1]) / 2

#原點 
origin = [0], [0]

#量有箭頭的線
plt.quiver(*origin, *v1, scale=10, color='r')
plt.quiver(*origin, *v,  scale=10, color='g')
plt.quiver(*origin, *v2, scale=10, color='b')

plt.annotate('origin vector', (0.025, 0.008), xycoords='data', color='b', fontsize=16)

#作圖
plt.axis('equal')
plt.grid()

plt.xticks(np.arange(-0.05, 0.06, 0.01), labels=np.arange(-5, 6, 1))
plt.yticks(np.arange(-3, 5, 1)/100,      labels=np.arange(-3, 5, 1))

plt.show()