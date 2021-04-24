import numpy as np
from tkinter import *


def evclid(a, b):
    return np.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)


def manfatan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def num_circule(x, y, fu):
    min = fu(x, y[0])
    num = 0
    for i, v in enumerate(y):
        if fu(x, v) < min:
            num = i
            min = fu(x, v)
    return num


def mudian(y):
    y.sort()
    if (len(y) % 2) == 1:
        return y[int((len(y) - 1) / 2)]
    else:
        a = y[int(len(y) / 2)]
        b = y[int((len(y) - 2) / 2)]
        return [(a[0] + b[0]) / 2, (a[1] + b[1]) / 2]


def body(x, y, fu):
    y_new = [[] for i in range(len(y))]

    for i in x:
        y_new[num_circule(i, y, fu)].append(i)

    for i in range(len(y)):
        if len(y_new[i]) != 0:
            y[i] = mudian(y_new[i])

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

    def yy(event):
        python_green = "#00ff00"
        x1, y1 = (event.x - 1), (event.y - 1)
        x2, y2 = (event.x + 5), (event.y + 5)
        w.create_oval(x1, y1, x2, y2, fill=python_green)
        print(event.x, event.y)
        y.append([event.x, event.y])

    def xx(event):
        python_green = "#cccccc"
        x1, y1 = (event.x - 1), (event.y - 1)
        x2, y2 = (event.x + 1), (event.y + 1)
        w.create_oval(x1, y1, x2, y2, fill=python_green)
        print("-", event.x, event.y)
        x.append([event.x, event.y])
        # w.delete("all")

    def run(event):
        nonlocal x
        nonlocal y
        xn = x
        yn = y
        print(x)
        print(y)

        while True:
            y2 = body(x, y, evclid)
            if y2 == y:
                break
            y = y2

        print(x)
        for i in y:
            python_green = "#ff0000"
            x1, y1 = (i[0] - 1), (i[1] - 1)
            x2, y2 = (i[0] + 5), (i[1] + 5)
            w.create_oval(x1, y1, x2, y2, fill=python_green)
        print(y)

        while True:
            y2 = body(xn, yn, manfatan)
            if y2 == yn:
                break
            yn = y2

        print(xn)
        for i in yn:
            python_green = "#0000ff"
            x1, y1 = (i[0] - 1), (i[1] - 1)
            x2, y2 = (i[0] + 5), (i[1] + 5)
            w.create_oval(x1, y1, x2, y2, fill=python_green)
        print(yn)

    w.pack(expand=YES, fill=BOTH)
    w.bind('<Button-1>', xx)
    w.bind('<Button-2>', run)
    w.bind('<Button-3>', yy)
    w.bind()

    message = Label(master, text="Press and Drag the mouse to draw")
    message.pack(side=BOTTOM)

    mainloop()


main()
