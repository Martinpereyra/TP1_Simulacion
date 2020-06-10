import math
import seaborn as sns
import matplotlib.pyplot as plt
import random as rd
import statistics as st


def binomial(n, p):  #Calcula una variable aleatoria con distribucion binomial
    x = 0
    for i in range(n):
        r = rd.random()  #Numero aleatorio entre 0 y 1
        if r <= p:
            x = x + 1
    return x

def factorial(n): #Mini funcion para calcular el factorial de un numero
    resultado = 1
    i = 1
    while i <= n:
        resultado = resultado * i
        i = i + 1
    return resultado

def contador(data):  #Cuenta la frecuencia de los elementos de la lista binomial
    global cero, uno, dos, tres, cuatro, cinco
    for i in range(len(data)):
        if data[i] == 0:
            cero += 1
        if data[i] == 1:
            uno += 1
        if data[i] == 2:
            dos += 1
        if data[i] == 3:
            tres += 1
        if data[i] == 4:
            cuatro += 1
        if data[i] == 5:
            cinco += 1

def calculoprobabilidad(xi): #Calcula la probabilidad de éxito
    x = 0
    suma = 0
    for i in range(len(xi)):
        vartemp = x * xi[i]
        suma = suma + vartemp
        x = x + 1
    return suma/500

def funcionbinomial(p, n): #Aplica la funcion de densidad binomial para calcular la probabilidad individual de cada evento
    pInvididual = []
    for i in range(6):
        x = (factorial(n)/(factorial(i)*factorial(n-i)))*p**i*(1-p)**(n-i)
        pInvididual.append(x)
    return pInvididual

def frecuenciaesperada(probabilidades): #Calcula la frecuencia esperada de cada evento
    esperada = []
    for i in range(len(probabilidades)):
        x = 100 * probabilidades[i]
        esperada.append(x)
    return esperada

def estadistico(xi, esperadas): #Calculo del estadistico de la prueba de bondad de ajuste
    suma = 0
    for i in range(6):
        x = ((xi[i] - esperadas[i])**2)/esperadas[i]
        suma = suma + x
    return suma

#Main
rep = 100
n = 5
p = 0.41
cero = 0
uno = 0
dos = 0
tres = 0
cuatro = 0
cinco = 0

data = []
for i in range(rep):  #Calcula una secuencias de numeros distribuidos binomialmente
    data.append(binomial(n, p))

count = (contador(data))
xi = [cero, uno, dos, tres, cuatro, cinco]
prob = calculoprobabilidad(xi)
probabilidades = funcionbinomial(prob, n)
esperadas = frecuenciaesperada(probabilidades)
chi = estadistico(xi, esperadas)

print("Los datos son: ", data)
print("La media aritmetica es: ", st.mean(data))
print("La probabilidad observada es: ", prob)
print("La frecuencia de cada numero es: ", xi)
print("Las probabilidades individuales esperadas son: ", probabilidades)
print("La frecuencia esperada de cada numero es: ", esperadas)
print("El estadistico es: ", chi)

sns.distplot(data, kde=False, color="b")
plt.show()

