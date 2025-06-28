#Escribir un programa que pida al usuario una palabra
# y muestre por pantalla si es un palíndromo.
# Pedir palabra al usuario
palabra = input("Introduce una palabra: ").lower().replace(" ", "")

# Verificar si la palabra es igual a su reverso
if palabra == palabra[::-1]:
    print("La palabra es un palíndromo.")
else:
    print("La palabra no es un palíndromo.")
