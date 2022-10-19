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

def parse_file(file_name):
    data = np.array([])
    data = np.loadtxt(file_name, dtype=float)
    return data

def transform_data(data, functions):
    new_data = np.copy(data)
    for cur_func in functions:
        new_data = cur_func(np.copy(new_data))
    return new_data

#данные: В | мА
def create_graph(data, title):
    func = PlotFunction()
    func.set_arrayX(data[:, 0])
    func.set_arrayY(data[:, 1])

    dots = PlotFunction()
    dots.set_arrayX(data[:, 0])
    dots.set_arrayY(data[:, 1])
    dots.set_legend('Экспериментальные данные')

    plot = MyPlot()
    plot.config_plot(title, 'Напряжение [B]', 'Ток [мА]')
    plot.add_function(func)
    plot.add_dots(dots)
    plot.draw_all()


def main():
    volt_4_data = parse_file('volt_4.txt')
    volt_6_data = parse_file('volt_6.txt')
    volt_9_data = parse_file('volt_9.txt')

    create_graph(volt_4_data, 'Запирающее напряжение 4 В')
    create_graph(volt_6_data, 'Запирающее напряжение 6 В')
    create_graph(volt_9_data, 'Запирающее напряжение 9 В')

    MyPlot.show_all()

if __name__ == '__main__':
    main()
