import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import interactive
from scipy import stats
import pandas as pd


# Global variables


# LCG Implementation

def lcg(a, c, m, initial_seed):
    seed = initial_seed
    while True:
        rand = (a * seed + c) % m
        seed = rand
        yield rand


def random_sample(n, seed):
    sample = []
    varAux = lcg(1103590199, 419329, (2 ** 32), seed)
    for i in range(n):
        observation = next(varAux) / (2 ** 32)
        sample.append(observation)

    return sample


# Von neumann Implementation

def midSquare(seed, n):
    list = []
    for i in range(n):
        nro = seed * seed
        nro = str(nro).zfill(8) # Rellena el int con 0 si tiene menos de 8 digitos
        nro = nro[2:6] # Saca los 4 digitos del medio
        nro = int(nro)
        u = nro / 9999
        list.append(u)
        seed = nro
    return list


# Test to LCG

def mean(data):
    return np.mean(data)


def test_kolmogorov(data,sample_size):
    dataaux = data.sort()
    max = 0.0
    for i in range(sample_size):
        observed = data[i]
        expected = i / sample_size

        distance = np.abs(observed - expected)
        if distance > max:
            max = distance

    return max


def test_chisquare(data, intervals, alpha=0.95):
    observation = pd.DataFrame(data, columns=['counts'])
    ranges = [i / intervals for i in range(intervals + 1)]
    observation = observation.groupby(pd.cut(observation['counts'], ranges)).count()
    cross = np.array([observation['counts'], [len(data) // intervals] * intervals])
    chi2_stat, p_value, dof, expected_table = stats.chi2_contingency(cross)
    threshold = stats.chi2.ppf(alpha, dof)
    return chi2_stat, p_value, threshold, alpha


def test_spectral():
    x = random_sample(10000, seed)
    y = random_sample(10000, seed + 1)

    fig = plt.figure()
    plt.plot(x, y, '.g', markersize=1.0)

    plt.xlim(0, 1)
    plt.ylim(0, 1)
    plt.show()

    np.random.seed(seed)
    x = np.random.random(10000)
    np.random.seed(seed + 1)
    y = np.random.random(10000)


    fig = plt.figure()
    plt.plot(x, y, '.g', markersize=1.0)

    plt.xlim(0, 1)
    plt.ylim(0, 1)
    plt.show()


def test_spectral_three():
    x = random_sample(10000, 325)
    y = random_sample(10000, 1233)
    z = random_sample(10000, 64126)

    fig = plt.figure()
    ax = plt.axes(projection='3d')
    plt.plot(x, y, z, '.g', markersize=1.0)

    ax.view_init(70, 30)
    plt.show()

    np.random.seed(325)
    x = np.random.random(10000)

    np.random.seed(1233)
    y = np.random.random(10000)

    np.random.seed(64126)
    z = np.random.random(10000)

    fig = plt.figure()
    ax = plt.axes(projection='3d')
    plt.plot(x, y, z, '.g', markersize=1.0)

    ax.view_init(70, 30)
    plt.show()


def plot_bitmap():
    Z = np.array(random_sample(250000, 64126)).reshape((500, 500))
    plt.imshow(Z, cmap='gray', interpolation='nearest')
    plt.show()

    U = np.random.random((500, 500))
    plt.imshow(U, cmap='gray', interpolation='nearest')
    plt.show()


# def test_autocorrelation(data, start, jump):
#     index1 = start
#     index2 = start + jump
#     total = 0.0
#     k = 0
#
#     while index2 < sample_size:
#         total += data[index1] * data[index2]
#         index1 = start + (jump * k)
#         index2 = start + (jump * (k + 1))
#         k += 1
#
#     mu = float(total / k + 1)
#     mu -= 0.25
#
#     num = float(13 * k + 7)
#     dem = float(12 * (k + 1))
#     variance = np.sqrt(num) / dem
#     z_stat = mu / variance
#     return z_stat



# Main section
seed = 4294966661
sample_size = 10
LcgData1 = np.array(random_sample(sample_size, seed))
np.random.seed(seed)
PyData1 = np.random.random(sample_size)


seed = 4294950
sample_size = 100
LcgData2 = np.array(random_sample(sample_size, seed))
np.random.seed(seed)
PyData2 = np.random.random(sample_size)


seed = 1103590199
sample_size = 1000
LcgData3 = np.array(random_sample(sample_size, seed))
np.random.seed(seed)
PyData3 = np.random.random(sample_size)


#Tabla promedio entre dos distribuciones

print('Promedio 1:  LCG: ', mean(LcgData1),' Py: ',mean(PyData1))
print('Promedio 2:  LCG: ', mean(LcgData2),' Py: ',mean(PyData2))
print('Promedio 3:  LCG: ', mean(LcgData3),' Py: ',mean(PyData3))
print('')

#Tabla kolmogorov

print('Kolmo 1:  LCG: ', test_kolmogorov(LcgData1, len(LcgData1)),' Py: ',test_kolmogorov(PyData1, len(PyData1)))
print('Kolmo 2:  LCG: ', test_kolmogorov(LcgData2, len(LcgData2)),' Py: ',test_kolmogorov(PyData2, len(PyData2)))
print('Kolmo 3:  LCG: ', test_kolmogorov(LcgData3, len(LcgData3)),' Py: ',test_kolmogorov(PyData3, len(PyData3)))
print('')
# Tabla chi2
print('')
chi2, p, _, alpha = test_chisquare(LcgData1, 10)
print('Chisquare LCG 1: chi2: ', chi2, ' p: ', p, ' alpha: ', alpha)
chi2, p, _, alpha = test_chisquare(PyData1, 10)
print('Chisquare PY 1: chi2: ', chi2, ' p: ', p, ' alpha: ', alpha)
print('')
chi2, p, _, alpha = test_chisquare(LcgData2, 10)
print('Chisquare LCG 2: chi2: ', chi2, ' p: ', p, ' alpha: ', alpha)
chi2, p, _, alpha = test_chisquare(PyData2, 10)
print('Chisquare PY 2: chi2: ', chi2, ' p: ', p, ' alpha: ', alpha)
print('')
chi2, p, _, alpha = test_chisquare(LcgData3, 10)
print('Chisquare LCG 3: chi2: ', chi2, ' p: ', p, ' alpha: ', alpha)
chi2, p, _, alpha = test_chisquare(PyData3, 10)
print('Chisquare PY 3: chi2: ', chi2, ' p: ', p, ' alpha: ', alpha)


#Spectral test
test_spectral()
test_spectral_three()

#Bitmap
plot_bitmap()


