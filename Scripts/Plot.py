#!usr/bin/python3

import numpy as np             
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from sklearn.metrics import r2_score

class PlotFunction:

    #dpi - dots per interval
    def __init__(self):
        self.__arrayX = np.array([])
        self.__arrayY = np.array([])
        self.__config_line = '--'
        self.__legend = ''
        self.__line_dpi = 1000    
        self.__bounds_koefs = [0.2, 0.2]           

    #getters
    @property
    def left_bound_koef(self):
        return self.__bounds_koefs[0]

    @property
    def right_bound_koef(self):
        return self.__bounds_koefs[1]

    @property                               
    def config_line(self):
        return self.__config_line

    @property                               
    def arrayX(self):
        return self.__arrayX

    @property
    def arrayY(self):
        return self.__arrayY

    @property
    def line_dpi(self):
        return self.__line_dpi

    @property
    def legend(self):
        return self.__legend

    #setters
    def set_left_bound_koef(self, left_koef):
        self.__bounds_koefs[0] = left_koef

    def set_right_bound_koef(self, right_koef):
        self.__bounds_koefs[1] = right_koef

    def set_line_dpi(self, line_dpi):           
        self.__line_dpi = line_dpi

    def set_config_line(self, config_line):  
        self.__config_line = config_line

    def set_arrayX(self, array):                 
        self.__arrayX = array

    def set_arrayY(self, array):
        self.__arrayY = array

    def set_legend(self, legend):
        self.__legend = legend


    def transformX(self, func):
        new_array = np.array([])
        for it in self.arrayX:
            new_array = np.append(new_array, func(it))
        self.set_arrayX(new_array)

    def transformY(self, func):
        new_array = np.array([])
        for it in self.arrayY:
            new_array = np.append(new_array, func(it))
        self.set_arrayY(new_array)

    #Sorts data by X array
    def sort_data(self):
        array_2D = np.array(self.arrayX, self.arrayY)
        array_2D = np.transpose(array_2D)
        array_2D = np.sort(array_2D, 0)
        self.set_arrayX(array_2D[:, 0])
        self.set_arrayY(array_2D[:, 1])


    #Creates functions in given boundaries
    def create_continuous_function(self, func, left_bound, right_bound):
        self.__arrayY = np.array([])
        self.__arrayX = np.array([])
        step = (right_bound - left_bound) / self.line_dpi
        cur_pos = left_bound
        for i in range(self.__line_dpi):
            self.set_arrayY(np.append(self.arrayY, func(cur_pos)))
            self.set_arrayX(np.append(self.arrayX, cur_pos))
            cur_pos += step

    #Creates dot functions from given array
    def create_dot_function(self, func, array):
        self.set_arrayX = array
        self.set_arrayY = array
        self.transformY(func)

    #Adds data to the end of function
    def append_function(self, my_plot_func):
        self.set_arrayX(np.append(self.arrayX, my_plot_func.arrayX))
        self.set_arrayY(np.append(self.arrayY, my_plot_func.arrayY))

    #Creates continuous function from inner data
    def fit_data(self, deg):
        koefs = np.polyfit(self.arrayX, self.arrayY, deg)
        min_X = min(self.arrayX)
        max_X = max(self.arrayX)
        start = min_X - (max_X - min_X) * self.left_bound_koef
        stop = max_X + (max_X - min_X) * self.right_bound_koef
        new_X_arr = np.linspace(start, stop, self.line_dpi)
        new_Y_arr = np.polyval(koefs, new_X_arr)
        self.set_arrayX(new_X_arr)
        self.set_arrayY(new_Y_arr)
        return koefs

    #Получение ближайшего значения по X
    def get_nearest_val(self, X):
        absolute_val_array = np.abs(self.arrayX - X)
        smallest_difference_index = absolute_val_array.argmin()
        return self.__arrayY[smallest_difference_index]

    #Checks difference between func and experimental_data
    #За правильный результат берутся экспериментальные данные
    #https://en.wikipedia.org/wiki/Coefficient_of_determination
    def calc_error(self, experimental_data):
        exper_X = experimental_data[:, 0]
        exper_Y = experimental_data[:, 1]
        predict_Y = np.array([])
        for cur_X in exper_X:
            predict_Y = np.append(predict_Y, self.get_nearest_val(cur_X))
        return r2_score(exper_Y, predict_Y)

    #Fits to func() 
    def fit_to_function(self, func):
        curve_fit()
    

class MyPlot:

    __slots__ = ['__plot', '__functions', '__figure_name', '__dots']     #запрет на доступ снаружи

    num_of_figures = 0

    def __add_legend(new_line, lines_list, new_legend, legends_list):
        if new_legend != '':
            lines_list.append(new_line)
            legends_list.append(new_legend)
        return legends_list

    def __init__(self):
        self.__plot = plt.figure(MyPlot.num_of_figures)
        self.__functions = list()
        self.__dots = list()
        self.__figure_name = MyPlot.num_of_figures
        MyPlot.num_of_figures += 1

    @property
    def functions(self):
        return self.__functions

    @property
    def dots(self):
        return self.__dots

    @property
    def figure_name(self):
        return self.__figure_name

    #Returns function number and adds data to functions list 
    def add_function(self, my_plot_func):
        self.functions.append(my_plot_func)
        return len(self.functions) - 1

    #Returns dots set number and adds data to dots list 
    def add_dots(self, my_plot_func):
        self.dots.append(my_plot_func)
        return len(self.dots) - 1

    #Removes and returns data with specified number and type
    def remove_data(self, data_num, is_function):
        if is_function:
            return self.functions.pop([data_num])
        else:
            return self.dots.pop([data_num])
    
    #Creates lines from each function
    def draw_all(self):
        legends_list = []
        lines_list = []
        plt.figure(self.figure_name)
        for it in self.functions:
            line = plt.plot(it.arrayX, it.arrayY, it.config_line)
            MyPlot.__add_legend(line, lines_list, it.legend, legends_list)
        for it in self.dots:
            line = plt.scatter(it.arrayX, it.arrayY)
            MyPlot.__add_legend(line, lines_list, it.legend, legends_list)
        plt.legend(lines_list, legends_list)
        

    def config_plot(self, title, xlabel, ylabel):
        plt.figure(self.figure_name)
        plt.grid()
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)


    def save_all():
        for fig_name in range(MyPlot.num_of_figures):
            plt.figure(fig_name)
            plt.savefig(fig_name)

    def show_all():
        plt.show()



def test():
    obj1 = PlotFunction()
    obj2 = PlotFunction()

    obj1.set_arrayX([1, 2])
    obj1.set_arrayY([1, 2])

    obj2.set_arrayX([-1, -2])
    obj2.set_arrayY([-1, -2])

    plot = MyPlot()
    plot.add_function(obj1)
    plot.add_function(obj2)

    plot.config_plot('test', 'testX', 'testY')
    plot.draw_all()
    MyPlot.show_all()  

def main():
    test()

if __name__ == '__main__':
    main()
    