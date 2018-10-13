tupla = (1,2,3, 2, 3, 3, "a", "c", "c")
print(tupla)

for numero in tupla:
    print(f"Numero {numero}")

print(tupla.index(3))

print(tupla.count(3))

print(tupla[0])

print(tupla[0:2])

print(set(tupla))

for t in set(tupla):
    print(f"Vaalor: {t}")