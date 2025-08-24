# Importa utilidades del sistema operativo para obtener la ruta absoluta al exportar
import os
# Fábricas concretas para crear ninjas predefinidos de Konoha y Suna
from konoha_factory import KonohaFactory
from suna_factory import SunaFactory
# Builder para crear ninjas personalizados paso a paso
from ninja_builder import NinjaBuilder
# Visitor para exportar la información a TXT y JSON
from visitor import ExportVisitor
# Clase que representa misiones con rango, recompensa y requisito
from mision import Mision

# Contenedor global ninjas
ninjas = []
# Conjunto de misiones
misiones = [
    Mision("Rescate", "B", 300, "Chunin"),
    Mision("Defensa de tu pueblo", "A", 500, "Jonin"),
]

def menu():
    # Muestra el menú principal
    print("\n===== MENÚ PRINCIPAL =====")
    print("1. Crear ninja (Factory)")
    print("2. Crear ninja personalizado (Builder)")
    print("3. Listar ninjas")
    print("4. Simular combate")
    print("5. Entrenar ninja")
    print("6. Exportar datos (TXT y JSON)")
    print("7. Salir")
    return input("Seleccione una opción: ")

def crear_ninja_factory():
    # Crea un ninja predefinido usando fábricas concretas y evita duplicados por nombre
    print("\n--- Crear Ninja con Factory ---")
    print("1. Naruto (Konoha)")
    print("2. Kakashi (Konoha)")
    print("3. Gaara (Suna)")
    print("4. Kankuro (Suna)")
    opcion = input("Seleccione una opción: ")

    # Variables auxiliares para la selección
    factory = None
    nuevo_ninja = None

    # Instancia la fabrica y crea ninja
    if opcion == "1":
        factory = KonohaFactory()
        nuevo_ninja = factory.crear_naruto()
    elif opcion == "2":
        factory = KonohaFactory()
        nuevo_ninja = factory.crear_kakashi()
    elif opcion == "3":
        factory = SunaFactory()
        nuevo_ninja = factory.crear_gaara()
    elif opcion == "4":
        factory = SunaFactory()
        nuevo_ninja = factory.crear_kankuro()
    else:
        # Opcion inválida
        print("Opción no válida.")
        return

    # Verificación de duplicados
    if any(ninja.nombre == nuevo_ninja.nombre for ninja in ninjas):
        print(f"El ninja {nuevo_ninja.nombre} ya está en la lista.")
    else:
        ninjas.append(nuevo_ninja)
        print(f"Ninja {nuevo_ninja.nombre} creado correctamente.")

def crear_ninja_builder():
    # Construye un ninja personalizado
    print("\n--- Crear Ninja Personalizado ---")
    nombre = input("Nombre: ")

    # Evita crear dos ninjas con el mismo nombre 
    if any(ninja.nombre.lower() == nombre.lower() for ninja in ninjas):
        print(f"El ninja {nombre} ya existe. Elige otro nombre.")
        return

    # Ingreso atributos
    rango = input("Rango (Genin, Chunin, Jonin): ")
    ataque = int(input("Ataque: "))
    defensa = int(input("Defensa: "))
    chakra = int(input("Chakra: "))

    # Configuración del builder
    builder = NinjaBuilder()
    builder.set_nombre(nombre).set_rango(rango).set_stats(ataque, defensa, chakra)

    # Bucle o fin
    while True:
        jutsu = input("Agregar jutsu (o 'fin' para terminar): ")
        if jutsu.lower() == "fin":
            break
        builder.add_jutsu(jutsu)

    # Crea el ninja y lo guarda
    ninjas.append(builder.build())
    print(f"Ninja {nombre} creado correctamente.")

def listar_ninjas():
    # Muestra los ninjas creados
    print("\n--- Lista de Ninjas ---")
    if not ninjas:
        print("No hay ninjas creados.")
        return
    for i, n in enumerate(ninjas, start=1):
        print(f"{i}. {n}")

def simular_combate():
    # Permite seleccionar dos ninjas existentes y muestra el resultado del combate
    listar_ninjas()
    if len(ninjas) < 2:
        # Se requiere al menos dos ninjas para combatir
        print("Debes tener al menos dos ninjas para simular combate.")
        return
    try:
        # Selección por índice
        idx1 = int(input("Seleccione el número del primer ninja: ")) - 1
        idx2 = int(input("Seleccione el número del segundo ninja: ")) - 1
        if idx1 == idx2:
            # Evita enfrentar el mismo ninja contra sí mismo
            print("No puedes pelear el mismo ninja.")
            return
        # Metodo para simular lucha
        print(ninjas[idx1].combatir(ninjas[idx2]))
    except (ValueError, IndexError):
        # Control de entradas
        print("Selección inválida.")

def entrenar_ninja():
    # Incrementa estadísticas de un ninja
    listar_ninjas()
    if not ninjas:
        return
    try:
        # Selección del ninja a entrenar
        idx = int(input("Seleccione el número del ninja a entrenar: ")) - 1
        # Incrementos a aplicar
        ataque = int(input("Incremento de ataque: "))
        defensa = int(input("Incremento de defensa: "))
        chakra = int(input("Incremento de chakra: "))
        # Aplica el entrenamiento mediante el método del objeto
        ninjas[idx].entrenar(ataque, defensa, chakra)
        print(f"{ninjas[idx].nombre} entrenado correctamente.")
    except (ValueError, IndexError):
        # Maneja errores de entrada o selección inválida
        print("Selección inválida.")

def exportar_datos():
    # Exporta ninjas y misiones a TXT y JSON; informa la ruta absoluta de salida
    visitor = ExportVisitor()
    visitor.exportar_txt(ninjas, misiones)
    visitor.exportar_json(ninjas, misiones)
    ruta = os.path.abspath(".")
    print("\n=== EXPORTACIÓN COMPLETA ===")
    print(f"Archivos generados en:\n{ruta}\\export.txt\n{ruta}\\export.json")

if __name__ == "__main__":
    # Bucle menu principal
    while True:
        opcion = menu()
        if opcion == "1":
            crear_ninja_factory()
        elif opcion == "2":
            crear_ninja_builder()
        elif opcion == "3":
            listar_ninjas()
        elif opcion == "4":
            simular_combate()
        elif opcion == "5":
            entrenar_ninja()
        elif opcion == "6":
            exportar_datos()
        elif opcion == "7":
            # Finaliza la aplicación
            print("Fin")
            break
        else:
            # Mensaje para opciones no válidas
            print("Opción inválida, intente de nuevo.")