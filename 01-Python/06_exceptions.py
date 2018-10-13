adrian = {
    "nombre": "Adrian"
}
arregloNumeros = [1,2]
try:
    adrian["nombre"] = 1
    adrian["apellidp"]
    arregloNumeros.append(2.2)
    arregloNumeros["1"] = 0
except KeyError:
    print("Error in key")
except TypeError:
    print("Type error")
try:
    arregloNumeros["1"] = 0
except Exception as e:
    print("Error: ", e.with_traceback())