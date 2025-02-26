import os
import json


class Inventario:
    def __init__(self, archivo="inventario.txt"):
        self.archivo = archivo
        self.productos = {}
        self.cargar_inventario()

    def cargar_inventario(self):
        """Carga el inventario desde un archivo de texto."""
        if not os.path.exists(self.archivo):
            print("El archivo de inventario no existe. Se creará uno nuevo.")
            return
        try:
            with open(self.archivo, "r") as f:
                contenido = f.read()
                if contenido:
                    self.productos = json.loads(contenido)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error al cargar el inventario: {e}")
        except PermissionError:
            print("No tienes permiso para leer el archivo de inventario.")

    def guardar_inventario(self):
        """Guarda el inventario en un archivo de texto."""
        try:
            with open(self.archivo, "w") as f:
                json.dump(self.productos, f, indent=4)
            print("Inventario guardado correctamente.")
        except PermissionError:
            print("No tienes permiso para escribir en el archivo de inventario.")
        except Exception as e:
            print(f"Error al guardar el inventario: {e}")

    def agregar_producto(self, nombre, cantidad, precio):
        """Añade un producto al inventario o actualiza su cantidad."""
        if nombre in self.productos:
            self.productos[nombre]["cantidad"] += cantidad
        else:
            self.productos[nombre] = {"cantidad": cantidad, "precio": precio}
        self.guardar_inventario()
        print(f"Producto '{nombre}' agregado/actualizado exitosamente.")

    def eliminar_producto(self, nombre):
        """Elimina un producto del inventario."""
        if nombre in self.productos:
            del self.productos[nombre]
            self.guardar_inventario()
            print(f"Producto '{nombre}' eliminado exitosamente.")
        else:
            print("El producto no existe en el inventario.")

    def mostrar_inventario(self):
        """Muestra todos los productos en el inventario."""
        if not self.productos:
            print("El inventario está vacío.")
        else:
            for nombre, datos in self.productos.items():
                print(f"{nombre}: {datos['cantidad']} unidades - ${datos['precio']} cada uno")


# Ejemplo de uso
if __name__ == "__main__":
    inventario = Inventario()
    while True:
        print("\n1. Agregar Producto")
        print("2. Eliminar Producto")
        print("3. Mostrar Inventario")
        print("4. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            nombre = input("Nombre del producto: ")
            try:
                cantidad = int(input("Cantidad: "))
                precio = float(input("Precio: "))
                inventario.agregar_producto(nombre, cantidad, precio)
            except ValueError:
                print("Error: La cantidad y el precio deben ser números válidos.")
        elif opcion == "2":
            nombre = input("Nombre del producto a eliminar: ")
            inventario.eliminar_producto(nombre)
        elif opcion == "3":
            inventario.mostrar_inventario()
        elif opcion == "4":
            print("Saliendo del sistema de gestión de inventarios.")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")
