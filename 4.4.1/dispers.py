import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import sklearn
from sklearn.metrics import r2_score

data_x, data_y = np.loadtxt("/home/uwu/Labs/4.4.1/dispers.txt", usecols=(0, 1), unpack=True)

data_y = data_y * 0.5

plt.grid(True)

plt.scatter(data_x, data_y, c='r', marker="+")

d = 2.001
lambda_ = 0.577

X_ = np.linspace(min(data_x) * 1.1, max(data_x) * 1.1, 300)
Y_ = X_ / np.sqrt(d * d - X_ * X_ * lambda_ * lambda_)

plt.title('Зависимость D*10^-6 от длины волны')   
plt.xlabel('Порядок максимума')   
plt.ylabel('Угловая дисперсия') 

bright_line = plt.plot(X_, Y_, 'r', linewidth=1)

plt.show()