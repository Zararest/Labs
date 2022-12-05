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

def draw_chanels():
    chanels = np.array([94, 1856, 1638, 953, 1965, 1779, 1362, 1112, 1550])
    energy = np.array([59, 1330, 1170, 660, 1410, 1270, 964, 780, 1085])

    line = PlotFunction()
    line.set_arrayX(chanels)
    line.set_arrayY(energy)
    line.sort_data()
    coefs = line.fit_data(1)
    print('Уравнение:''y =', coefs[0], '* x +', coefs[1])

    dots = PlotFunction()
    dots.set_arrayX(chanels)
    dots.set_arrayY(energy)

    plot = MyPlot()
    plot.config_plot('Энергии от номера канала', 'N', 'E [кэВ]')
    plot.add_function(line)
    plot.add_dots(dots)
    plot.draw_all()

def draw_R():
    R = np.array([0.00185, 0.00422, 0.00240, 0.00230])
    energy = np.array([1 / 1270, 1 / 660, 1 / 1170, 1 / 1330])

    line = PlotFunction()
    line.set_arrayY(R)
    line.set_arrayX(energy)
    line.sort_data()
    coefs = line.fit_data(1)
    #print('Ошибка:', line.calc_error(np.array([energy], [R])))
    print('Уравнение:''y =', coefs[0], '* x +', coefs[1])

    dots = PlotFunction()
    dots.set_arrayY(R)
    dots.set_arrayX(energy)

    plot = MyPlot()
    plot.config_plot('R от энергии', '1 / E [1 / кэВ]', 'R')
    plot.add_function(line)
    plot.add_dots(dots)
    plot.draw_all()

def draw_back():
    energy_back = np.array([27, 240, 295, 87, 184])
    energy = np.array([61, 1329, 660, 124, 511])

    line = PlotFunction()
    line.set_arrayY(energy_back)
    line.set_arrayX(energy)
    line.sort_data()
    coefs = line.fit_data(2)
    #print('Ошибка:', line.calc_error(np.array([energy], [R])))
    #print('Уравнение:''y =', coefs[0], '* x +', coefs[1])

    dots = PlotFunction()
    dots.set_arrayY(energy_back)
    dots.set_arrayX(energy)

    plot = MyPlot()
    plot.config_plot('Энергия обратного рассеяния от энергии фотопика', 'E [кэВ]', 'E [кэВ]')
    plot.add_function(line)
    plot.add_dots(dots)
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

    #draw_spectrum(Noise, 'Noise')
    #draw_spectrum(Am_data, 'Спектр Am')
    #draw_spectrum(Co_data, 'Спектр Co')
    #draw_spectrum(Cs_data, 'Спектр Cs')
    #draw_spectrum(Eu_data, 'Спектр Eu')
    #draw_spectrum(Na_data, 'Спектр Na')
    #draw_chanels()
    #draw_R()
    draw_back()
    MyPlot.show_all()

if __name__ == '__main__':
    main()