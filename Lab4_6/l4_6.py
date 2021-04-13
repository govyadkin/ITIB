import math
import matplotlib.pyplot as plt


def f_net(w, x):
    net = 0
    for i, j in zip(w, x):
        net += i * j

    return net


def func(w1, w2, w3):
    y = [3, 1]
    x1 = [1, 2, 2]
    fu = lambda x: (1 - math.exp(-x)) / (1 + math.exp(-x))
    fui = lambda x: 0.5 * (1 - x ** 2)

    em = []
    num = 0
    while num < 100:
        net1 = f_net(w1, x1)
        x23 = [1, fu(net1)]

        net2 = f_net(w2, x23)
        y1 = fu(net2)

        net3 = f_net(w3, x23)
        y2 = fu(net3)
        e = math.sqrt((y[0] - y1) ** 2 + (y[1] - y2) ** 2)
        em += [e]
        print("y = (", y1, y2, "), E(", num, ")=", e)
        if e < 0.001:
            break

        d1 = fui(y1) * (y[0] - y1)
        d2 = fui(y2) * (y[1] - y2)
        d0 = fui(x23[1]) * (w2[1] * d1 + w3[1] * d2)

        for i, j in enumerate(x1):
            w1[i] += d0 * j

        for n, i in enumerate(x23):
            w2[n] += d1 * i
            w3[n] += d2 * i

        num += 1

    plt.xlabel("эпоха")  # ось абсцисс
    plt.ylabel("e")  # ось ординат
    plt.grid()
    ex = [i for i in range(len(em))]
    plt.plot(ex, em)
    plt.show()


func([0, 0, 0], [0, 0], [0, 0])
