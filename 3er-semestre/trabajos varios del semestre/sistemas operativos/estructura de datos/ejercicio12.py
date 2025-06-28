#Escribir un programa que almacene las matrices
 # A=(1 2 3)   y   B= (-1 0)
#    (4 5 6)          ( 0 1)
#                     ( 1 1)
#en una lista y muestre por pantalla su producto.
#Nota: Para representar matrices mediante listas usar listas anidadas,
# representando cada vector fila en una lista.
# Matrices de ejemplo
A = [
    [1, 2, 3],
    [4, 5, 6]
]

B = [
    [-1, 0],
    [0, 1],
    [1, 1]
]


# Función para multiplicar matrices A (m x n) y B (n x p)
def multiplicar_matrices(A, B):
    m = len(A)
    n = len(A[0])
    p = len(B[0])

    # Crear matriz resultado m x p con ceros
    resultado = [[0 for _ in range(p)] for _ in range(m)]

    # Multiplicación
    for i in range(m):
        for j in range(p):
            for k in range(n):
                resultado[i][j] += A[i][k] * B[k][j]

    return resultado


# Calcular producto
producto = multiplicar_matrices(A, B)

# Mostrar resultado
print("Producto de matrices:")
for fila in producto:
    print(fila)
