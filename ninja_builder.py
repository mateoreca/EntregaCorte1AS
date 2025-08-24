from ninja import Ninja

class NinjaBuilder:
    def __init__(self):
        # Inicializa atributos
        self.nombre = None
        self.rango = None
        self.ataque = 0
        self.defensa = 0
        self.chakra = 0
        self.jutsus = []

    def set_nombre(self, nombre):
        # Asigna el nombre del ninja
        self.nombre = nombre
        return self  # Permite encadenar métodos

    def set_rango(self, rango):
        # Asigna el rango del ninja
        self.rango = rango
        return self

    def set_stats(self, ataque, defensa, chakra):
        # Asigna valores base de ataque, defensa y chakra
        self.ataque = ataque
        self.defensa = defensa
        self.chakra = chakra
        return self

    def add_jutsu(self, jutsu):
        # Agrega un jutsu a la lista
        self.jutsus.append(jutsu)
        return self

    def build(self):
        # Crea y devuelve
        return Ninja(self.nombre, self.rango, self.ataque, self.defensa, self.chakra, self.jutsus)
