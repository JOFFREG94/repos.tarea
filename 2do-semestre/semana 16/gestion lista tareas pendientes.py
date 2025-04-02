import tkinter as tk
from tkinter import messagebox

# Funciones para manejar tareas
def guardar_tareas():
    with open("tareas.txt", "w", encoding="utf-8") as f:
        for tarea in lista_tareas.get(0, tk.END):
            f.write(tarea + "\n")

def cargar_tareas():
    try:
        with open("tareas.txt", "r", encoding="utf-8") as f:
            tareas = f.readlines()
            for tarea in tareas:
                lista_tareas.insert(tk.END, tarea.strip())
    except FileNotFoundError:
        pass  # Si el archivo no existe, no pasa nada

def agregar_tarea(event=None):
    tarea = entrada_tarea.get().strip()
    if tarea:
        lista_tareas.insert(tk.END, tarea)
        entrada_tarea.delete(0, tk.END)
        guardar_tareas()  # Guardar después de agregar tarea
    else:
        messagebox.showwarning("Advertencia", "No puedes agregar una tarea vacía.")

def marcar_completada(event=None):
    if isinstance(event, tk.Event) and event.widget == entrada_tarea:
        return
    try:
        seleccion = lista_tareas.curselection()[0]
        tarea = lista_tareas.get(seleccion)
        if not tarea.startswith("✔ "):
            lista_tareas.delete(seleccion)
            lista_tareas.insert(seleccion, f"✔ {tarea}")
            lista_tareas.itemconfig(seleccion, {'fg': 'gray'})  # Cambiar color de texto
            guardar_tareas()  # Guardar después de marcar como completada
    except IndexError:
        messagebox.showwarning("Advertencia", "Selecciona una tarea para marcar como completada.")

def eliminar_tarea(event=None):
    if isinstance(event, tk.Event) and event.widget == entrada_tarea:
        return
    try:
        seleccion = lista_tareas.curselection()[0]
        lista_tareas.delete(seleccion)
        guardar_tareas()  # Guardar después de eliminar tarea
    except IndexError:
        messagebox.showwarning("Advertencia", "Selecciona una tarea para eliminar.")

def limpiar_lista():
    lista_tareas.delete(0, tk.END)
    guardar_tareas()  # Guardar después de limpiar todas las tareas

def cerrar_aplicacion(event=None):
    guardar_tareas()  # Guardar tareas al cerrar la aplicación
    root.quit()

# Configuración de la ventana
root = tk.Tk()
root.title("Lista de Tareas")
root.geometry("420x450")
root.resizable(False, False)
root.configure(bg="#f0f0f0")

# Etiqueta y Campo de entrada
tk.Label(root, text="Nueva Tarea:", bg="#f0f0f0", font=("Arial", 10, "bold")).pack(pady=5)
entrada_tarea = tk.Entry(root, width=50)
entrada_tarea.pack(pady=5)
entrada_tarea.bind("<Return>", agregar_tarea)

# Botones
frame_botones = tk.Frame(root, bg="#f0f0f0")
frame_botones.pack(pady=5)

btn_agregar = tk.Button(frame_botones, text="Agregar", command=agregar_tarea, width=12)
btn_agregar.grid(row=0, column=0, padx=5)

btn_completar = tk.Button(frame_botones, text="Marcar Completada", command=marcar_completada, width=15)
btn_completar.grid(row=0, column=1, padx=5)

btn_eliminar = tk.Button(frame_botones, text="Eliminar", command=eliminar_tarea, width=12)
btn_eliminar.grid(row=0, column=2, padx=5)

btn_limpiar = tk.Button(frame_botones, text="Limpiar Todo", command=limpiar_lista, width=12)
btn_limpiar.grid(row=0, column=3, padx=5)

# Lista de tareas con Scrollbar
frame_lista = tk.Frame(root)
frame_lista.pack(pady=10)

scrollbar = tk.Scrollbar(frame_lista)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

lista_tareas = tk.Listbox(frame_lista, width=55, height=15, yscrollcommand=scrollbar.set)
lista_tareas.pack()
scrollbar.config(command=lista_tareas.yview)

# Menú de opciones
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

menu_archivo = tk.Menu(menu_bar, tearoff=0)
menu_archivo.add_command(label="Salir", command=cerrar_aplicacion)
menu_bar.add_cascade(label="Archivo", menu=menu_archivo)

menu_ayuda = tk.Menu(menu_bar, tearoff=0)
menu_ayuda.add_command(label="Acerca de", command=lambda: messagebox.showinfo("Acerca de", "Aplicación de lista de tareas - Tkinter"))
menu_bar.add_cascade(label="Ayuda", menu=menu_ayuda)

# Atajos de teclado
root.bind("<c>", marcar_completada)
root.bind("<d>", eliminar_tarea)
root.bind("<Delete>", eliminar_tarea)
root.bind("<Escape>", cerrar_aplicacion)

# Cargar tareas al iniciar
cargar_tareas()

# Ejecutar la aplicación
root.mainloop()
