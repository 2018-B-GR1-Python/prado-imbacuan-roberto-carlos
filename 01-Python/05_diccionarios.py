adrian = {
    "nombre": "Adrian",
    'apellido': 'Eguez',
    "edad": 29,
    "casado": False,
    "mascota": {
        "nombre": "cachetes"
    }
}
print(adrian["nombre"])
print(adrian["mascota"]["nombre"])
print(adrian.get("apellido"))
print(adrian.pop("casado"))
print(adrian)
print(adrian.values())

for valor in  adrian.values():
    print(f"Valor: {valor}")

for llave in adrian.keys():
    print(f"LLave: {llave} valor: {adrian.get(llave)}")

for clave, valor in adrian.items():
    print(f"clave: {clave} valor: {valor}")

adrian["profesor"] = "Maestro"
print(adrian)
adrian.update({"peso":0,"altura":1})
