#Generador Van Neuman
def midSquare(seed, n):
    list = []
    d = "0."
    for i in range(n):
        nro = seed * seed
        nro = str(nro).zfill(8) # Rellena el int con 0 si tiene menos de 8 digitos
        nro = nro[2:6] # Saca los 4 digitos del medio
        u = float(str(d) + nro)  # Una negrada pero no encontraba otra solucion
        list.append(u)
        nro = int(nro)
        seed = nro
    return list

seed = int(input("Ingrese un seed: ")) # Ingresar numero de 4 digitos
n = int(input("Ingrese un n: "))
list = midSquare(seed, n)
for x in range (len(list)):
    print(list[x])

# A simple vista se puede ver que no es un buen generador puesto que al caer un 0, este se propaga para siempre.
# Tambien observamos que con ciertas semillas se repite una secuencia de numeros infinitamente. Probar con 5436 y 9547
