import funciones_de_mascotas


def impirmir_encabezado_en_tablamascsotas():
    print('%-5s%-12s%-12s%-12s%-20s%-15s%-12s' % ('Cod', 'Categoria', 'Ciudad', 'Edad(aprox)', 'Color', 'Estado', 'Descripción'))


def imprimir_fila_en_tablamascota(mascota):
    print('%(code)-5s%(category)-12s%(city)-12s%(age)-12s%(color)-20s%(state)-15s%(description)-12s' % mascota)


def mostrar_lista_mascotas():
    print("Lista de mascotas:")
    lista = funciones_de_mascotas.obtener_lista_mascotas()
    impirmir_encabezado_en_tablamascsotas()
    for mascota in lista:
        imprimir_fila_en_tablamascota(mascota)
    ordenar = True
    while (ordenar):
       respuesta = input("Desea ordenar la lista (Si/No): ")
       if (True if respuesta == "Si" else False):
           ordenar = True
           respuesta_orden = input("Coomo desea ordenar la lista? (A: ascendente/D: descendente): ")
           if (True if respuesta_orden == "A" else False):
               ordenar = False
           else:
               ordenar = True
           print("0) Código")
           print("1) Categoria")
           print("2) Ciudad")
           print("3) Edad")
           print("4) Color")
           print("5) Estado")
           print("6) Descripción")
           llave = input('Ingrese una llave a ordenar: ')
           def llaves(value):
               try:
                   return {
                       0: 'code',
                       1: 'category',
                       2: 'city',
                       3: 'age',
                       4: 'color',
                       5: 'state',
                       6: 'description'
                   }[value]
               except KeyError:
                   print("Opción no definida")
           if (llave.isnumeric()):
               llave = int(llave)
               llave_a_ordennar = llaves(llave)
               def sortBy(elem):
                   return elem[llave_a_ordennar]
               impirmir_encabezado_en_tablamascsotas()
               lista.sort(key=sortBy, reverse=ordenar)
               for mascota in lista:
                   imprimir_fila_en_tablamascota(mascota)
           else:
               ordenar = False
       else:
           ordenar = False

# mostar interfaz para la busqueda de datos
def buscar_mascota():
    print("Búsqueda de mascota:")
    code = input("Ingrese el codigo de mascota a buscar: ")
    mascota = funciones_de_mascotas.obtener_mascota_por_codigo(code)
    if mascota != None:
        impirmir_encabezado_en_tablamascsotas()
        imprimir_fila_en_tablamascota(mascota)
    else:
        print(f"Mascota con código {code} no existe")


# mostar interfaz para la eliminación de datos
def eliminar_mascota():
    print("Eliminar mascota:")
    code = input("Ingrese el codigo de mascota a eliminar: ")
    funciones_de_mascotas.remover_mascota_por_codigo(code)

# mostar interfax para la actualización de datos
def actualizar_mascota():
    print("Actualización de mascota:")
    code = input("Ingrese el codigo de mascota a actualizar: ")
    mascota = funciones_de_mascotas.obtener_mascota_por_codigo(code)
    def opciones(value):
        try:
            return {
                0: 'category',
                1: 'city',
                2: 'age',
                3: 'color',
                4: 'state',
                5: 'description'
            }[value]
        except KeyError:
            print("Opción no definida")
    if mascota != None:
        impirmir_encabezado_en_tablamascsotas()
        imprimir_fila_en_tablamascota(mascota)
        print("\nOpciones:")
        print("0) Actualizar categoria")
        print("1) Actualizar ciudad")
        print("2) Actualizar edad")
        print("3) Actualizar color")
        print("4) Actualizar estado")
        print("5) Actualizar descripción")
        read = input("Ingrese una opción: ")
        if (read.isnumeric()):
            opcion_actualizar = int(read)
        try:
            llave_a_actualizar = opciones(opcion_actualizar)
            valor = input('Ingrese el nuevo valor: ')
            dato_a_actualizar = {
                llave_a_actualizar: valor
            }
            funciones_de_mascotas.actualizar_mascota_por_diccionario(mascota, dato_a_actualizar)
        except TypeError:
            print(f'Option {option}')
    else:
        print(f"Mascota con código {code} no existe")

# seleccionador de acciones principales
def acciones(value):
    try:
        return {
            0: None,
            1: funciones_de_mascotas.crear_mascota,
            2: mostrar_lista_mascotas,
            3: buscar_mascota,
            4: eliminar_mascota,
            5: actualizar_mascota
        }[value]
    except KeyError:
        print("No existe esta acción")

# función principal
def main(option):
    while option != 0:
        print("\nOpciones:")
        print("1) Ingresar una mascota")
        print("2) Obtener lista de mascotas")
        print("3) Buscar mascota")
        print("4) Eliminar mascota")
        print("5) Actualizar mascota")
        print("0) Salir")
        read = input("Ingrese una opción: ")
        if (read.isnumeric()):
            option = int(read)
        try:
            acciones(option)()
        except TypeError:
            print(f'Option {option}')

main(-1)

