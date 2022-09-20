import sys
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
#Я НЕНАВИЖУ ПИТОН
#matplotlib ругается на тип, передаваемый в легенду
import warnings
#warnings.filterwarnings("ignore")
#Я НЕНАВИЖУ ПИТОН


def parse_file(file_name):
    data = np.array([])
    data = np.loadtxt(file_name, dtype=float)
    return data

def transform_data(data, functions):
    new_data = np.copy(data)
    for cur_func in functions:
        new_data = cur_func(np.copy(new_data))
    return new_data

#выходные данные: P [мм рт ст] | I [пкА]
def convert_P(data):
    room_P = 738
    new_data = np.copy(data)
    for i in range(len(data[:, 0])):
        new_data[i, 0] = room_P - data[i, 0]
    return new_data

def draw_line(data, legend):
    print(data)
    func = PlotFunction()
    func.set_left_bound_koef(1)
    func.set_arrayX(data[:, 0])
    func.set_arrayY(data[:, 1])
    func.set_legend(legend)
    koefs = func.fit_data(1)
    print('Уравнение:', legend, 'y =', koefs[0], '* x +', koefs[1])
    print('Погрешность:', func.calc_error(data))
    return func

def process_first_set(data):
    data = transform_data(data, [convert_P])

    func = PlotFunction()
    func.set_arrayX(data[:, 0])
    func.set_arrayY(data[:, 1])

    dots = PlotFunction()
    dots.set_arrayX(data[:, 0])
    dots.set_arrayY(data[:, 1])
    dots.set_legend('Экспериментальные данные')

    left_line = draw_line(data[0 : 23], 'Участок роста')
    right_line = draw_line(data[27 : ], 'Плато')

    plot = MyPlot()
    plot.config_plot('Зависимость тока от давления', 'P[мм.рт.ст]', 'I[пкА]')
    plot.add_dots(dots)
    plot.add_function(func)
    plot.add_function(left_line)
    plot.add_function(right_line)
    plot.draw_all()

def calc_dirivative(arrayX, arrayY):
    result = np.array([])
    for i in range(arrayX.size - 1):
        result = np.append(result, (arrayY[i + 1] - arrayY[i]) / (arrayX[i + 1] - arrayX[i]))
    return result

def process_second_set(data):
    data = transform_data(data, [convert_P])

    dots = PlotFunction()
    dots.set_arrayX(data[:, 0])
    dots.set_arrayY(data[:, 1])
    dots.set_legend('Экспериментальные данные')

    interpol = PlotFunction()
    interpol.set_arrayX(data[:, 0])
    interpol.set_arrayY(data[:, 1])
    interpol.set_left_bound_koef(-0.1)
    interpol.set_right_bound_koef(-0.1)
    interpol.fit_data(10)

    dirivative_data = calc_dirivative(np.copy(interpol.arrayX), np.copy(interpol.arrayY))
    dirivative_data = -150 * dirivative_data
    dirivative = PlotFunction()
    dirivative.set_arrayX(np.copy(interpol.arrayX)[1:][250 : 600])
    dirivative.set_arrayY(dirivative_data[250 : 600])
    dirivative.set_legend('Производная')

    extrapol = PlotFunction()
    extrapol.set_arrayX(data[4 : 20, 0])
    extrapol.set_arrayY(data[4 : 20, 1])
    extrapol.set_left_bound_koef(0.2)
    extrapol.set_right_bound_koef(0.2)
    extrapol.fit_data(1)
    extrapol.set_legend('Линейное придлиэение')

    plot = MyPlot()
    plot.config_plot('График зависимости N(P)', 'P[мм.рт.ст]', 'N')
    plot.add_dots(dots)
    plot.add_function(interpol)
    plot.add_function(dirivative)
    plot.add_function(extrapol)
    plot.draw_all()

def main():
    data_first = parse_file('First_data_set.txt')
    data_second = parse_file('Second_data_set.txt')

    process_first_set(data_first)
    process_second_set(data_second)
    MyPlot.show_all()

if __name__ == '__main__':
    main()