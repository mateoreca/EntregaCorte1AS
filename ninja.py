class Ninja:
    def __init__(self, nombre, rango, ataque, defensa, chakra, jutsus=None):
        # Inicializa los atributos
        self.nombre = nombre
        self.rango = rango
        self.ataque = ataque
        self.defensa = defensa
        self.chakra = chakra
        self.jutsus = jutsus if jutsus else []

    def __str__(self):
        # Representación ninjas
        return (f"Ninja: {self.nombre} | Rango: {self.rango} | "
                f"Stats -> Ataque: {self.ataque}, Defensa: {self.defensa}, Chakra: {self.chakra} | "
                f"Jutsus: {', '.join(self.jutsus)}")

    def entrenar(self, inc_ataque=0, inc_defensa=0, inc_chakra=0):
        # Incrementa las estadísticas
        self.ataque += inc_ataque
        self.defensa += inc_defensa
        self.chakra += inc_chakra

    def combatir(self, otro):
        # Calcula el poder de combate y determina el ganador o empate
        poder_self = self.ataque + self.chakra - otro.defensa
        poder_otro = otro.ataque + otro.chakra - self.defensa
        if poder_self > poder_otro:
            return f"{self.nombre} gana el combate contra {otro.nombre}"
        elif poder_otro > poder_self:
            return f"{otro.nombre} gana el combate contra {self.nombre}"
        return "Empate en el combate"
