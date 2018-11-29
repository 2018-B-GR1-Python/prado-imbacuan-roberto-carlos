def transformar_cadenatexto_a_diccionariomascota(linea):
    partes_linea = (linea + "").replace("\n", "").split(';')
    mascota = {
        'code': partes_linea[0],
        'category': partes_linea[1],
        'city': partes_linea[2],
        'age': int(partes_linea[3]),
        'color': partes_linea[4],
        'state': partes_linea[6],
        'description': partes_linea[5]
    }
    return mascota

def transformar_diccioanriomascota_a_cadenatexto(mascota):
    return f"{mascota['code']};{mascota['category']};{mascota['city']};{mascota['age']};{mascota['color']};{mascota['description']};{mascota['state']}"