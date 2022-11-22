from hashlib import new
from sqlite3 import converters
import sys
from sysconfig import parse_config_h
sys.path.insert(0,"../")
#Я НЕНАВИЖУ ПИТОН
#Я НЕНАВИЖУ ПИТОН
#Я НЕНАВИЖУ ПИТОН
#Я НЕНАВИЖУ ПИТОН
#Я НЕНАВИЖУ ПИТОН
#Я НЕНАВИЖУ ПИТОН
from Plot import MyPlot
from Plot import PlotFunction
#Я НЕНАВИЖУ ПИТОН
import numpy as np
import math

#--------------------- Повторные функции
def parse_file(file_name):
  data = np.array([])
  data = np.loadtxt(file_name, dtype=float)
  return data

def calc_cos(X):
  return 1 - np.cos(math.radians(X))

def convert_N(Y):
  return 1 / Y

def draw_graph(data):
  func = PlotFunction()
  func.set_arrayX(data[:, 0])
  func.set_arrayY(data[:, 1])
  func.transformX(calc_cos)
  func.transformY(convert_N)
  koefs = func.fit_data(1)
  print('Уравнение:', 'N(1 - cos())', 'y =', koefs[0], '* x +', koefs[1])
  print('Ближайшее значения для 0:', func.get_nearest_val(calc_cos(0)), 'и 90:', func.get_nearest_val(calc_cos(90)))

  dots = PlotFunction()
  dots.set_arrayX(data[:, 0])
  dots.set_arrayY(data[:, 1])
  dots.transformX(calc_cos)
  dots.transformY(convert_N)

  plot = MyPlot()
  plot.config_plot('Зависимость номера канала от угла рассеяния', '1 - cos(x)', '1/N')
  plot.add_function(func)
  plot.add_dots(dots)
  plot.draw_all()

def main():
  data = parse_file('data.txt')

  draw_graph(data)
  MyPlot.show_all()

if __name__ == '__main__':
  main()