#Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva,
# los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.

# Pedir al usuario los números ganadores (suponiendo 6 números)
numeros = []

print("Introduce los 6 números ganadores de la lotería primitiva:")

for i in range(6):
    numero = int(input(f"Número {i + 1}: "))
    numeros.append(numero)

# Ordenar la lista
numeros.sort()

# Mostrar los números ordenados
print("\nNúmeros ganadores ordenados de menor a mayor:")
print(numeros)
