#!usr/bin/python3

import numpy as np             
import matplotlib.pyplot as plt


class PlotFunction:

    #dpi - dots per interval
    def __init__(self):
        self.__arrayX = np.array([])
        self.__arrayY = np.array([])
        self.__config_line = '--'
        self.__legend = ''
        self.__line_dpi = 1000              

    #getters
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

    #Creates functions in given boundaries
    def create_continuous_function(self, func, left_bound, right_bound):
        np.delete(self.arrayY)
        np.delete(self.arrayX)
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

    #Creates continuous function from given data
    def fit_data(self, dots, left_bound, right_data):
        pass
    

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
    