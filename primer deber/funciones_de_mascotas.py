import manejo_archivos
import transformaciones
def crear_mascota():
    print("Nueva mascota:")
    code = input("Ingrese un id: ")
    category = input("Ingrese una categoria: ")
    city = input("Ciudad: ")
    age = input("Ingrese una edad aproximada: ")
    color = input("Ingrese el color: ")
    description = input("Ingrese una descripcion del animal: ")
    pet = code + ";" + category + ";" + city + ";" + age + ";" + color + ';' + description + ';No rescatado'
    manejo_archivos.agregar_a_archivo('./pets.txt', 'a', pet)

def obtener_lista_mascotas():
    archivo_pets = manejo_archivos.leer_archivos('./pets.txt')
    mascotas = []
    for cadena in archivo_pets:
        mascotas.append(transformaciones.transformar_cadenatexto_a_diccionariomascota(cadena))
    return mascotas

def obtener_mascota_por_codigo(code):
    lista = obtener_lista_mascotas()
    for mascota in lista:
        if mascota.get('code') == code:
            break
    else:
        mascota = None
    return mascota

def guardar_listadediccionarios_como_listadecadenadetexto(lista):
    lista_cadenas = []
    for mascota in lista:
        cadena = transformaciones.transformar_diccioanriomascota_a_cadenatexto(mascota)
        lista_cadenas.append(cadena)
    manejo_archivos.agregar_a_archivo('./pets.txt', 'w', *lista_cadenas)

def remover_mascota_por_codigo(code):
    lista = obtener_lista_mascotas()
    mascota_a_remover = obtener_mascota_por_codigo(code)
    if mascota_a_remover != None:
        lista.remove(mascota_a_remover)
    print(f'Eliminando mascota con código {code}')
    guardar_listadediccionarios_como_listadecadenadetexto(lista)

def actualizar_mascota_por_diccionario(mascota, dato_actualizado):
    lista = obtener_lista_mascotas()
    index = lista.index(mascota)
    mascota.update(dato_actualizado)
    lista[index] = mascota
    print(f"Actualizando mascota con código {mascota['code']}")
    guardar_listadediccionarios_como_listadecadenadetexto(lista)