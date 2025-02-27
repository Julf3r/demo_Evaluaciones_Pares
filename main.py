import csv
import os

archivo_csv = "datos_estudiantes.csv"

def agregar_estudiante():
    nombre = input("Nombre del estudiante: ")
    edad = input("Edad: ")
    carrera = input("Carrera: ")

    with open(archivo_csv, mode="a+", newline="", encoding="utf-8") as archivo:
        archivo.seek(0)  # Mover el cursor al inicio para leer si hay encabezados
        lector = csv.reader(archivo)
        tiene_encabezados = any(lector)  # Verifica si el archivo tiene datos

        escritor = csv.writer(archivo)
        if not tiene_encabezados:
            escritor.writerow(["Nombre", "Edad", "Carrera"])  # Escribir encabezados solo si no existen

        escritor.writerow([nombre, edad, carrera])

    print("Información guardada con éxito.")

def buscar_estudiante():
    if not os.path.exists(archivo_csv):
        print("No hay datos registrados aún.")
        return

    nombre_buscar = input("Ingrese su nombre para buscar su información: ")

    with open(archivo_csv, mode="r", encoding="utf-8") as archivo:
        lector = csv.reader(archivo)
        encabezados = next(lector, None)  # Leer los encabezados si existen

        encontrado = False
        for fila in lector:
            if fila[0] == nombre_buscar:  # Buscar por nombre
                print("\nInformación encontrada:")
                print(f"{encabezados[0]}: {fila[0]}")
                print(f"{encabezados[1]}: {fila[1]}")
                print(f"{encabezados[2]}: {fila[2]}")
                encontrado = True
                break

        if not encontrado:
            print("No se encontró información para ese nombre.")

# Menú principal
while True:
    print("\n1. Agregar estudiante")
    print("2. Buscar estudiante")
    print("3. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        agregar_estudiante()
    elif opcion == "2":
        buscar_estudiante()
    elif opcion == "3":
        print("Saliendo...")
        break
    else:
        print("Opción no válida. Intente de nuevo.")
