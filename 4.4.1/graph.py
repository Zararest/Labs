import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import sklearn
from sklearn.metrics import r2_score

data_x, data_y = np.loadtxt("/home/uwu/Labs/4.4.1/data.txt", usecols=(0, 1), unpack=True)

plt.grid(True)

plt.scatter(data_x, data_y, c='r', marker="+")

coef_data = np.polyfit(data_x, data_y, 1)

plt.title('Зависимость sin(f) от длины волны')   
plt.xlabel('Длина волны [н.м]')   
plt.ylabel('Синусс угла отклонения') 

bright_line = plt.plot(data_x, coef_data[1] + coef_data[0]*data_x, 'r', linewidth=1)

plt.show()

print("Отклонение", r2_score(data_y, coef_data[1] + coef_data[0]*data_x))
print("уравнение:", coef_data[1], "+", coef_data[0], "*x")