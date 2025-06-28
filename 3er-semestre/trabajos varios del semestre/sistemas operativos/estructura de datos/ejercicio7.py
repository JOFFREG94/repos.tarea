#Escribir un programa que almacene el abecedario en una lista,
# elimine de la lista las letras que ocupen posiciones múltiplos de 3,
# y muestre por pantalla la lista resultante.

import string

# Almacenar el abecedario en una lista
abecedario = list(string.ascii_lowercase)  # letras de la 'a' a la 'z'

# Eliminar las letras en posiciones múltiplos de 3 (considerando la primera posición como 1)
resultado = [letra for indice, letra in enumerate(abecedario, start=1) if indice % 3 != 0]

# Mostrar la lista resultante
print("Lista resultante:")
print(resultado)
