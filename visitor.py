import json

class ExportVisitor:
    # Exporta los datos de ninjas y misiones a un archivo TXT
    def exportar_txt(self, ninjas, misiones, filename="export.txt"):
        with open(filename, "w", encoding="utf-8") as f:
            f.write("=== NINJAS ===\n")
            for n in ninjas:
                f.write(str(n) + "\n")  # Escribe cada ninja como texto
            f.write("\n=== MISIONES ===\n")
            for m in misiones:
                f.write(str(m) + "\n")  # Escribe cada misión como texto

    # Exporta los datos de ninjas y misiones a un archivo JSON
    def exportar_json(self, ninjas, misiones, filename="export.json"):
        data = {
            "ninjas": [n.__dict__ for n in ninjas],   # Convierte los ninjas en diccionarios
            "misiones": [m.__dict__ for m in misiones]  # Convierte las misiones en diccionarios
        }
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)  # Guarda el archivo en formato legible
