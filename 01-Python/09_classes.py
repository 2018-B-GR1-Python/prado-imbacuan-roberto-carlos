


class Escuela:

    #valor_categoria = 4
    __ciudad = 'Quito'  # atr private
    pais = 'Ecuador'  #  atr public

    def __init__(self, nombre, valor_categoria = 4):
        print(self)
        print('Hola constructor')
        self.nombre = nombre
        self.valor_categoria = valor_categoria

    def saludar(self):
        print(f'Hola desde {self.nombre} localizada en {self.__ciudad} - {self.pais}')

    def categoria(self):
        return self.valor_categoria * 3

twa = Escuela('EPN')
twa.valor_categoria = 2
print(twa)

twa.saludar()
print(twa.categoria())

class Auto:

    _ensamblado = 'Quito'
    numero_asientos = 5

    def __init__(self, nomnbre,color):
        self.nombre = nomnbre
        self.color = color

    def __init__(self, nombre, color, color_techo = ''):
        self.nombre = nombre
        self.color = color
        self.colo_techo = color_techo

    def cambiar_ensamblado(self, ensamblado):
        self._ensamblado = ensamblado

    def __maximo_numero_pssajeros(self):
        return self.numero_asientos + 3

    def __str__(self):
        return (f"{self.nombre}"
                f"{self.color}"
                f"{self.numero_asientos}"
                f"{self._ensamblado}"
                f"{self.__maximo_numero_pssajeros()}")
bmw = Auto('Blanco', 'Version 1')
print(bmw)


class Hyundai(Auto):
    def __init__(self, color, nombre):
        super().__init__(nombre, color)
        print('construcotr')
        print(self._ensamblado)

mi_carro = Hyundai('Negro', 'Santa fe')
print(mi_carro)