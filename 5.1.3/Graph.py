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

def draw_graph(data):
  func_V1 = PlotFunction()
  func_V1.set_arrayX(data[:, 1])
  func_V1.set_arrayY(data[:, 0])
  func_V1.set_legend('V1 = 2.98 B')

  func_V2 = PlotFunction()
  func_V2.set_arrayX(data[:, 3])
  func_V2.set_arrayY(data[:, 2])
  func_V1.set_legend('V2 = 2.6 B')

  dots_V1 = PlotFunction()
  dots_V1.set_arrayX(data[:, 1])
  dots_V1.set_arrayY(data[:, 0])
  
  dots_V2 = PlotFunction()
  dots_V2.set_arrayX(data[:, 3])
  dots_V2.set_arrayY(data[:, 2])
  
  plot = MyPlot()
  plot.config_plot('Зависимость тока через газ от напряжения', 'E [B]', 'I * R [B]')
  plot.add_function(func_V1)
  plot.add_function(func_V2)
  plot.add_dots(dots_V1)
  plot.add_dots(dots_V2)
  plot.draw_all()

def neg_log(X):
  return -np.log(X / 10000)

def draw_prob(data):
  func = PlotFunction()
  func.set_arrayX(data[:, 1])
  func.set_arrayY(data[:, 0])
  func.transformY(neg_log)

  dots = PlotFunction()
  dots.set_arrayX(data[:, 1])
  dots.set_arrayY(data[:, 0])
  dots.transformY(neg_log)

  plot = MyPlot()
  plot.config_plot('Зависимоть вероятности рассеяния от напряжения', 'E', 'w ~ -ln(I)')
  plot.add_function(func)
  plot.add_dots(dots)
  plot.draw_all()

def main():
  data = parse_file('data.txt')

  draw_graph(data)
  draw_prob(data)
  MyPlot.show_all()

if __name__ == '__main__':
  main()