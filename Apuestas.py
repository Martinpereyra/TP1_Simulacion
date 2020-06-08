import random
import matplotlib.pyplot as plt


def rollRuleta():
    random.seed()
    roll = random.randint(0, 36)

    if roll == 0:
        return False
    elif (roll % 2) != 0:
        return False
    elif (roll % 2) == 0:
        return True


def apuesta_simple(fondos, apuesta_inicial, numero_apuestas):
    global contador_quiebra_simple, profit_simple, contador_profit_simple
    value = fondos
    apuesta = apuesta_inicial
    wX = []
    vY = []
    apuestaActual = 1
    while apuestaActual <= numero_apuestas:
        if rollRuleta():
            value += apuesta
            wX.append(apuestaActual)
            vY.append(value)

        else:
            value -= apuesta
            wX.append(apuestaActual)
            vY.append(value)

            if value <= 0:
                contador_quiebra_simple += 1
                break

        apuestaActual += 1
    profit_simple += value
    if value < fondos:
        color = 'r'
    else:
        color = 'g'
        contador_profit_simple += 1
    plt.plot(wX, vY, color, linewidth=0.5)


def apuesta_martingala(fondos, apuesta_inicial, numero_apuestas):
    global contador_quiebra_martingala, profit_martingala, contador_profit_martingala
    value = fondos
    wX = []
    vY = []
    apuestaActual = 1
    apuestaPrevia = 'win'
    cantidadApuestaPrevia = apuesta_inicial

    while apuestaActual <= numero_apuestas:
        if apuestaPrevia == 'win':
            apuesta = cantidadApuestaPrevia  # add
            if rollRuleta():
                value += apuesta
                wX.append(apuestaActual)
                vY.append(value)
            else:
                value -= apuesta
                apuestaPrevia = 'loss'
                cantidadApuestaPrevia = apuesta
                wX.append(apuestaActual)
                vY.append(value)
                if value <= 0:
                    contador_quiebra_martingala += 1
                    break
        elif apuestaPrevia == 'loss':
            apuesta = cantidadApuestaPrevia * 2  # add
            if (value - apuesta) < 0:
                apuesta = value
            if rollRuleta():
                value += apuesta
                cantidadApuestaPrevia = apuesta_inicial
                apuestaPrevia = 'win'
                wX.append(apuestaActual)
                vY.append(value)
            else:
                value -= apuesta
                apuestaPrevia = 'loss'
                cantidadApuestaPrevia = apuesta
                wX.append(apuestaActual)
                vY.append(value)
                if value <= 0:
                    contador_quiebra_martingala += 1
                    break

        apuestaActual += 1
    profit_martingala += value
    if value < fondos:
        color = 'r'
    else:
        color = 'g'
        contador_profit_martingala += 1
    plt.plot(wX, vY, color, linewidth=0.5)


def dAlembert(fondos, apuesta_inicial, numero_apuestas):
    global contador_quiebra_dalembert, profit_dalembert, contador_profit_dalembert
    value = fondos
    wX = []
    vY = []
    apuestaActual = 1
    apuestaAnterior = 'win'
    cantidadApuestaPrevia = apuesta_inicial

    while apuestaActual <= numero_apuestas:

        if apuestaAnterior == 'win':
            apuesta =  cantidadApuestaPrevia - apuesta_inicial
            if apuesta <= 0:
                apuesta = apuesta_inicial
            if rollRuleta():
                value += apuesta

                wX.append(apuestaActual)
                vY.append(value)
            else:
                apuestaAnterior = 'loss'
                value -= apuesta
                wX.append(apuestaActual)
                vY.append(value)
                if value <= 0:
                    contador_quiebra_dalembert += 1
                    break
            cantidadApuestaPrevia = apuesta
        elif apuestaAnterior == 'loss':
            apuesta = cantidadApuestaPrevia + apuesta_inicial
            if value - apuesta < 0:
                apuesta = value
            if rollRuleta():
                apuestaAnterior = 'win'
                value += apuesta
                wX.append(apuestaActual)
                vY.append(value)
            else:
                value -= apuesta
                wX.append(apuestaActual)
                vY.append(value)
                if value <= 0:
                    contador_quiebra_dalembert += 1
                    break
            cantidadApuestaPrevia = apuesta

        apuestaActual += 1
    profit_dalembert += value
    if value < fondos:
        color = 'r'
    else:
        color = 'g'
        contador_profit_dalembert += 1
    plt.plot(wX, vY, color, linewidth=0.5)






# MAIN SECTION

numero_apostadores = 1000
maximo_apuestas = 60
fondo_inicial = 10000
valor_apuesta = 1000

#print("Beneficio del casino usando apuesta simple",((fondo_inicial*numero_apostadores) - profit_simple)*0.00001,'%')
# APUESTA SIMPLE

contador_quiebra_simple = 0
contador_profit_simple = 0
profit_simple = 0
y = 0
while y < numero_apostadores:
    apuesta_simple(fondo_inicial, valor_apuesta, maximo_apuestas)
    y += 1

print('Probabilidad de quiebra apuesta simple:', (contador_quiebra_simple / float(y)) * 100,'%')
print('Probabilidad de obtener beneficio utilizando apuesta simple:', (contador_profit_simple / float(y)) * 100,'%')
print("Beneficio del casino usando apuesta simple2",((fondo_inicial*numero_apostadores) - profit_simple)*0.00001,'%')
print('_________________________________________________________________________________')
plt.axhline(fondo_inicial, color='r')
plt.ylabel('Fondos')
plt.xlabel('Numero de apuesta')
plt.title('Estrategia Apuesta simple')
plt.show()

# APOSTANDO CON MARTINGALA

contador_quiebra_martingala = 0
contador_profit_martingala = 0
profit_martingala = 0
x = 0
while x < numero_apostadores:
    apuesta_martingala(fondo_inicial, valor_apuesta, maximo_apuestas)
    x += 1

print('Probabilidad de quiebra utlizando martingala:', (contador_quiebra_martingala / float(x)) * 100)
print('Probabilidad de obtener beneficio utilizando martingala:', (contador_profit_martingala / float(x)) * 100)
print("Beneficio del casino usando Martingala",((fondo_inicial*numero_apostadores) - profit_martingala)*0.00001,'%')
print('_________________________________________________________________________________')
plt.axhline(fondo_inicial, color='r')
plt.ylabel('Fondos')
plt.xlabel('Numero de apuesta')
plt.title('Estrategia Martingala')
plt.show()




# APOSTANDO CON D'ALEMBERT

contador_quiebra_dalembert = 0
contador_profit_dalembert = 0
profit_dalembert = 0
z = 0
while z < numero_apostadores:
    dAlembert(fondo_inicial,valor_apuesta,maximo_apuestas)
    z+=1

print('Probabilidad de quiebra dAlembert:', (contador_quiebra_dalembert / float(z)) * 100)
print('Probabilidad de obtener beneficio utilizando DAlembert:', (contador_profit_dalembert / float(z)) * 100)
print("Beneficio del casino usando DAlembert",((fondo_inicial*numero_apostadores) - profit_dalembert)*0.00001,'%')
print('_________________________________________________________________________________')
plt.axhline(fondo_inicial, color='r')
plt.ylabel('Fondos')
plt.xlabel('Numero de apuesta')
plt.title('Estrategia DAlembert')
plt.show()