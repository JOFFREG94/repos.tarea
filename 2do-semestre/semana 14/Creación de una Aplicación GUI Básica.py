import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

def agregar_dato():
    dato = entrada_texto.get()
    try:
        fecha = datetime.strptime(dato, "%Y-%m-%d").date()
        tabla.insert("", "end", values=(fecha,))
        entrada_texto.delete(0, tk.END)
        etiqueta_mensaje.config(text="")  # Limpiar mensaje de error si la entrada es válida
    except ValueError:
        etiqueta_mensaje.config(text="Formato inválido. Use YYYY-MM-DD", fg="red")
        ventana.after(3000, lambda: etiqueta_mensaje.config(text=""))  # Eliminar el mensaje tras 3 segundos

def limpiar_datos():
    if messagebox.askyesno("Confirmación", "¿Seguro que deseas borrar todos los datos?"):
        for item in tabla.get_children():
            tabla.delete(item)
        etiqueta_mensaje.config(text="")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Aplicación GUI - Gestión de Fechas")
ventana.geometry("400x300")
ventana.resizable(False, False)  # Evitar redimensionamiento

# Etiqueta y campo de texto
frame_input = tk.Frame(ventana)
frame_input.pack(pady=10)

etiqueta = tk.Label(frame_input, text="Ingrese una fecha (YYYY-MM-DD):")
etiqueta.grid(row=0, column=0, padx=5)

entrada_texto = tk.Entry(frame_input)
entrada_texto.grid(row=0, column=1, padx=5)

# Mensaje de error
etiqueta_mensaje = tk.Label(ventana, text="", fg="red")
etiqueta_mensaje.pack()

# Botones
frame_botones = tk.Frame(ventana)
frame_botones.pack(pady=5)

boton_agregar = tk.Button(frame_botones, text="Agregar", command=agregar_dato)
boton_agregar.grid(row=0, column=0, padx=5)

boton_limpiar = tk.Button(frame_botones, text="Limpiar", command=limpiar_datos)
boton_limpiar.grid(row=0, column=1, padx=5)

# Tabla para mostrar datos
frame_tabla = tk.Frame(ventana)
frame_tabla.pack(pady=10, fill=tk.BOTH, expand=True)

tabla = ttk.Treeview(frame_tabla, columns=("Fecha",), show="headings")
tabla.heading("Fecha", text="Fecha")
tabla.pack(fill=tk.BOTH, expand=True)

# Ejecutar la aplicación
ventana.mainloop()