import random as rn
import matplotlib.pyplot as plt
import seaborn as sns
import statistics as st
import math

sns.set_style("white")


def uniform(a, b):
    r = rn.random()
    return r*(b-a) + a

def calculoacumulada(data, a, b):
    acum = []
    serie = data[0:10:1]
    serie.sort()
    for i in range(len(serie)):
        x = (serie[i] - a)/(b-a)
        acum.append(x)
    return acum

def resta(data, s):
    resta = []
    for i in range(10):
        r = s[i] - data[i]
        resta.append(r)
    return resta

if __name__ == "__main__":
    data = []
    a = 2
    b = 5
    for i in range(10000):
        data.append(uniform(a, b))

    s = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]

    print(data)
    print(calculoacumulada(data, a, b))
    print(resta(data, s))

    sns.distplot(data, kde=False)
    plt.show()