arreglo = []

# arregloCosas = [...]
arregloNUmeros = [1,2, 3, 4, 5, 6, 7, 8, 9]

# [0,3[

print (arregloNUmeros[0:5])
print (arregloNUmeros[3:5])
print (arregloNUmeros[:2])
print (arregloNUmeros[2:])
print (arregloNUmeros[-1])
print (arregloNUmeros[-2])
print (arregloNUmeros[3:-2])
print (arregloNUmeros[-5:-2])
print (arregloNUmeros[-2:-5])

print (7 in arregloNUmeros)
print (15 in arregloNUmeros)

print(len(arregloNUmeros))

arregloNUmeros.append(10)

print arregloNUmeros

arregloNUmeros.pop()
print arregloNUmeros

arregloNUmeros.pop(-3)

print arregloNUmeros

arregloNUmeros.insert(1,1.1)

print arregloNUmeros

del arregloNUmeros[1:4]

print arregloNUmeros