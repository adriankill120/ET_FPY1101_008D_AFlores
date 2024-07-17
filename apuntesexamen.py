import random  # Importamos la biblioteca random para generar números aleatorios
import statistics  # Importamos la biblioteca statistics para cálculos estadísticos
from math import prod  # Importamos la función prod del módulo math para calcular productos

# Generando números aleatorios
print("Generando números aleatorios:")

# Generar un número flotante aleatorio entre 0.0 y 1.0
numero_aleatorio = random.random()
print(f"Número aleatorio entre 0.0 y 1.0: {numero_aleatorio}")

# Generar un número entero aleatorio entre 1 y 100
numero_entero = random.randint(1, 100)
print(f"Número entero aleatorio entre 1 y 100: {numero_entero}")

# Elegir un elemento aleatorio de una lista
lista = ['a', 'b', 'c', 'd']
elemento_aleatorio = random.choice(lista)
print(f"Elemento aleatorio de la lista: {elemento_aleatorio}")

# Reordenar aleatoriamente una lista (modifica la lista original)
random.shuffle(lista)
print(f"Lista reordenada aleatoriamente: {lista}")

# Cálculos estadísticos
print("\nRealizando cálculos estadísticos:")

data = [10, 20, 30, 40, 50]

# Calcular el promedio de los datos
promedio = statistics.mean(data)
print(f"Promedio de los datos: {promedio}")

# Calcular la mediana de los datos
mediana = statistics.median(data)
print(f"Mediana de los datos: {mediana}")

# Calcular la desviación estándar de los datos
desviacion_estandar = statistics.stdev(data)
print(f"Desviación estándar de los datos: {desviacion_estandar}")

# Calcular el producto de los datos usando la función prod de math
producto = prod(data)
print(f"Producto de los datos: {producto}")  # Resultado: 120000 (10 * 20 * 30 * 40 * 50)