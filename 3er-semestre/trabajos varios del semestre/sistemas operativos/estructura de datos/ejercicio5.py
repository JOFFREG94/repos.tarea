#Escribir un programa que almacene en una lista los números del 1 al 10
# y los muestre por pantalla en orden inverso separados por comas.
# Crear una lista con los números del 1 al 10
numeros = list(range(1, 11))

# Invertir la lista
numeros.reverse()

# Mostrar los números separados por comas
print(", ".join(str(numero) for numero in numeros))
