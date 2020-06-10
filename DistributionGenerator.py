import math as mt
import numpy as np
from scipy import special
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns
import random as rd


def generate_uniform(a, b, size):
    uniformValuesList = []
    for i in range(size):
        r = rd.random()
        uniformValue = r * (b - a) + a
        uniformValuesList.append(uniformValue)
    return uniformValuesList


# Funcion que devuelve una lista de valores que siguen una distribucion normal(mu,variance)
def generate_normal_values(m, var, size):
    normalValuesList = []
    for i in range(sample_size):
        p = rd.random()
        normalValue = m + var * mt.sqrt(2) * special.erfinv((2 * p) - 1)
        normalValuesList.append(normalValue)
    return normalValuesList


def generate_normal(mu, sigma, size):
    normalValuesList = []
    for z in range(size):
        sum = 0.0
        for i in range(12):
            sum += rd.random()
        normalValue = sigma * (sum - 6.0) + mu
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


def plot_uniform():
    X = np.arange(2, 5, 0.1)
    U = (1 / 3) * (X / X)
    plt.plot(X, U)
    plt.show()


def plot_hipergeometric():
    k = np.arange(0, 21)
    U = stats.hypergeom.pmf(k, 500, 50, 100)
    plt.plot(U)
    plt.xlim(1, 25)
    plt.show()


def plot_exponencial():
    L = 1
    X = np.arange(0, 5, 0.01)
    P = L * np.exp(-L * X)
    plt.plot(X, P)
    plt.show()


def plot_binomial():
    n = 5
    p = 0.41
    k = np.arange(0, 21)
    binomial = stats.binom.pmf(k, n, p)
    plt.plot(k, binomial)
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
    d = p * (np.power((1 - p), t))

    plt.plot(t, d)
    plt.show()


if __name__ == "__main__":
    sample_size = 10000
    mu = 5
    variance = 1
    sigma = mt.sqrt(variance)
    normalValues = generate_normal_values(mu, variance, sample_size)
    normalValues = generate_normal(mu,sigma,sample_size)
    plotting_normal(mu, sigma, normalValues)
    lambd = 5
    poissonValues = generate_poisson_values(lambd, sample_size)
    plotting_poisson(lambd, poissonValues)
    p = 0.3
    geometricValues = generate_geometric_values(p, sample_size)
    plotting_geometric(p, geometricValues)
    plot_binomial()
    plot_exponencial()
    plot_uniform()
    plot_hipergeometric()
