class Mision:
    # Constructor de la clase Mision
    # nombre, rango asignado, recompensa en puntos o dinero, y rango mínimo requerido del ninja
    def __init__(self, nombre, rango, recompensa, requisito_rango):
        self.nombre = nombre                  # Nombre de la misión (ejemplo: "Rescate")
        self.rango = rango                    # Rango de dificultad de la misión (ejemplo: "A", "B", "S")
        self.recompensa = recompensa          # Recompensa de la misión (valor numérico)
        self.requisito_rango = requisito_rango  # Rango mínimo que debe tener el ninja para realizarla

    # Representación en texto de la misión para mostrarla en listados o exportaciones
    def __str__(self):
        return f"Misión: {self.nombre} | Rango: {self.rango} | Recompensa: {self.recompensa}"
