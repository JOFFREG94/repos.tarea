import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
import datetime


def agregar_evento():
    fecha = entry_fecha.get()
    hora = entry_hora.get()
    descripcion = entry_descripcion.get()

    if fecha and hora and descripcion:
        tree.insert("", "end", values=(fecha, hora, descripcion))
        entry_fecha.set_date(datetime.date.today())  # Restablece la fecha al día actual
        entry_hora.delete(0, tk.END)
        entry_descripcion.delete(0, tk.END)
    else:
        messagebox.showwarning("Entrada inválida", "Todos los campos son obligatorios")


def eliminar_evento():
    seleccionado = tree.selection()
    if seleccionado:
        if messagebox.askyesno("Confirmar", "¿Estás seguro de eliminar el evento?"):
            tree.delete(seleccionado)
    else:
        messagebox.showwarning("Selección inválida", "Selecciona un evento para eliminar")


# Crear ventana principal
root = tk.Tk()
root.title("Agenda Personal")
root.geometry("500x400")

# Frame para la entrada de datos
frame_entrada = tk.Frame(root)
frame_entrada.pack(pady=10)

tk.Label(frame_entrada, text="Fecha:").grid(row=0, column=0)
tk.Label(frame_entrada, text="Hora:").grid(row=1, column=0)
tk.Label(frame_entrada, text="Descripción:").grid(row=2, column=0)

entry_fecha = DateEntry(frame_entrada, width=12, background='darkblue', foreground='white', borderwidth=2)
entry_fecha.grid(row=0, column=1)

entry_hora = tk.Entry(frame_entrada)
entry_hora.grid(row=1, column=1)

entry_descripcion = tk.Entry(frame_entrada)
entry_descripcion.grid(row=2, column=1)

# Botones
frame_botones = tk.Frame(root)
frame_botones.pack(pady=10)

tk.Button(frame_botones, text="Agregar Evento", command=agregar_evento).pack(side=tk.LEFT, padx=5)
tk.Button(frame_botones, text="Eliminar Evento", command=eliminar_evento).pack(side=tk.LEFT, padx=5)
tk.Button(frame_botones, text="Salir", command=root.quit).pack(side=tk.LEFT, padx=5)

# TreeView para mostrar eventos
tree = ttk.Treeview(root, columns=("Fecha", "Hora", "Descripción"), show="headings")
tree.heading("Fecha", text="Fecha")
tree.heading("Hora", text="Hora")
tree.heading("Descripción", text="Descripción")
tree.pack(pady=20)

root.mainloop()
