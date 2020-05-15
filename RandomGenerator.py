import pylab as plt
import numpy as np
import scipy as sci


# LCG Implementation

def lcg(a, c, m, initial_seed):
    seed = initial_seed
    while True:
        rand = (a * seed + c) % m
        seed = rand
        yield rand

def random_sample(n, seed = 1103603443773377):
    sample = []
    global sum
    varAux = lcg(1103590199, 419329, (2**32), seed)
    for i in range(n):
        observation = next(varAux) / (2**32)
        sum += observation
        sample.append(observation)

    return sample

#Test to LCG

def







# Bitmap plot of LGC and numpy random
def plot_bitmap():
    Z = np.array(random_sample(250000)).reshape((500,500))
    plt.imshow(Z, cmap='gray', interpolation='nearest')
    plt.show()

    U = np.random.random((500, 500))   # Test data
    plt.imshow(U, cmap='gray', interpolation='nearest')
    plt.show()
