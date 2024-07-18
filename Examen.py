import random
import csv
import statistics
import math

lista_trabajadores = ["Juan Perez", "Maria Garcia", "Carlos Lopez", "Ana Martinez", "Pedro Rodriguez", "Laura Herandez", "Miguel Sanchez", "Isabel Gomez", "Francisco Diaz", "Elena Fernandez"]
sueldos = []

def sueldos_empleados_aleatorios():
    global sueldos
    sueldos = [random.randint(300000, 2500000) for _ in lista_trabajadores]
    print("Sueldos asignados correctamente.")

def clasificador_sueldos():
    if not sueldos:
        print("Asigne los sueldos")
        return

    sueldos_menores_800k = [(lista_trabajadores[i], sueldos[i]) for i in range(len(sueldos)) if sueldos[i] < 800000]
    sueldos_entre_800k_y_2000k = [(lista_trabajadores[i], sueldos[i]) for i in range(len(sueldos)) if 800000 <= sueldos[i] <= 2000000]
    sueldos_superiores_2000k = [(lista_trabajadores[i], sueldos[i]) for i in range(len(sueldos)) if sueldos[i] > 2000000]

    print("Sueldos menores a $800.000")
    for nombre_trabajador, sueldo in sueldos_menores_800k:
        print(f"{nombre_trabajador}: ${sueldo}")
    print("Total:", len(sueldos_menores_800k))

    print("\nSueldos entre $800.000 y $2.000.000")
    for nombre_trabajador, sueldo in sueldos_entre_800k_y_2000k:
        print(f"{nombre_trabajador}: ${sueldo}")
    print("Total:", len(sueldos_entre_800k_y_2000k))

    print("\nSueldos superiores a $2.000.000")
    for nombre_trabajador, sueldo in sueldos_superiores_2000k:
        print(f"{nombre_trabajador}: ${sueldo}")
    print("Total:", len(sueldos_superiores_2000k))

def ver_estadisticas():
    if not sueldos:
        print("Primero asigne los sueldos.")
        return

    sueldo_alto = max(sueldos)
    sueldo_bajo = min(sueldos)
    promedio = sum(sueldos) / len(sueldos)
    media_geometrica = math.exp(sum(math.log(s) for s in sueldos) / len(sueldos))

    print(f"Sueldo más alto: ${sueldo_alto}")
    print(f"Sueldo más bajo: ${sueldo_bajo}")
    print(f"Promedio de sueldos: ${promedio:.2f}")
    print(f"Media geométrica de sueldos: ${media_geometrica:.2f}")

def reporte_sueldos():
    if not sueldos:
        print("Primero debe asignar los sueldos.")
        return
    
    with open("reporte_sueldos.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Nombre empleado", "Sueldo base", "Descuento salud", "Descuento AFP", "Sueldo líquido"])

        for i in range(len(lista_trabajadores)):
            sueldo_base = sueldos[i]
            Descuento_salud = sueldo_base * 0.07
            Descuento_AFP = sueldo_base * 0.12
            Sueldo_liquido = sueldo_base - Descuento_salud - Descuento_AFP
            writer.writerow([lista_trabajadores[i], sueldo_base, Descuento_salud, Descuento_AFP, Sueldo_liquido])
    
    print("Reporte generado correctamente.")

def mostrar_menu():
    print("\n==== MENU ====")
    print("1. Asignar sueldos aleatorios")
    print("2. Clasificar sueldos")
    print("3. Ver estadísticas")
    print("4. Reporte de sueldos")
    print("5. Salir del programa")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            sueldos_empleados_aleatorios()
        elif opcion == "2":
            clasificador_sueldos()
        elif opcion == "3":
            ver_estadisticas()
        elif opcion == "4":
            reporte_sueldos()
        elif opcion == "5":
            print("Finalizando programa...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()
