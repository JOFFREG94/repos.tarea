import json


class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def actualizar_cantidad(self, nueva_cantidad):
        self.cantidad = nueva_cantidad

    def actualizar_precio(self, nuevo_precio):
        self.precio = nuevo_precio

    def to_dict(self):
        return {
            "id": self.id_producto,
            "nombre": self.nombre,
            "cantidad": self.cantidad,
            "precio": self.precio
        }


class Inventario:
    def __init__(self):
        self.productos = {}
        self.cargar_desde_archivo()

    def agregar_producto(self, producto):
        if producto.id_producto in self.productos:
            print("El producto ya existe en el inventario.")
        else:
            self.productos[producto.id_producto] = producto
            self.guardar_en_archivo()

    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            self.guardar_en_archivo()
            print("Producto eliminado correctamente.")
        else:
            print("Producto no encontrado.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        if id_producto in self.productos:
            if cantidad is not None:
                self.productos[id_producto].actualizar_cantidad(cantidad)
            if precio is not None:
                self.productos[id_producto].actualizar_precio(precio)
            self.guardar_en_archivo()
        else:
            print("Producto no encontrado.")

    def buscar_producto(self, nombre):
        encontrados = [p.to_dict() for p in self.productos.values() if nombre.lower() in p.nombre.lower()]
        return encontrados if encontrados else "Producto no encontrado."

    def mostrar_productos(self):
        return [p.to_dict() for p in self.productos.values()]

    def guardar_en_archivo(self):
        with open("inventario.json", "w") as archivo:
            json.dump([p.to_dict() for p in self.productos.values()], archivo, indent=4)

    def cargar_desde_archivo(self):
        try:
            with open("inventario.json", "r") as archivo:
                productos_cargados = json.load(archivo)
                self.productos = {p["id"]: Producto(p["id"], p["nombre"], p["cantidad"], p["precio"]) for p in
                                  productos_cargados}
        except (FileNotFoundError, json.JSONDecodeError):
            self.productos = {}


# Menú interactivo
def menu():
    inventario = Inventario()

    # Agregar ejemplos de productos
    inventario.agregar_producto(Producto("001", "Laptop", 10, 750.99))
    inventario.agregar_producto(Producto("002", "Mouse", 25, 15.99))
    inventario.agregar_producto(Producto("003", "Teclado", 20, 25.50))
    inventario.agregar_producto(Producto("004", "Monitor", 8, 150.75))

    while True:
        print("\n--- Gestión de Inventario ---")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto")
        print("5. Mostrar todos los productos")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_producto = input("ID del producto: ")
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            inventario.agregar_producto(Producto(id_producto, nombre, cantidad, precio))
        elif opcion == "2":
            id_producto = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)
        elif opcion == "3":
            id_producto = input("ID del producto a actualizar: ")
            cantidad = input("Nueva cantidad (dejar vacío para no cambiar): ")
            precio = input("Nuevo precio (dejar vacío para no cambiar): ")
            inventario.actualizar_producto(id_producto, int(cantidad) if cantidad else None,
                                           float(precio) if precio else None)
        elif opcion == "4":
            nombre = input("Nombre del producto a buscar: ")
            print(inventario.buscar_producto(nombre))
        elif opcion == "5":
            print(inventario.mostrar_productos())
        elif opcion == "6":
            break
        else:
            print("Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    menu()
