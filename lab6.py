import numpy as np
from tkinter import *


def euclid(a, b):
    return np.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)


def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def num_circle(x, y, fu):
    min = fu(x, y[0])
    num = 0
    for i, v in enumerate(y):
        if fu(x, v) < min:
            num = i
            min = fu(x, v)
    return num


def average(a, b):
    return (a + b) / 2


def median(y):
    a = [i[0] for i in y]
    b = [i[1] for i in y]
    a.sort()
    b.sort()
    if (len(y) % 2) == 1:
        return [a[int((len(y) - 1) / 2)], b[int((len(y) - 1) / 2)]]
    else:
        return [average(a[int(len(y) / 2)], a[int((len(y) - 2) / 2)]),
                average(b[int(len(y) / 2)], b[int((len(y) - 2) / 2)])]


def epohe(x, y, fu, num):
    y_new = [[] for i in range(len(y))]

    for i in x:
        y_new[num_circle(i, y, fu)].append(i)

    print("Эпоха №", num)
    print("Центр  --  сопоставимые точки")
    for i in range(len(y)):
        print(y[i], "  --  ", y_new[i])

    for i in range(len(y)):
        if len(y_new[i]) != 0:
            y[i] = median(y_new[i])

    print("Новые центры: ", y)

    return y


def main():
    canvas_width = 500
    canvas_height = 150

    x = []
    y = []

    master = Tk()
    master.title("Points")
    w = Canvas(master,
               width=canvas_width,
               height=canvas_height)

    def drow(color, size, x_print, y_print):
        x1, y1 = (x_print - 1), (y_print - 1)
        x2, y2 = (x_print + size), (y_print + size)
        w.create_oval(x1, y1, x2, y2, fill=color)

    def yy(event):
        drow("#00ff00", 5, event.x, event.y)
        print(event.x, event.y)
        y.append([event.x, event.y])

    def xx(event):
        drow("#cccccc", 1, event.x, event.y)
        print("-", event.x, event.y)
        x.append([event.x, event.y])

    def body(xn, yn, fun, color):
        i = 1
        while True:
            y2 = epohe(xn, [i for i in yn], fun, i)
            if y2 == yn:
                break
            yn = [i for i in y2]
            i += 1

        for i in yn:
            drow(color, 5, i[0], i[1])

    def run(event):
        nonlocal x
        nonlocal y
        print("Исходные данные:")

        print("X: ", x)
        print("Y: ", y, "\n")

        yn = [i for i in y]

        print("По Евклиду:")
        body(x, y, euclid, "#ff0000")
        print()

        print("По Манхэттену:")
        body(x, yn, manhattan, "#0000ff")
        print()

    w.pack(expand=YES, fill=BOTH)
    w.bind('<Button-1>', xx)
    w.bind('<Button-2>', run)
    w.bind('<Button-3>', yy)
    w.bind()

    message = Label(master, text="ПКМ - y // ЛКМ - x // колесико - run")
    message.pack(side=BOTTOM)

    mainloop()


main()
