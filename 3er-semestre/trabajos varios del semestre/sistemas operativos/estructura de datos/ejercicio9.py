#Escribir un programa que pida al usuario una palabra
# y muestre por pantalla el número de veces que contiene cada vocal.
# Pedir palabra al usuario
palabra = input("Introduce una palabra: ").lower()

# Definir las vocales
vocales = "aeiou"

# Contar las apariciones de cada vocal
for vocal in vocales:
    cantidad = palabra.count(vocal)
    print(f"La vocal '{vocal}' aparece {cantidad} veces.")
