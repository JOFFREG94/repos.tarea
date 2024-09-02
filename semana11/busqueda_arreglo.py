def buscar_en_matriz(matriz, valor_buscado):
    """
    Busca un valor en una matriz bidimensional y devuelve su posición si se encuentra.

    :param matriz: Lista de listas que representa la matriz.
    :param valor_buscado: Valor a buscar en la matriz.
    :return: Tupla con la fila y columna del valor si se encuentra, None si no se encuentra.
    """
    for i, fila in enumerate(matriz):
        for j, valor in enumerate(fila):
            if valor == valor_buscado:
                return (i, j)
    return None


def main():
    # Definir una matriz 3x3
    matriz = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    # Valor que se busca en la matriz
    valor_buscado = 5

    # Buscar el valor en la matriz
    resultado = buscar_en_matriz(matriz, valor_buscado)

    if resultado:
        print(f"El valor {valor_buscado} se encontró en la posición {resultado}.")
    else:
        print(f"El valor {valor_buscado} no se encontró en la matriz.")


if __name__ == "__main__":
    main()
