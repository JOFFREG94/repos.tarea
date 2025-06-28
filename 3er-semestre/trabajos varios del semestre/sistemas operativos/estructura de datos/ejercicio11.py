#Escribir un programa que almacene los vectores
# (1,2,3) y (-1,0,2) en dos listas y muestre por pantalla su producto escalar.

# Vectores almacenados en listas
vector1 = [1, 2, 3]
vector2 = [-1, 0, 2]

# Calcular producto escalar
producto_escalar = sum(a * b for a, b in zip(vector1, vector2))

# Mostrar el resultado
print(f"El producto escalar de {vector1} y {vector2} es: {producto_escalar}")


