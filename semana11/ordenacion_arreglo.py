def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def ordenar_fila(matriz, fila):
    bubble_sort(matriz[fila])

# Matriz de ejemplo
matriz = [[3, 1, 4],
          [5, 9, 2],
          [7, 6, 8]]

# Fila a ordenar (comenzando desde 0)
fila_a_ordenar = 1

print("Matriz original:")
for fila in matriz:
    print(fila)

ordenar_fila(matriz, fila_a_ordenar)

print("\nMatriz con la fila", fila_a_ordenar, "ordenada:")
for fila in matriz:
    print(fila)