import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import sklearn
from sklearn.metrics import r2_score

data_x, data_y = np.loadtxt("/home/uwu/Labs/4.7.2/data.txt", usecols=(0, 1), unpack=True)

data_y = data_y * data_y

plt.grid(True)

plt.scatter(data_x, data_y, c='r')

coef_data = np.polyfit(data_x, data_y, 1)

plt.title('Зависимость r^2 от номера кольца')   
plt.xlabel('Номер кольца')   
plt.ylabel('Квадрат радиуса [мм^2]') 

bright_line = plt.plot(data_x, coef_data[1] + coef_data[0]*data_x, 'r')

plt.show()

print("Отклонение", r2_score(data_y, coef_data[1] + coef_data[0]*data_x))
print("уравнение темных:", coef_data[1], "+", coef_data[0], "*x")