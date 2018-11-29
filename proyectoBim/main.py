import musica
import random


def crear_cancion_UI():
    nuevo = musica.Cancion()
    nuevo.song_id = ''.join(random.choice('abcde') for _ in range(3))
    nuevo.latitude = random.randint(-84, 84)
    nuevo.longitude = random.randint(-180, 180)
    artist_id = input("Ingrese el id del artista: ")
    artista = musica.Artist(artist_id)
    artista.buscar()
    if (artista.artist_name != None):
        nuevo.artist_id = artist_id
        nuevo.artist_name = artista.artist_name
        nuevo.artist_hotttnesss = artista.artist_hotttnesss
        nuevo.title = input("Ingrese el nombre de la canción: ")
        nuevo.terms = input("Ingrese el estilo musical: ")
        nuevo.year = input("Ingrese el año de  lanzamiento: ")
        nuevo.duration = input("Ingrese la duración de la canción(seg): ")
        nuevo.familiarity = input("¿Que tan familiar es la canción? [0 a 1]: ")
        nuevo.location = input("Ingrese el lugar de origen: ")
        nuevo.loudness = input("¿Que tan ruidosa es la canción? [0 a 1]: ")
        nuevo.similar = input("Ingrese el id de una canción similar: ")
        nuevo.song_hotttnesss = input("¿Que tan popular es la canción? [0 a 1]: ")
        nuevo.tempo = input("Ingrese el tempo: [0 a 200]: ")
        nuevo.crear()
    else:
        print('Artista no encontrado')


def mostrar_lista_canciones_UI():
    print("Lista de canciones:")
    cancion = musica.Cancion()
    cancion.listar(None, False)
    ordenar = True
    while (ordenar):
       respuesta = input("Desea ordenar la lista (Si/No): ")
       if (True if respuesta == "Si" else False):
           ordenar = True
           respuesta_orden = input("Como desea ordenar la lista? (A: ascendente/D: descendente): ")
           ascendente = False
           if (True if respuesta_orden == "A" else False):
               ascendente = True
               ordenar = False
           else:
               ascendente = False
               ordenar = True
           print("0) Popularidad")
           print("1) Ruido")
           print("2) Año")
           print("3) Popularidad del artista")
           print("4) Titulo")
           llave = input('Ingrese una llave a ordenar: ')
           def llaves(value):
               try:
                   return {
                       0: 'song_hotttnesss',
                       1: 'loudness',
                       2: 'year',
                       3: 'artist_hotttnesss',
                       4: 'title',
                   }[value]
               except KeyError:
                   print("Opción no definida")
           if (llave.isnumeric()):
               llave = int(llave)
               llave_a_ordennar = llaves(llave)
               cancion.listar(llave_a_ordennar, ascendente)
           else:
               ordenar = False
       else:
           ordenar = False

# mostar interfaz para la busqueda de datos
def buscar_cancion_UI():
    print("Búsqueda:")
    cancion = musica.Cancion()
    id = input("Ingrese el id de la canción: ")
    cancion.buscar(id)


# mostar interfaz para la eliminación de datos
def eliminar_cacion_UI():
    cancion = musica.Cancion()
    code = input("Ingrese el codigo de la canción a eliminar: ")
    cancion.eliminar(code)

# mostar interfax para la actualización de datos
def actualizar_cancion_UI():

    print("Actualización:")
    cancion = musica.Cancion()
    code = input("Ingrese el id de una canción: ")
    cancion_a_actualizar = cancion.leer(code)

    def opciones(value):
        try:
            return {
                0: 'artist_hotttnesss',
                1: 'artist_name',
                2: 'duration',
                3: 'familiarity',
                4: 'location',
                5: 'loudness',
                6: 'similar',
                7: 'song_hotttnesss',
                8: 'tempo',
                9: 'terms',
                10: 'title',
                11: 'year',
            }[value]
        except KeyError:
            print("Opción no definida")
    if not cancion_a_actualizar.empty:
        print("\nOpciones para actualizar:")
        print("0) Popularidad del artista")
        print("1) Nombre del artista")
        print("2) Duración")
        print("3) Familiaridad")
        print("4) Lugar")
        print("5) Nivel de ruido")
        print("6) ID canción similar")
        print("7) Popularidad")
        print("8) Tempo")
        print("9) Estilo")
        print("10) Título")
        print("11) Año")
        read = input("Ingrese una opción: ")
        if (read.isnumeric()):
            opcion_actualizar = int(read)
        try:
            llave_a_actualizar = opciones(opcion_actualizar)
            valor = input('Ingrese el nuevo valor: ')
            cancion_a_actualizar[llave_a_actualizar] = valor
            cancion.actualizar(cancion_a_actualizar)
        except TypeError:
            print(f'Option {option}')
    else:
        print(f"Registro con código {code} no existe")

# seleccionador de acciones principales
def acciones(value):
    cancion = musica.Cancion()
    try:
        return {
            0: None,
            1: crear_cancion_UI,
            2: buscar_cancion_UI,
            3: mostrar_lista_canciones_UI,
            4: actualizar_cancion_UI,
            5: eliminar_cacion_UI,
            6: cancion.filtrar,
        }[value]
    except KeyError:
        print("No existe esta acción")


# función principal
def main(option):
    while option != 0:
        print("\nThe Million Song Dataset:")
        print("1) Crear")
        print("2) Buscar")
        print("3) Ver lista")
        print("4) Actualizar")
        print("5) Eliminar")
        print("6) Crear datos filtrados")
        print("0) Salir")
        read = input("Ingrese una opción: ")
        if (read.isnumeric()):
            option = int(read)
        try:
            acciones(option)()
        except TypeError:
            print(f'Option {option}')

main(-1)

