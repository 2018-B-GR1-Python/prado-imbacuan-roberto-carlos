def hola_mundo():
	print("Hola mundo")

hola_mundo()

print(hola_mundo())


def sumar_dos_numeros(numero_uno, numero_dos):
    if(numero_uno == 1):
        return "Hola"
    else:
        return  numero_uno + numero_dos
    return  numero_uno + numero_dos

print(sumar_dos_numeros(1,2))

def imprimr_universidad(nombre_universidad = "EPN"):
    print(f"{nombre_universidad} es lo maximo")

imprimr_universidad()
imprimr_universidad("Salford")

def guardar_carros(posicion, placa, usuario, tip, color):
    print(f"Guardamos en {posicion} el auto con placa {placa} del usuario {usuario}")
    if(color):
        print(f"El color del carro es {color}")
    if(tip):
        print(f"Se recibio un tip de {tip}")

guardar_carros(tip=25.53,color="Amarillo", posicion=1, placa='123-abc',usuario="Adrian")
guardar_carros(1, '123-abc',"Adrian",tip=25.53,color="Amarillo")

# normales
# defecto or *


def sumar_numeros(resta, *numeros, valor_inicial=0):
    for numero in numeros:
        valor_inicial = valor_inicial + numero
    print(resta)
    print(numeros)
    print(valor_inicial)
    return valor_inicial - resta

resultado = sumar_numeros(1,1,2,3,4,5,4,3,2,5,2,4,5,5,2,valor_inicial= 10)
print(resultado)

sumar_numeros(1,1,2,3,4,5,6,7,8,9,0, valor_inicial= 10)
sumar_numeros(1,1,2,3,4,5,6,7,8,9,0)

# Paramentros *kwargs
def imprimit(**kwargs):
    print(f"{kwargs['primer_nombre']} {kwargs['segundo_nombre']} "
          f"{kwargs['apellido_paterno']} {kwargs['apellido_materno']}")

# imprimit("a", "b", "c", "d")
imprimit(primer_nombre="Vicente", segundo_nombre="Adraian", apellido_paterno="Eguez", apellido_materno="Sarzosa")


#numero = input("Ingrese un numero")print(float(numero) + 12.2 + 1)

# opcional = input("Desea papas con suorden, Opc: Si Opc: No")
# if(True if opcional == "Si" else False):
#   print("Truthy")
# else:
#   print("Falsy")

# numeros = input("Ingrese numeros: ")
# Proceso
# Recibir numeros separados
# 1) Rwcibir numeros -> Validar numeros y que este separados por comas
# 1.1) Sepearar por comas
# 1.2) sean numeros
# 2)
tupla = (1,2,3,4)
sumar_numeros(0,valor_inicial=0, *tupla)

def calculadora(numero_uno,numero_dos, opeacion="sumar"):
    def sumar_dos_numeros_c():
        return numero_uno + numero_dos
    def restar_dos_numeros():
        return numero_uno - numero_dos
    def multiplicar_dos_numeros():
        return  numero_uno * numero_dos
    def dividir_dos_numeros():
        return  numero_uno / numero_dos

    def switch(value):
        return {
            'sumar': sumar_dos_numeros_c(),
            'restar': restar_dos_numeros(),
            'mult': multiplicar_dos_numeros(),
            'div': dividir_dos_numeros(),
        }[value]
    return switch(opeacion)
print("Calculadora")
print(calculadora(1,2))
print(calculadora(1,2,"restar"))
print(calculadora(1,2,"mult"))
print(calculadora(1,1,"div"))

# Crear borrar actualizar buscar

# Leer archivos
def leer_Archivos(path):
    try:
        archivo = open(path)  # Defecto es 'r'
        arreglo_lienas_archivo = archivo.readlines()
        for linea in arreglo_lienas_archivo:
            print(linea)
        archivo.close()
    except Exception:
        print("leer: No se puede leer el archivo")

def agregar_a_archivo(path, *lineas_a_escribir):
    try:
        archivo = open(path, 'a')
        for linea in lineas_a_escribir:
            archivo.write("\n" + linea)
        archivo.close()
    except Exception:
        print("escribir: No se puede leer el archivo")


leer_Archivos('./08_ejemplo.txt')
agregar_a_archivo('./08_ejemplo.txt', "Hola esta es una nueva linea")

# Funciones lambda
elevar_al_cuadrado = lambda n: n * n
sumar_dos_numeros_v2 = lambda x,y: x + y

print(elevar_al_cuadrado(2))
print(sumar_dos_numeros(3,4))