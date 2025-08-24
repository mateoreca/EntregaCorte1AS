# Importa la clase base Ninja para crear instancias con los atributos requeridos
from ninja import Ninja

class KonohaFactory:
    # Método que crea un objeto Ninja con los atributos específicos de Naruto Uzumaki
    def crear_naruto(self):
        return Ninja(
            nombre="Naruto Uzumaki",       # Nombre del ninja
            rango="Genin",                 # Rango de Naruto
            ataque=75,                     # Nivel de ataque
            defensa=60,                    # Nivel de defensa
            chakra=100,                    # Nivel de chakra
            jutsus=["Rasengan", "Kage Bunshin no Jutsu"]  # Lista de jutsus característicos
        )

    # Método que crea un objeto Ninja con los atributos específicos de Kakashi Hatake
    def crear_kakashi(self):
        return Ninja(
            nombre="Kakashi Hatake",       # Nombre del ninja
            rango="Jonin",                 # Rango de Kakashi
            ataque=85,                     # Nivel de ataque
            defensa=70,                    # Nivel de defensa
            chakra=90,                     # Nivel de chakra
            jutsus=["Chidori", "Sharingan", "Raikiri"]  # Lista de jutsus característicos
        )
