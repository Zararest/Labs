from Plot import MyPlot
from Plot import PlotFunction 

import numpy as np

#matplotlib ругается на тип, передаваемый в легенду
import warnings
warnings.filterwarnings("ignore")

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

#Подается в Кельвинах
def get_epsilon(cur_T):
    epsilon_arr_T = np.array([800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000])
    epsilon_arr = np.array([0.067, 0.081, 0.105, 0.119, 0.133, 0.144, 0.164, 0.179, 0.195, 0.209, 0.223, 0.236, 0.249])
    tmp_func = PlotFunction()
    tmp_func.set_arrayX(epsilon_arr_T)
    tmp_func.set_arrayY(epsilon_arr)
    tmp_func.fit_data(5)
    return tmp_func.get_nearest_val(cur_T)

#Умножает температуру на константы и возводит в степень
#Данные на входе: T [K] | P [мВт]
#Данные на выходе: T [K] | P [мВт] / const * T^4 {sigma}
def mult_and_divide_T(data):
    const_S = 0.000036 #площадь нити в м^2
    new_data = np.copy(data)
    for i in range(data[:, 0].size):
        new_data[i, 0] = np.power(data[i, 0], 4) * const_S * get_epsilon(data[i, 0]) 
    for i in range(data[:, 0].size):
        new_data[i, 1] = new_data[i, 1] / new_data[i, 0]
        new_data[i, 0] = data[i, 0]
    return new_data

def calc_h(data):
    new_data = np.copy(data)
    K_b = 1.38 * (10**(-23))
    C_const = 3 * (10**8)
    for i in range(data[:, 0].size):
        new_data[i, 1] = ((2 * (np.pi**5) * (K_b**4)) / (15 * (C_const**2) * new_data[i, 1]))**(1/3)
    return new_data

def convert_P(data):
    new_data = np.copy(data)
    for i in range(data[:, 0].size):
        new_data[i, 1] = new_data[i, 1] * 0.001
    return new_data

def swap_columns(data, first_col, second_col):
    data[:, [first_col, second_col]] = data[:, [second_col, first_col]] #из-за [] выражение аналогично x, y = y, x

#применяет функции к данным
def transform_data(data, functions):
    new_data = data
    for cur_func in functions:
        new_data = cur_func(np.copy(new_data))
    return new_data

#Графики для подсчета постоянной Больцмана
# На графике построить отношение мощности к T^4 * коэф 
def draw_constant(data):
    data = transform_data(data, [convert_T, calc_P, sort_X, mult_and_divide_T, convert_P, calc_h])

    func = PlotFunction()
    func.set_arrayX(data[:, 0])
    func.set_arrayY(data[:, 1])
    func.set_legend('Зависимость постоянной Боьцмана от T')

    dots = PlotFunction()
    dots.set_arrayX(data[:, 0])
    dots.set_arrayY(data[:, 1])
    dots.set_legend('Экспериментальные данные')

    plot = MyPlot()
    plot.config_plot('Анализ постоянной Планка', 'T[K]', 'h[Дж*с]')
    plot.add_function(func)
    plot.add_dots(dots)
    plot.draw_all()



def draw_W_from_T(data):
    data = transform_data(data, [convert_T, calc_P, sort_X])

    func = PlotFunction()
    func.set_arrayX(data[:, 0])
    func.set_arrayY(data[:, 1])
    func.transformX(np.log)
    func.transformY(np.log)
    func.set_legend('Экспериментальные данные')

    approx_func = PlotFunction()
    approx_func.set_arrayX(data[:, 0])
    approx_func.set_arrayY(data[:, 1])
    approx_func.transformX(np.log)
    approx_func.transformY(np.log)
    koefs = approx_func.fit_data(1)
    approx_func.set_legend('Линейное приближение')

    print('График мощности от температуры')
    print('y = ', koefs[0], '* x +', koefs[1])

    log_data = data
    for i in range(data[:, 0].size):
        log_data[i, 0] = np.log(data[i, 0])
        log_data[i, 1] = np.log(data[i, 1])
        
    print('Погрешность:', approx_func.calc_error(log_data))

    plot = MyPlot()
    plot.config_plot('ln(W) = ln(f(T))', 'T[K] в лог масштабе', 'W[мВ] в лог масштабе')
    plot.add_dots(func)
    plot.add_function(approx_func)
    plot.draw_all()

#данные на входе: T_ярк[С] | U[мВ] | I[A]
def main():
    data = parse_file('Data.txt')
    first_data = data
    second_data = data
    draw_W_from_T(first_data)
    draw_constant(second_data)

    #MyPlot.save_all()
    MyPlot.show_all()
    

if __name__ == '__main__':
    main()
