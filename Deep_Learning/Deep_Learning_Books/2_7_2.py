import numpy as np
import matplotlib.pyplot as plt

def func(x): return x**2

def dfunc(x): return 2*x

def GD(x_start, df, epochs, lr):
    xs = np.zeros(epochs+1)
    x = x_start
    xs[0] = x
    for i in range(epochs):
        dx = df(x)
        x += -dx * lr
        xs[i+1] = x
    return xs

x_start = 5
epocs   = 15
lr      = 0.3

w = GD(x_start, dfunc, epocs, lr=lr)
print(np.around(w,2))

color = 'r'

from numpy import arange
t = arange(-6.0, 6.0, 0.01)
plt.plot(t, func(t), c='b')
plt.plot(w, func(w), c=color, label='lr={}'.format(lr))
plt.scatter(w, func(w), c=color,)

plt.show()