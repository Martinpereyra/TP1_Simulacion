import random as rd

from RandomGenerator import random_sample
import math as mt
import numpy as np
from scipy import special
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns

# Funcion que devuelve una lista de valores que siguen una distribucion normal(mu,variance)
def generate_normal_values(uniformValuesList, sample_size):
    normalValuesList = []
    for i in range(sample_size):
        p = uniformValuesList[i]
        normalValue = mu + variance * mt.sqrt(2) * special.erfinv((2 * p) - 1)
        normalValuesList.append(normalValue)
    return normalValuesList


def plotting(mu, sigma, normalValuesList):
    sns.distplot(normalValuesList, kde=False, color="b")
    plt.show()

    x = np.linspace(mu - 3 * sigma, mu + 3 * sigma, 100)
    plt.plot(x, stats.norm.pdf(x, mu, sigma))
    plt.show()


if __name__ == "__main__":
    seed = 4294966661
    sample_size = 1000
    mu = 0
    variance = 1
    sigma = mt.sqrt(variance)
    uniformValuesList = random_sample(sample_size, seed)
    plotting(mu, sigma, generate_normal_values(uniformValuesList, sample_size))
