import random as rd
import math
import seaborn as sns
import matplotlib.pyplot as plt
import statistics as st
import numpy as np

def discrete_plot(data, alpha=.5):
    hist, edges = np.histogram(data, bins=np.arange(min(data),max(data)+2)-0.5)
    return plt.bar(edges[:-1], hist, align="edge", ec="k", alpha=alpha)

#Exponential generator
def exponencial(media, n):
    sample = []
    for i in range(n):
        r = rd.random()
        x = - media * math.log(r) #Aplicación de la ecuación (11)
        sample.append(x)
    return sample

def calculoacumulada(data):
    acum = []
    serie = data[0:10:1]
    serie.sort()
    u = st.mean(serie)
    lamb = 1/u
    for i in range(len(serie)):
        x = 1 - (math.exp(-lamb*serie[i]))
        acum.append(x)
    return acum

def resta(data, s):
    resta = []
    for i in range(10):
        r = s[i] - data[i]
        resta.append(r)
    return resta

#Main
media = 1
n = 50
data = []
acum = []
resta1 = []
s = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]

data = (exponencial(media, n))
acum = (calculoacumulada(data))
resta1 = resta(data, s)

print("Los datos son: ", data)
print("Probabilidades acumuladas: ", acum)
print("Resta entre acumulada y s: ", resta1)
print("La media aritmetica observada es: ", st.mean(data))

discrete_plot(data)
plt.show()