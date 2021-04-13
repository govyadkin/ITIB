import numpy as np
from itertools import chain, combinations
import matplotlib.pyplot as plt


def binar(number, dis):
    b = list(bin(number)[2:])
    b = list("0" * (dis - len(b))) + b
    b = [int(num) for num in b]
    return b


def phi(c, x):
    ph = [1]
    for el_c in c:
        result = sum([(x[i] - el_c[i]) ** 2 for i in range(len(x))])
        ph += [np.exp(-result)]
    return ph


def f_net(w, x):
    net = 0
    for i, j in zip(w, x):
        net += i * j

    return net


def res_y_e(num, function, dis, w, c, fun, bool_print):
    res = ""
    e = 0
    for number, value in enumerate(function):
        y = fun(f_net(w, phi(c, binar(number, dis))))
        res += str(y) + ","
        e += int(value != y)

    if bool_print:
        print(num, "Y=[", res, "], W=", np.around(w, 7), " E =", e)
    return e


def fu2(functions, fun, funi, bool_print, mask):
    function = [int(num) for num in functions]

    n = 0.3
    dis = 4
    w = [0] * 4
    c = [[0, 0, 0, 0], [0, 0, 0, 1], [1, 0, 0, 0]]

    num = 0
    e = res_y_e(num, function, dis, w, c, fun, bool_print)

    em = [e]
    while e != 0 and num < 100:
        for number, value in enumerate(function):
            if mask[number] == 1:
                ph = phi(c, binar(number, dis))
                net = f_net(w, ph)
                d = value - fun(net)

                for i in range(len(w)):
                    w[i] += n * d * ph[i] * funi(net)

        num += 1
        e = res_y_e(num, function, dis, w, c, fun, bool_print)
        em += [e]

    if bool_print:
        plt.xlabel("эпоха")  # ось абсцисс
        plt.ylabel("e")  # ось ординат
        plt.grid()
        ex = [i for i in range(len(em))]
        plt.plot(ex, em)
        plt.show()

    return e, w


def all_subsets(ss):
    return chain(*map(lambda x: combinations(ss, x), range(2, len(ss) + 1)))


def fu3(functions, fun, funi):
    stuff = []
    for i in range(16):
        stuff += [i]

    for subset in all_subsets(stuff):
        mask = [0] * 2 ** 4
        for i in subset:
            mask[i] = 1

        e, w = fu2(functions, fun, funi, False, mask)
        if e == 0:
            print(subset)
            fu2(functions, fun, funi, True, mask)
            break


funct = "0011" + "1111" + "0111" + "1111"

print("------------------1")
fu2(funct, lambda x: int(x >= 0), lambda x: 1, True, [1] * 16)
print("------------------")
fu3(funct, lambda x: int(x >= 0), lambda x: 1)

print("------------------2")
fu2(funct, lambda x: int(((1 + np.tanh(x)) / 2) >= 0.5), lambda x: (1 - np.tanh(x) ** 2) / 2, True, [1] * 16)
print("------------------")
fu3(funct, lambda x: int(((1 + np.tanh(x)) / 2) >= 0.5), lambda x: (1 - np.tanh(x) ** 2) / 2)
