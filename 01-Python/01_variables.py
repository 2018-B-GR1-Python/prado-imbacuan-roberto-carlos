print "Hola mundo"

edad = 20
sueldo = 1.02
print edad + sueldo
print edad + int(sueldo)

nombre  = "Roberto"  # Comentario
apellido = 'Prado'
apellido_materno = """Imbacuan"""
print nombre
print apellido
print apellido_materno

print nombre == apellido  #  True / False
print apellido == apellido_materno  # True / False

print int(True)
print int(False)

print str(True)
print str(False)

print ("prado roberto".capitalize())  # Prado Roberto
print ("prado roberto".split())  # Prado Roberto

nombre_completo = "roberto prado".split(" ")

print (nombre_completo[0].capitalize() + " " + nombre_completo[1].capitalize())

print "Carlos".isalpha()
print "10".isdigit()  # isnumeric en versiones de python 3+ isdigit en 2.7
print "prado".isdigit()
print "Vicente10".isalnum()
print "10".isalnum()
#  print int("Vicente")
print "Mi nombre es {0} {1}".format(nombre_completo[0].capitalize(), "Roberto", "Prado")
# print (f"Mi nombre es {nombre_completo[0].capitalize()}" f"{nombre_completo[0].capitalize()}")

print (r"Saltos de linea ")
no_existe = None # Null
print no_existe





