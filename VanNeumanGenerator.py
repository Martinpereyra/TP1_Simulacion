#Generador Van Neuman
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

seed = int(input("Ingrese un seed: ")) # Ingresar numero de 4 digitos
n = int(input("Ingrese un n: "))
list = midSquare(seed, n)

for x in range (len(list)):
    print(list[x])

# A simple vista se puede ver que no es un buen generador puesto que al caer un 0, este se propaga para siempre.

