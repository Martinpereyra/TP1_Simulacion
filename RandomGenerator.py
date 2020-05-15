import pylab as plt
import numpy as np
from scipy import stats
import pandas as pd

#Global variables



# LCG Implementation

def lcg(a, c, m, initial_seed):
    seed = initial_seed
    while True:
        rand = (a * seed + c) % m
        seed = rand
        yield rand

def random_sample(n, seed = 1103603443773377):
    sample = []
    varAux = lcg(1103590199, 419329, (2**32), seed)
    for i in range(n):
        observation = next(varAux) / (2**32)
        sample.append(observation)

    return sample

#Test to LCG

def mean(data):
    return np.mean(data)

def test_kolmogorov(data):
    return stats.kstest(data, 'uniform')


# def test_chisquare(data, intervals):





# Bitmap plot of LGC and numpy random
def plot_bitmap():
    Z = np.array(random_sample(250000)).reshape((500,500))
    plt.imshow(Z, cmap='gray', interpolation='nearest')
    plt.show()

    U = np.random.random((500, 500))   # Test data
    plt.imshow(U, cmap='gray', interpolation='nearest')
    plt.show()



#Main section
sample_size = 40
data = np.array(random_sample(sample_size))
print(mean(data))
print(test_kolmogorov(data))


# Standby things

# df = pd.DataFrame({
#     'i': [],
#     'F(Xi)': [],
#     'i/n': [],
#     'i/n - F(Xi)': [],
#     'F(Xi) – (i-1)/n': []
# })

# df1 = pd.DataFrame({
#     'i': [i],
#     'F(Xi)': [f],
#     'i/n': [i_n],
#     'i/n - F(Xi)': [infx],
#     'F(Xi) – (i-1)/n': [fxi]
# })
# df = df.append(df1, ignore_index=True)