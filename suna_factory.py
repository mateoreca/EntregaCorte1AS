from ninja import Ninja

class SunaFactory:
    # Crea un objeto Ninja Gaara
    def crear_gaara(self):
        return Ninja(
            nombre="Gaara",
            rango="Kazekage",
            ataque=90,
            defensa=95,
            chakra=85,
            jutsus=["Sabaku Kyu", "Shukaku no Tate"]
        )

    # Crea un objeto Ninja Kankuro
    def crear_kankuro(self):
        return Ninja(
            nombre="Kankuro",
            rango="Jonin",
            ataque=70,
            defensa=65,
            chakra=75,
            jutsus=["Kugutsu no Jutsu", "Karasu"]
        )
