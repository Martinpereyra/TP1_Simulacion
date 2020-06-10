import math as mt
import numpy as np
from scipy import special
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns
import random as rd


# Funcion que devuelve una lista de valores que siguen una distribucion normal(mu,variance)
def generate_normal_values(m, var, size):
    normalValuesList = []
    for i in range(sample_size):
        p = rd.random()
        normalValue = m + var * mt.sqrt(2) * special.erfinv((2 * p) - 1)
        normalValuesList.append(normalValue)
    return normalValuesList


def plotting_normal(m, sig, normalValuesList):
    sns.distplot(normalValuesList, kde=False, color="b")
    plt.show()

    x = np.linspace(m - 3 * sig, m + 3 * sig, 100)
    plt.plot(x, stats.norm.pdf(x, m, sig))
    plt.show()


def generate_poisson_values(p, size):
    poissonValuesList = []
    b = np.exp(-p)
    for i in range(size):
        x = 0
        tr = 1.0
        r = rd.random()
        tr = tr * r
        while tr >= b:
            x += 1
            r = rd.random()
            tr = tr * r
        poissonValuesList.append(x)
    return poissonValuesList


def plotting_poisson(lambd, poissonValues):
    sns.distplot(poissonValues, kde=False, color="b")
    plt.show()

    t = np.arange(0, 20, 0.1)
    d = np.exp(-lambd) * np.power(lambd, t) / special.factorial(t)

    plt.plot(t, d)
    plt.show()


def generate_geometric_values(p, size):
    geometricValuesList = []
    for i in range(size):
        r = rd.random()
        q = 1 - p
        x = mt.floor(mt.log(r) / mt.log(q))
        geometricValuesList.append(x)
    return geometricValuesList


def plotting_geometric(p, geometricValues):
    sns.distplot(geometricValues, kde=False, color="b")
    plt.show()

    t = np.arange(0, 20, 0.1)
    d = p*(np.power((1-p), t))

    plt.plot(t, d)
    plt.show()

if __name__ == "__main__":
    sample_size = 10000
    mu = 0
    variance = 1
    sigma = mt.sqrt(variance)
    normalValues = generate_normal_values(mu, variance, sample_size)
    plotting_normal(mu, sigma, normalValues)
    lambd = 5
    poissonValues = generate_poisson_values(lambd, sample_size)
    plotting_poisson(lambd, poissonValues)
    p = 0.3
    geometricValues = generate_geometric_values(p, sample_size)
    print(np.mean(geometricValues))
    # plotting_geometric(p, geometricValues)
