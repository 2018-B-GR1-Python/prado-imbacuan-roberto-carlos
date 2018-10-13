arregloNUmeros = [1,2, 3, 4, 5, 6, 7, 8, 9]

for numero in arregloNUmeros:
    print(numero)

for indice in range(1,5):
    print (f"Numero de iteración: {indice}")

for indice in range(3):
    print(f"Numero de iteración: {indice}")

for indice in range(7,10):
    print(f"Numero de iteración: {indice}")

for indice in range(10):
    if(indice == 6):
        break  # Detener la ejecución de esta iteración, el loop no continua
    print(f"Numero de iteración: {indice}")

for indice in range(10):
    if(indice == 6):
        continue  # Detener la ejecución de esta iteración, el loop continua
    if (indice == 4):
        continue  # Detener la ejecución de esta iteración, el loop continua
    print(f"Numero de iteración: {indice}")

numeroAuxiliar = 10
numeroAuxiliarDos = 10
while numeroAuxiliar < 10:
    print(f"NUmero: {numeroAuxiliar}")
    numeroAuxiliar += 1
    if numeroAuxiliarDos == 70:
        print(numeroAuxiliarDos)
