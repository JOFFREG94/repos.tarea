#Escribir un programa que pregunte por una muestra de números,
# separados por comas, los guarde en una lista
# y muestre por pantalla su media y desviación típica.
import math

# Pedir la muestra de números separados por comas
entrada = input("Introduce los números separados por comas: ")

# Convertir la entrada en una lista de números (floats)
numeros = [float(num.strip()) for num in entrada.split(",")]

# Calcular la media
media = sum(numeros) / len(numeros)

# Calcular la desviación típica (muestral)
varianza = sum((x - media) ** 2 for x in numeros) / (len(numeros) - 1)
desviacion_tipica = math.sqrt(varianza)

# Mostrar resultados
print(f"Media: {media}")
print(f"Desviación típica: {desviacion_tipica}")


