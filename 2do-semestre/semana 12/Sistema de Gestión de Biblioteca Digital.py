class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        # Tupla para autor y título, ya que son inmutables
        self.titulo = titulo
        self.autor = tuple(autor)  # Tupla de autor
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        return f"Titulo: {self.titulo}, Autor: {', '.join(self.autor)}, Categoria: {self.categoria}, ISBN: {self.isbn}"


class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []  # Lista de libros prestados

    def __str__(self):
        return f"Usuario: {self.nombre}, ID: {self.id_usuario}, Libros prestados: {len(self.libros_prestados)}"


class Biblioteca:
    def __init__(self):
        self.libros = {}  # Diccionario para almacenar los libros por ISBN
        self.usuarios = []  # Lista para almacenar los objetos de usuario

    def añadir_libro(self, libro):
        # Añadir un libro al catálogo de la biblioteca
        self.libros[libro.isbn] = libro
        print(f"Libro '{libro.titulo}' añadido a la biblioteca.")

    def quitar_libro(self, isbn):
        # Eliminar un libro del catálogo utilizando su ISBN
        if isbn in self.libros:
            libro = self.libros.pop(isbn)
            print(f"Libro '{libro.titulo}' eliminado de la biblioteca.")
        else:
            print("Libro no encontrado.")

    def registrar_usuario(self, usuario):
        # Registrar un nuevo usuario (almacenando el objeto Usuario)
        self.usuarios.append(usuario)
        print(f"Usuario '{usuario.nombre}' registrado.")

    def dar_de_baja_usuario(self, id_usuario):
        # Dar de baja un usuario (eliminar su objeto Usuario)
        usuario = next((u for u in self.usuarios if u.id_usuario == id_usuario), None)
        if usuario:
            self.usuarios.remove(usuario)
            print(f"Usuario con ID '{id_usuario}' dado de baja.")
        else:
            print(f"Usuario con ID '{id_usuario}' no encontrado.")

    def prestar_libro(self, id_usuario, isbn):
        # Prestar un libro a un usuario
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
        # Devolver un libro prestado por un usuario
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
        # Buscar libros por título, autor o categoría
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
        # Listar libros prestados a un usuario específico
        usuario = next((u for u in self.usuarios if u.id_usuario == id_usuario), None)
        if usuario:
            if usuario.libros_prestados:
                print(f"Libros prestados a {usuario.nombre}:")
                for libro in usuario.libros_prestados:
                    print(f" - {libro.titulo} (ISBN: {libro.isbn})")
            else:
                print(f"{usuario.nombre} no tiene libros prestados.")

    def mostrar_libros(self):
        # Mostrar todos los libros disponibles en la biblioteca
        if self.libros:
            print("Libros disponibles en la biblioteca:")
            for libro in self.libros.values():
                print(f" - {libro}")
        else:
            print("No hay libros en la biblioteca.")


# Crear algunos libros
libro1 = Libro("Cien años de soledad", ["Gabriel García Márquez"], "Ficción", "1234567890")
libro2 = Libro("El amor en los tiempos del cólera", ["Gabriel García Márquez"], "Ficción", "2345678901")
libro3 = Libro("La casa de los espíritus", ["Isabel Allende"], "Ficción", "3456789012")
libro4 = Libro("1984", ["George Orwell"], "Distopía", "4567890123")

# Crear algunos usuarios
usuario1 = Usuario("Juan Pérez", "U001")
usuario2 = Usuario("Ana López", "U002")
usuario3 = Usuario("Carlos Díaz", "U003")

# Crear la biblioteca
biblioteca = Biblioteca()

# Registrar usuarios
biblioteca.registrar_usuario(usuario1)
biblioteca.registrar_usuario(usuario2)
biblioteca.registrar_usuario(usuario3)

# Añadir libros a la biblioteca
biblioteca.añadir_libro(libro1)
biblioteca.añadir_libro(libro2)
biblioteca.añadir_libro(libro3)
biblioteca.añadir_libro(libro4)

# Prestar libros
biblioteca.prestar_libro("U001", "1234567890")
biblioteca.prestar_libro("U002", "2345678901")

# Listar libros prestados
biblioteca.listar_libros_prestados("U001")
biblioteca.listar_libros_prestados("U002")

# Buscar libros por título
print("\nBuscar libros por título 'Cien años':")
libros_encontrados = biblioteca.buscar_libros(titulo="Cien años")
for libro in libros_encontrados:
    print(libro)

# Buscar libros por autor
print("\nBuscar libros por autor 'Gabriel García Márquez':")
libros_encontrados = biblioteca.buscar_libros(autor="Gabriel García Márquez")
for libro in libros_encontrados:
    print(libro)

# Devolver libro
biblioteca.devolver_libro("U001", "1234567890")

# Listar libros prestados nuevamente
biblioteca.listar_libros_prestados("U001")

# Quitar libro de la biblioteca
biblioteca.quitar_libro("3456789012")

# Mostrar libros disponibles en la biblioteca
biblioteca.mostrar_libros()
