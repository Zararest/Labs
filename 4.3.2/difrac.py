import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import sklearn
from sklearn.metrics import r2_score

data_x_1, data_y_1 = np.loadtxt("/home/uwu/Labs/4.3.2/data_1.txt", usecols=(0, 1), unpack=True)
data_x_2, data_y_2 = np.loadtxt("/home/uwu/Labs/4.3.2/data_2.txt", usecols=(0, 1), unpack=True)
data_x_3, data_y_3 = np.loadtxt("/home/uwu/Labs/4.3.2/data_3.txt", usecols=(0, 1), unpack=True)
data_x_4, data_y_4 = np.loadtxt("/home/uwu/Labs/4.3.2/data_4.txt", usecols=(0, 1), unpack=True)

plt.grid(True)
plt.title('Зависимость периода решетки от размера щели')   
plt.xlabel('1 / D [мм]')   
plt.ylabel('Период решетки [мк м]') 

plt.scatter(data_x_1, data_y_1, c='r', marker="1")
plt.scatter(data_x_2, data_y_2, c='g', marker="+")
plt.scatter(data_x_3, data_y_3, c='b', marker="v")
plt.scatter(data_x_4, data_y_4, c='y', marker=".")

coef_data_1 = np.polyfit(data_x_1, data_y_1, 1)
coef_data_2 = np.polyfit(data_x_2, data_y_2, 1)
coef_data_3 = np.polyfit(data_x_3, data_y_3, 1)
coef_data_4 = np.polyfit(data_x_4, data_y_4, 1)

X_1 = np.linspace(-5, 4, 300)
Y_1 = coef_data_1[1] + coef_data_1[0] * X_1

X_2 = np.linspace(-5, 4, 300)
Y_2 = coef_data_2[1] + coef_data_2[0] * X_2

X_3 = np.linspace(-5, 4, 300)
Y_3 = coef_data_3[1] + coef_data_3[0] * X_3

X_4 = np.linspace(-5, 4, 300)
Y_4 = coef_data_4[1] + coef_data_4[0] * X_4

plt.title('Зависимость координат светлых полос от номера m')   
plt.xlabel('номер полосы m')   
plt.ylabel('Координата светлой полосы ') 

bright_line = plt.plot(X_1, Y_1, 'r--', linewidth=1)
bright_line = plt.plot(X_2, Y_2, 'g-.', linewidth=1)
bright_line = plt.plot(X_3, Y_3, 'b:', linewidth=1)
bright_line = plt.plot(X_4, Y_4, 'y', linewidth=1)
plt.show()

print("уравнение красных(2.55MHZ):", coef_data_1[1], "+", coef_data_1[0], "*x", "отклонение ", r2_score(data_y_1, coef_data_1[1] + coef_data_1[0]*data_x_1))
print("уравнение зеленых(1.43MHZ):", coef_data_2[1], "+", coef_data_2[0], "*x", "отклонение ", r2_score(data_y_2, coef_data_2[1] + coef_data_2[0]*data_x_2))
print("уравнение синих(5.88MHZ):", coef_data_3[1], "+", coef_data_3[0], "*x", "отклонение ", r2_score(data_y_3, coef_data_3[1] + coef_data_3[0]*data_x_3))
print("уравнение желтых(3.17MHZ):", coef_data_4[1], "+", coef_data_4[0], "*x", "отклонение ", r2_score(data_y_4, coef_data_4[1] + coef_data_4[0]*data_x_4))