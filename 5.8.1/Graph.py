from Plot import MyPlot
from Plot import PlotFunction 

import numpy as np

def parse_file(file_name):
    data = np.array([])
    data = np.loadtxt(file_name, dtype=float)
    return data

def get_koefs():
    X_bright_T = np.array([900, 1900])
    Y_bright_T = np.array([910, 1980]) 
    koefs = np.polyfit(X_bright_T, Y_bright_T, 1)
    return koefs

#данные на выходе: T [K] | U [мВ] | I [A]
def convert_T(data):
    T_in_K_degrees = data[:, 0] + 273 
    koefs = get_koefs()
    new_T = np.polyval(koefs, T_in_K_degrees) #alternative data.T[0]
    converted_data = data
    converted_data[:, 0] = new_T
    return converted_data

#данные на выходе: T [K] | P [мВт]
def calc_P(data):
    converted_data = np.array([data[:, 0], data[:, 1] * data[:, 2]])
    converted_data = converted_data.T
    return converted_data

def sort_X(data):
    #new_data = np.transpose(data)
    new_data = data
    new_data = np.sort(data, 0)
    return new_data

def swap_columns(data, first_col, second_col):
    data[:, [first_col, second_col]] = data[:, [second_col, first_col]] #из-за [] выражение аналогично x, y = y, x

#применяет функции к данным
def transform_data(data, functions):
    new_data = data
    for cur_func in functions:
        new_data = cur_func(new_data)
    return new_data

#данные на входе: T_ярк[С] | U[мВ] | I[A]
def main():
    data = parse_file('Data.txt')
    data = transform_data(data, [convert_T, calc_P, sort_X])
    func = PlotFunction()
    func.set_arrayX(data[:, 0])
    func.set_arrayY(data[:, 1])
    func.transformX(np.log)
    func.transformY(np.log)
    func.set_legend('Экспериментальные данные')
    plot = MyPlot()
    plot.config_plot('ln(W) = ln(f(T))', 'T[C] в лог масштабе', 'W[мВ] в лог масштабе')
    plot.add_dots(func)
    plot.draw_all()
    MyPlot.show_all()

if __name__ == '__main__':
    main()
