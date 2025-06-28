#Escribir un programa que almacene las asignaturas d
# e un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua)
# en una lista, pregunte al usuario la nota que ha sacado en cada
# asignatura y elimine de la lista las asignaturas aprobadas.
# Al final el programa debe mostrar por pantalla
# las asignaturas que el usuario tiene que repetir.

# Lista de asignaturas
asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]

# Lista para guardar las asignaturas no aprobadas
asignaturas_repetir = []

# Pedir notas al usuario y verificar si aprobó
for asignatura in asignaturas:
    nota = float(input(f"¿Qué nota has sacado en {asignatura}? "))
    if nota < 7:
        asignaturas_repetir.append(asignatura)

# Mostrar asignaturas que debe repetir
print("\nDebes repetir las siguientes asignaturas:")
for asignatura in asignaturas_repetir:
    print(asignatura)
