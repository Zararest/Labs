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

#--------------------- Повторные функции
def parse_file(file_name):
    data = np.array([])
    data = np.loadtxt(file_name, dtype=float)
    return data

def transform_data(data, functions):
    new_data = np.copy(data)
    for cur_func in functions:
        new_data = cur_func(np.copy(new_data))
    return new_data
#----------------------

def calc_per_sec(data):
    new_data = np.copy(data[:, 0 : 2])
    zero_level = 12                         #часитиц в секунду при закрытой заглушке
    for i in range(len(data[:, 0])):
        new_data[i, 1] = data[i, 1] / data[i, 2] - zero_level
    return new_data

def calc_log(data):
    N_0 = 11990.9
    new_data = np.copy(data)
    for i in range(len(data[:, 0])):
        new_data[i, 1] = np.log(N_0 / data[i, 1])
    return new_data

def draw_graph(data_set):
    converted_data_set = []
    functions = [calc_per_sec, calc_log]
    for it in data_set:
        converted_data_set.append(transform_data(it, functions))

    converted_data_set[0][:, 0] = converted_data_set[0][:, 0] * 20 #толщина в мм Al
    converted_data_set[1][:, 0] = converted_data_set[1][:, 0] * 10 #толщина в мм Fe
    converted_data_set[2][:, 0] = converted_data_set[2][:, 0] * 4.3#толщина в мм Pb

    functions_set = []
    dots_set = []
    legends_set = ['Al', 'Fe', 'Pb']
    for i in range(len(converted_data_set)):
        func = PlotFunction()
        func.set_arrayX(converted_data_set[i][:, 0])
        func.set_arrayY(converted_data_set[i][:, 1])
        func.set_legend(legends_set[i])
        koefs = func.fit_data(1)
        print('Уравнение:', legends_set[i], 'y =', koefs[0], '* x +', koefs[1])
        print('Погрешность:', func.calc_error(converted_data_set[i]))
        functions_set.append(func)

        dots = PlotFunction()
        dots.set_arrayX(converted_data_set[i][:, 0])
        dots.set_arrayY(converted_data_set[i][:, 1])
        dots_set.append(dots)

    plot = MyPlot()
    plot.config_plot('Зависимость ослабления потока гамма квантов от толщины материала', 'l [мм]', 'ln N_0 / N')
    for i in range(len(functions_set)):
        plot.add_function(functions_set[i])
        plot.add_dots(dots_set[i])
    plot.draw_all()


def main():
    Al_data = parse_file('Al.txt')
    Fe_data = parse_file('Fe.txt')
    Pb_data = parse_file('Pb.txt')

    draw_graph([Al_data, Fe_data, Pb_data])
    MyPlot.show_all()

if __name__ == '__main__':
    main()
