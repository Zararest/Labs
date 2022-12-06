#Я НЕНАВИЖУ ПИТОН
#Я НЕНАВИЖУ ПИТОН
#Я НЕНАВИЖУ ПИТОН
from Plot import MyPlot
from Plot import PlotFunction
#Я НЕНАВИЖУ ПИТОН
import numpy as np


def draw_line():
    V_R = np.array([3.52, 5.35, 7.14, 8.90, 10.53])
    V = np.array([0.44, 0.65, 0.85, 1.07, 1.25])

    line = PlotFunction()
    line.set_arrayY(V)
    line.set_arrayX(V_R)
    line.sort_data()
    coefs = line.fit_data(1)
    #print('Ошибка:', line.calc_error(np.array([energy], [R])))
    print('Уравнение:''y =', coefs[0], '* x +', coefs[1])

    dots = PlotFunction()
    dots.set_arrayY(V)
    dots.set_arrayX(V_R)

    plot = MyPlot()
    plot.config_plot('Зависимость напряжения на пробной катушке от напряжения в цепи', 'V_R [мВ]', 'V [мВ]')
    plot.add_function(line)
    plot.add_dots(dots)
    plot.draw_all()

def main():
    draw_line()
    MyPlot.show_all()

if __name__ == '__main__':
    main()