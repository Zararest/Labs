import numpy as np
import matplotlib
import matplotlib.pyplot as plt

y = np.array([1, 2, -6, 0])
x = np.array([-1, -2, -3, -4])

lines = plt.plot(x, y)
print(lines)
plt.setp(lines, linestyle='-.')
plt.show()