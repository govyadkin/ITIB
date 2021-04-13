import numpy as np
from math import sqrt, exp, pow
import matplotlib.pyplot as plt


class Neur:
    def __init__(self, realValues1, winLen1, teachingRate1):
        self.windowLen = winLen1
        self.pointsNum = 20
        self.w = [0] * (self.windowLen + 1)
        self.realVal = realValues1
        self.neuronVal = self.realVal[:self.windowLen] + [0] * (self.pointsNum - self.windowLen)
        self.nn = teachingRate1

    def Train(self, maxIter):
        num = 0
        epsilon = 0
        while num < maxIter:
            for i in range(self.windowLen, self.pointsNum):
                net = self.w[self.windowLen]
                for j in range(self.windowLen):
                    net += self.w[j] * self.realVal[i - self.windowLen + j]
                self.neuronVal[i] = net

                for j in range(self.windowLen):
                    self.w[j] += self.nn * (self.realVal[i] - self.neuronVal[i]) * self.realVal[i - self.windowLen + j]

                epsilon = 0
                for j in range(self.windowLen, self.pointsNum):
                    epsilon += pow(self.realVal[j] - self.neuronVal[j], 2)

                epsilon = sqrt(epsilon)

                if epsilon < 0.0001:
                    print(epsilon)
                    break

            num += 1
            print(num, epsilon, self.w)

    def predict(self, num):
        for i in range(self.pointsNum, self.pointsNum + num):
            net = self.w[self.windowLen]
            for j in range(self.windowLen):
                net += self.w[j] * self.neuronVal[i - self.windowLen + j]

            self.neuronVal += [net]


def CalculateFunc(begin, end, pointsQuantity, f):
    step = (end - begin) / (pointsQuantity - 1)
    res = []
    points = []
    for i in range(pointsQuantity):
        points += [begin + step * i]
        res += [f(begin + step * i)]
    return points, res


def main():
    fun = lambda x: exp(x - 2) - np.sin(x)
    a = -1
    b = 2
    x, realValues = CalculateFunc(a, b, 20, fun)
    x1, y1 = CalculateFunc(b, 2 * b - a, 20, fun)
    realValues += y1
    x += x1

    c = 800
    d = 8
    b = 0.5

    n = Neur(realValues, d, b)
    n.Train(c)

    n.predict(20)

    plt.xlabel("x")  # ось абсцисс
    plt.ylabel("y")  # ось ординат
    plt.grid()
    plt.plot(x, realValues)
    plt.plot(x, n.neuronVal)
    plt.show()


main()
