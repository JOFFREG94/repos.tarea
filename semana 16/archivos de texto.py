# Escribir en el archivo de texto
# Abrimos el archivo en modo escritura ('w'), lo que crea el archivo si no existe
with open('my_notes.txt', 'w') as file:
    # Escribimos tres líneas de notas personales en el archivo
    file.write("Nota 1: tienes que traer el dinero.\n")
    file.write("Nota 2: Estudia para que seas un buen profesional.\n")
    file.write("Nota 3: llama al equipo para organizar un furbol.\n")

# Abrimos el archivo en modo lectura ('r')
with open('my_notes.txt', 'r') as file:
    # Leemos el contenido del archivo línea por línea
    for line in file:
        # Mostramos cada línea leída en la consola
        print(line.strip())
