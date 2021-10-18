
import matplotlib.pyplot as plt
import numpy as np
import math
import findzero

def func(x):
    return x**3 - 1

print(findzero(func,0.,2.,0.0001))

x = np.linspace(0,2,100)
y = func(x)
plt.plot(x,y)
plt.show()
