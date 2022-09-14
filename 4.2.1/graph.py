import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import sklearn
from sklearn.metrics import r2_score

bright_x, bright_y = np.loadtxt("/home/uwu/Labs/4.2.1/bright.txt", usecols=(0, 1), unpack=True)
dark_x, dark_y = np.loadtxt("/home/uwu/Labs/4.2.1/dark.txt", usecols=(0, 1), unpack=True)

bright_y = bright_y * bright_y
dark_y = dark_y * dark_y

plt.grid(True)

plt.scatter(bright_x, bright_y, c='r')
plt.scatter(dark_x, dark_y, c='g')

coef_bright = np.polyfit(bright_x, bright_y, 1)
coef_dark = np.polyfit(dark_x, dark_y, 1)

plt.title('Зависимость r^2 от номера кольца')   
plt.xlabel('Номер кольца')   
plt.ylabel('Квадрат радиуса [мм^2]') 

x_data = bright_x
y_data = coef_bright[1] + coef_bright[0]*bright_x
bright_line = plt.plot(x_data, y_data, 'r', label='Светлые кольца')

x_data = dark_x
y_data = coef_dark[1] + coef_dark[0]*dark_x
dark_line = plt.plot(x_data, y_data, 'g', label='Темные кольца')

plt.legend()
plt.show()



print("Отклонение для темных", r2_score(dark_y, coef_dark[1] + coef_dark[0]*dark_x))
print("Отклонение для светлых", r2_score(bright_y, coef_bright[1] + coef_bright[0]*bright_x))
print("уравнение темных:", coef_dark[1], "+", coef_dark[0], "*x")
print("уравнение светлых:", coef_bright[1], "+", coef_bright[0], "*x")

