class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.titulo = titulo
        self.autor = tuple(autor)  # Autor como tupla para que no cambie
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        return f"Titulo: {self.titulo}, Autor: {', '.join(self.autor)}, Categoria: {self.categoria}, ISBN: {self.isbn}"


class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []  # Lista de libros prestados al usuario

    def __str__(self):
        return f"Usuario: {self.nombre}, ID: {self.id_usuario}, Libros prestados: {len(self.libros_prestados)}"


class Biblioteca:
    def __init__(self):
        self.libros = {}
        self.usuarios = []

    def añadir_libro(self, libro):
        self.libros[libro.isbn] = libro
        print(f"Libro '{libro.titulo}' añadido a la biblioteca.")

    def quitar_libro(self, isbn):
        if isbn in self.libros:
            libro = self.libros.pop(isbn)
            print(f"Libro '{libro.titulo}' eliminado de la biblioteca.")
        else:
            print("Libro no encontrado.")

    def registrar_usuario(self, usuario):
        self.usuarios.append(usuario)
        print(f"Usuario '{usuario.nombre}' registrado.")

    def dar_de_baja_usuario(self, id_usuario):
        usuario = next((u for u in self.usuarios if u.id_usuario == id_usuario), None)
        if usuario:
            self.usuarios.remove(usuario)
            print(f"Usuario con ID '{id_usuario}' dado de baja.")
        else:
            print(f"Usuario con ID '{id_usuario}' no encontrado.")

    def prestar_libro(self, id_usuario, isbn):
        usuario = next((u for u in self.usuarios if u.id_usuario == id_usuario), None)
        if not usuario:
            print(f"Usuario con ID {id_usuario} no registrado.")
            return
        if isbn not in self.libros:
            print(f"Libro con ISBN {isbn} no encontrado.")
            return

        libro = self.libros[isbn]
        usuario.libros_prestados.append(libro)
        print(f"Libro '{libro.titulo}' prestado a {usuario.nombre}.")

    def devolver_libro(self, id_usuario, isbn):
        usuario = next((u for u in self.usuarios if u.id_usuario == id_usuario), None)
        if not usuario:
            print(f"Usuario con ID {id_usuario} no registrado.")
            return
        if isbn not in self.libros:
            print(f"Libro con ISBN {isbn} no encontrado.")
            return

        libro = self.libros[isbn]
        if libro in usuario.libros_prestados:
            usuario.libros_prestados.remove(libro)
            print(f"Libro '{libro.titulo}' devuelto por {usuario.nombre}.")

    def buscar_libros(self, titulo=None, autor=None, categoria=None):
        resultados = []
        for libro in self.libros.values():
            if titulo and titulo.lower() in libro.titulo.lower():
                resultados.append(libro)
            elif autor and any(a.lower() in autor.lower() for a in libro.autor):
                resultados.append(libro)
            elif categoria and categoria.lower() in libro.categoria.lower():
                resultados.append(libro)

        return resultados

    def listar_libros_prestados(self, id_usuario):
        usuario = next((u for u in self.usuarios if u.id_usuario == id_usuario), None)
        if usuario:
            if usuario.libros_prestados:
                print(f"Libros prestados a {usuario.nombre}:")
                for libro in usuario.libros_prestados:
                    print(f" - {libro.titulo} (ISBN: {libro.isbn})")
            else:
                print(f"{usuario.nombre} no tiene libros prestados.")

    def mostrar_libros(self):
        if self.libros:
            print("Libros disponibles en la biblioteca:")
            for libro in self.libros.values():
                print(f" - {libro}")
        else:
            print("No hay libros en la biblioteca.")


def mostrar_menu():
    print("\n===== Menú de la Biblioteca Digital =====")
    print("1. Añadir libro")
    print("2. Quitar libro")
    print("3. Registrar usuario")
    print("4. Dar de baja usuario")
    print("5. Prestar libro")
    print("6. Devolver libro")
    print("7. Buscar libro")
    print("8. Listar libros prestados")
    print("9. Mostrar libros disponibles")
    print("0. Salir")
    return input("Elige una opción: ")


def ejecutar_opciones(biblioteca):
    while True:
        opcion = mostrar_menu()

        if opcion == "1":
            # Añadir libro
            titulo = input("Título del libro: ")
            autor = input("Autor del libro (separado por coma si hay más de uno): ").split(',')
            categoria = input("Categoría del libro: ")
            isbn = input("ISBN del libro: ")
            libro = Libro(titulo, autor, categoria, isbn)
            biblioteca.añadir_libro(libro)

        elif opcion == "2":
            # Quitar libro
            isbn = input("ISBN del libro a quitar: ")
            biblioteca.quitar_libro(isbn)

        elif opcion == "3":
            # Registrar usuario
            nombre = input("Nombre del usuario: ")
            id_usuario = input("ID del usuario: ")
            usuario = Usuario(nombre, id_usuario)
            biblioteca.registrar_usuario(usuario)

        elif opcion == "4":
            # Dar de baja usuario
            id_usuario = input("ID del usuario a dar de baja: ")
            biblioteca.dar_de_baja_usuario(id_usuario)

        elif opcion == "5":
            # Prestar libro
            id_usuario = input("ID del usuario: ")
            isbn = input("ISBN del libro a prestar: ")
            biblioteca.prestar_libro(id_usuario, isbn)

        elif opcion == "6":
            # Devolver libro
            id_usuario = input("ID del usuario: ")
            isbn = input("ISBN del libro a devolver: ")
            biblioteca.devolver_libro(id_usuario, isbn)

        elif opcion == "7":
            # Buscar libro
            print("Opciones de búsqueda:")
            print("1. Buscar por título")
            print("2. Buscar por autor")
            print("3. Buscar por categoría")
            sub_opcion = input("Elige una opción: ")
            if sub_opcion == "1":
                titulo = input("Introduce el título del libro: ")
                resultados = biblioteca.buscar_libros(titulo=titulo)
            elif sub_opcion == "2":
                autor = input("Introduce el autor del libro: ")
                resultados = biblioteca.buscar_libros(autor=autor)
            elif sub_opcion == "3":
                categoria = input("Introduce la categoría del libro: ")
                resultados = biblioteca.buscar_libros(categoria=categoria)

            # Mostrar resultados de búsqueda
            if resultados:
                print("Libros encontrados:")
                for libro in resultados:
                    print(libro)
            else:
                print("No se encontraron libros con esos criterios.")

        elif opcion == "8":
            # Listar libros prestados
            id_usuario = input("ID del usuario: ")
            biblioteca.listar_libros_prestados(id_usuario)

        elif opcion == "9":
            # Mostrar todos los libros disponibles
            biblioteca.mostrar_libros()

        elif opcion == "0":
            # Salir del programa
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida, por favor intenta de nuevo.")


# Crear la biblioteca
biblioteca = Biblioteca()

# Ejemplo: Añadir algunos libros y usuarios
libro1 = Libro("Cien años de soledad", ["Gabriel García Márquez"], "Ficción", "1234567890")
libro2 = Libro("1984", ["George Orwell"], "Distopía", "0987654321")
libro3 = Libro("La sombra del viento", ["Carlos Ruiz Zafón"], "Misterio", "1122334455")

usuario1 = Usuario("Juan Pérez", "U001")
usuario2 = Usuario("Ana López", "U002")

# Añadir libros a la biblioteca
biblioteca.añadir_libro(libro1)
biblioteca.añadir_libro(libro2)
biblioteca.añadir_libro(libro3)

# Registrar usuarios
biblioteca.registrar_usuario(usuario1)
biblioteca.registrar_usuario(usuario2)

# Iniciar el menú interactivo
ejecutar_opciones(biblioteca)
