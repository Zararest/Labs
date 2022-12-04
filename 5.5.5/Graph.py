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
#---------------------


def draw_spectrum(data, legend):
    func = PlotFunction()
    func.set_arrayX(data[:, 0])
    func.set_arrayY(data[:, 1])
    
    dots = PlotFunction()
    dots.set_arrayX(data[:, 0])
    dots.set_arrayY(data[:, 1])

    plot = MyPlot()
    plot.config_plot(legend, 'Номер канала', 'Энергия')
    plot.add_function(func)
    #plot.add_dots(dots)
    plot.draw_all()


def main():
    Am_data = parse_file('Am.txt')
    Co_data = parse_file('Co.txt')
    Cs_data = parse_file('Cs.txt')
    Eu_data = parse_file('Eu.txt')
    Na_data = parse_file('X.txt')
    Noise = parse_file('Noise.txt')
    Am_data[:, 1] = Am_data[:, 1] - Noise[:, 1]
    Co_data[:, 1] = Co_data[:, 1] - Noise[:, 1]
    Cs_data[:, 1] = Cs_data[:, 1] - Noise[:, 1]
    Eu_data[:, 1] = Eu_data[:, 1] - Noise[:, 1]
    Na_data[:, 1] = Na_data[:, 1] - Noise[:, 1] 

    draw_spectrum(Noise, 'Noise')
    draw_spectrum(Am_data, 'Спектр Am')
    draw_spectrum(Co_data, 'Спектр Co')
    draw_spectrum(Cs_data, 'Спектр Cs')
    draw_spectrum(Eu_data, 'Спектр Eu')
    draw_spectrum(Na_data, 'Спектр Na')
    MyPlot.show_all()

if __name__ == '__main__':
    main()