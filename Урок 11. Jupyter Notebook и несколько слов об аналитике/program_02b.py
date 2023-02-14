import matplotlib.pyplot as plt
import numpy as np

limit = 20
step = 0.01
step_acr = 0.000001
line_style = '-'
direct_up = True
line_color = 'b'

style_blue_up = True
style_blue_down = True
style_red_up = True
style_red_down = True
root = True


def choose_line_color():
    global line_color
    line_color = 'r' if line_color == 'b' else 'b'
    return line_color


def choose_line_style():
    global line_style
    line_style = '-' if line_style == '--' else '--'
    return line_style


def x_fun(x):
    f = -12 * x ** 4 * np.sin(np.cos(x)) - 18 * \
        x ** 3 + 5 * x ** 2 + 10 * x - 30
    return f


x = np.arange(-limit, limit + step, step)
x_change = [(-limit, 'limit')]

for i in range(len(x) - 1):

    if x_fun(x[i]) > 0 and x_fun(x[i + 1]) < 0 or x_fun(x[i]) < 0 and x_fun(x[i + 1]) > 0:
        x_acr = np.arange(x[i], x[i + 1] + step_acr, step_acr)

        for j in range(len(x_acr) - 1):
            if x_fun(x_acr[j]) > 0 and x_fun(x_acr[j + 1]) < 0 or x_fun(x_acr[j]) < 0 and x_fun(x_acr[j + 1]) > 0:
                x_change.append((x_acr[j], 'zero'))

    if direct_up:
        if (x_fun(x[i])) > x_fun(x[i + 1]):
            direct_up = False
            x_change.append((x[i], 'dir'))

    else:
        if x_fun(x[i]) < x_fun(x[i + 1]):
            direct_up = True
            x_change.append((x[i], 'dir'))


x_change.append((limit, 'limit'))

for i in range(len(x_change) - 1):
    cur_x = np.arange(x_change[i][0], x_change[i + 1][0] + step, step)
    if x_change[i][1] == 'zero':
        if root:
            lbl = 'Корни уравнения'

            root = False

        else:
            lbl = None

        plt.plot(x_change[i][0], x_fun(x_change[i][0]), 'go', label=lbl)
        plt.rcParams['lines.linestyle'] = choose_line_style()
        plt.plot(cur_x, x_fun(cur_x), line_color)
    else:
        if line_color == 'r' and line_style == '-' and style_blue_up:
            lbl = 'X является убывающим & выше нуля'

            style_blue_up = False

        elif line_color == 'r' and line_style == '--' and style_blue_down:
            lbl = 'X является убывающим & ниже нуля'

            style_blue_down = False

        if line_color == 'b' and line_style == '-' and style_red_up:
            lbl = 'X является возрастающим & выше нуля'

            style_red_up = False

        elif line_color == 'b' and line_style == '--' and style_red_down:
            lbl = 'X является возрастающим & ниже нуля'

            style_red_down = False

        plt.plot(cur_x, x_fun(cur_x), choose_line_color(), label=lbl)
        lbl = None

plt.grid()
plt.legend()
plt.show()
