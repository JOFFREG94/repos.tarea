#Escribir un programa que almacene las asignaturas de un curso
# (por ejemplo Matemáticas, Física, Química, Historia y Lengua)
# en una lista, pregunte al usuario la nota que ha sacado en cada asignatura,
# y después las muestre por pantalla con el mensaje
# En <asignatura> has sacado <nota> donde <asignatura>
# es cada una des las asignaturas de la lista y <nota>
# cada una de las correspondientes notas introducidas por el usuario.
# Lista de asignaturas
asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]

# Diccionario para guardar las notas
notas = {}

# Pedir la nota de cada asignatura al usuario
for asignatura in asignaturas:
    nota = input(f"¿Qué nota has sacado en {asignatura}? ")
    notas[asignatura] = nota

# Mostrar las notas
print("\nResumen de tus notas:")
for asignatura in asignaturas:
    print(f"En {asignatura} has sacado {notas[asignatura]}")
