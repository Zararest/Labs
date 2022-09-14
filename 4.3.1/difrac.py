import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import sklearn
from sklearn.metrics import r2_score

data_x, data_y = np.loadtxt("/home/uwu/Labs/4.3.1/frenel.txt", usecols=(0, 1), unpack=True)

 
plt.grid(True)

plt.scatter(data_x, data_y, c='r', marker="+")

coef_data = np.polyfit(data_x, data_y, 1)

X_ = np.linspace(min(data_x) * 0.9, max(data_x) * 1.1, 300)
Y_ = coef_data[1] + coef_data[0] * X_

plt.title('Зависимость удвоенной координаты крайней зоны от n')   
plt.xlabel('Номер зоны')   
plt.ylabel('Удвоенная координата [мм]') 

bright_line = plt.plot(X_, Y_, 'r', linewidth=1)
plt.plot([1, 6], [275, 275], 'r', linewidth=1)

plt.show()

print("Отклонение", r2_score(data_y, coef_data[1] + coef_data[0]*data_x))
print("уравнение темных:", coef_data[1], "+", coef_data[0], "*x")