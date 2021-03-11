import numpy as np
from itertools import chain, combinations


def binar(number, dis):
    b = list(bin(number)[2:])
    b = list("1" + "0" * (dis - len(b))) + b
    b = [int(num) for num in b]
    return b


def f_net(w, x):
    net = 0
    for i, j in zip(w, x):
        net += i * j

    return net


def res_y_e(num, function, dis, w, fun, bool_print):
    res = ""
    e = 0
    for number, value in enumerate(function):
        y = fun(f_net(w, binar(number, dis)))
        res += str(y)+","
        e += int(value != y)

    if bool_print:
        print(num, "Y=[", res,"], W=", np.around(w, 3)," E =", e)
    return e


def fu2(functions, fun, funi, bool_print, mask):
    function = [int(num) for num in functions]

    dis = 4
    n = 0.3
    w = [0] * (dis + 1)

    num = 0
    e = res_y_e(num, function, dis, w, fun, bool_print)
    while e != 0 and num < 100:
        for number, value in enumerate(function):
            if mask[number] == 1:
                x = binar(number, dis)
                net = f_net(w, x)
                y = fun(net)
                d = value - y

                for i in range(len(w)):
                    w[i] += n * d * x[i] * funi(net)

        num += 1
        e = res_y_e(num, function, dis, w, fun, bool_print)

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
print("------------------2")
fu2(funct, lambda x: int(((1 + np.tanh(x)) / 2) >= 0.5), lambda x: (1 - np.tanh(x) ** 2) / 2, True, [1] * 16)
print("------------------3")
fu3(funct, lambda x: int(x >= 0), lambda x: 1)

# funct = "0001" * 3 + "0000"
# fu2(funct, lambda x: int(1 / (1 + np.exp(-x)) >= 0.5), lambda x: (1 / (1 + np.exp(-x))) * (1 - (1 / (1 + np.exp(-x)))))
# print("------------------")
