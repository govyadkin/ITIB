import random
import numpy as np


class Lab5:
    def __init__(self, init_symbols, width, height):
        self.len = len(init_symbols[0])
        self.weights_matrix = np.zeros((self.len, self.len), dtype=int, order='C')
        self._init_weights_matrix(init_symbols)
        self.width = width
        self.height = height

    def _init_weights_matrix(self, init_symbols):
        self.len = len(init_symbols[0])
        for i in range(self.len):
            for j in range(i + 1, self.len):
                for k in range(len(init_symbols)):
                    self.weights_matrix[i][j] += init_symbols[k][i] * init_symbols[k][j]
                self.weights_matrix[j][i] = self.weights_matrix[i][j]
        # print(self.weights_matrix)
        for i in self.weights_matrix:
            print(i)

    def print_num(self, num, res):
        for i in range(self.height):
            s = ""
            for j in range(self.width):
                if num[i + j * self.height] == 1:
                    s += " ⬛"
                else:
                    s += "  "
            s += " --- "
            for j in range(self.width):
                if res[i + j * self.height] == 1:
                    s += " ⬛"
                else:
                    s += "  "
            print(s)

    def output_result_synchronously(self, vec):
        res = np.dot(vec, self.weights_matrix)

        def f_net(i, j):
            if j == 0:
                return vec[i]
            return int(j / np.abs(j))

        return [f_net(i, j) for i, j in enumerate(res)]

    def final_conclusion(self, vec):
        while True:
            res = self.output_result_synchronously(vec)
            # print(res)

            flag = True

            for i, j in zip(res, vec):
                if j != i:
                    flag = False

            if flag:
                break

            vec = res

            # self.print_num(vec)

        return vec


def get_vec(symbol):
    for i in range(int(len(symbol) / 10)):
        symbol[random.randint(0, len(symbol) - 1)] *= -1
    return symbol


def main():
    width = 5
    height = 7
    symbols = [[-1, 1, -1, -1, -1, -1, 1,
                1, -1, -1, -1, -1, 1, 1,
                1, -1, -1, -1, 1, -1, 1,
                1, -1, -1, 1, -1, -1, 1,
                -1, 1, 1, -1, -1, -1, 1],

               [-1, -1, -1, 1, 1, -1, -1,
                -1, -1, 1, -1, 1, -1, -1,
                -1, 1, -1, -1, 1, -1, -1,
                1, 1, 1, 1, 1, 1, 1,
                -1, -1, -1, -1, 1, -1, -1],

               [-1, -1, 1, 1, 1, 1, -1,
                -1, 1, -1, 1, -1, -1, 1,
                1, -1, -1, 1, -1, -1, 1,
                1, -1, -1, 1, -1, -1, 1,
                -1, -1, -1, -1, 1, 1, -1, ]
               ]

    lab = Lab5(symbols, width, height)
    print("Эталонный тест")
    for i in symbols:
        lab.print_num(i, lab.final_conclusion(i))
        print("---------------------------")

    for i in symbols:
        vec = get_vec(i)
        lab.print_num(vec, lab.final_conclusion(vec))
        print("---------------------------")


main()
