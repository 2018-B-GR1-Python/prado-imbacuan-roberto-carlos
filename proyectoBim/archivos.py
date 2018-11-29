import json


# 1) Ingresar un registro
def leer_json(path):
    try:
        json_data = open(path).read()
        data = json.loads(json_data)
        return data
    except Exception as e:
        print("No se puede leer el archivo: " + e)
        return []
