import tkinter as tk
from tkinter import messagebox

# Función para cargar tareas desde un archivo
def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
            for task in tasks:
                listbox_tasks.insert(tk.END, task.strip())
    except FileNotFoundError:
        pass  # Si no hay archivo, no hacer nada

# Función para guardar las tareas en un archivo
def save_tasks():
    with open("tasks.txt", "w") as file:
        for task in listbox_tasks.get(0, tk.END):
            file.write(task + "\n")

# Función para agregar tarea
def add_task():
    task = entry_task.get()  # Obtener la tarea ingresada
    if task != "":  # Si la tarea no está vacía
        listbox_tasks.insert(tk.END, task)  # Agregar tarea a la lista
        entry_task.delete(0, tk.END)  # Limpiar el campo de entrada
        save_tasks()  # Guardar las tareas en el archivo
    else:
        messagebox.showwarning("Advertencia", "Por favor, ingresa una tarea.")  # Mensaje de advertencia si no se ingresa texto

# Función para eliminar tarea
def delete_task():
    try:
        task_index = listbox_tasks.curselection()  # Obtener el índice de la tarea seleccionada
        listbox_tasks.delete(task_index)  # Eliminar tarea
        save_tasks()  # Guardar las tareas en el archivo
    except:
        messagebox.showwarning("Advertencia", "Por favor, selecciona una tarea para eliminar.")  # Mensaje si no hay tarea seleccionada

# Función para marcar tarea como completada
def complete_task():
    try:
        task_index = listbox_tasks.curselection()  # Obtener el índice de la tarea seleccionada
        task = listbox_tasks.get(task_index)  # Obtener la tarea
        # Marcar la tarea como completada
        listbox_tasks.delete(task_index)  # Eliminar la tarea de la lista
        listbox_tasks.insert(task_index, task + " (Completada)")  # Insertar la tarea como completada
        save_tasks()  # Guardar las tareas en el archivo
    except:
        messagebox.showwarning("Advertencia", "Por favor, selecciona una tarea para marcar como completada.")  # Mensaje si no hay tarea seleccionada

# Función para manejar la tecla Enter para agregar tareas
def handle_enter(event):
    add_task()

# Función para ordenar tareas alfabéticamente
def sort_tasks():
    tasks = listbox_tasks.get(0, tk.END)
    tasks_sorted = sorted(tasks)
    listbox_tasks.delete(0, tk.END)  # Limpiar la lista
    for task in tasks_sorted:
        listbox_tasks.insert(tk.END, task)  # Insertar tareas ordenadas
    save_tasks()  # Guardar las tareas ordenadas en el archivo

# Función para filtrar tareas completadas
def filter_completed_tasks():
    tasks = listbox_tasks.get(0, tk.END)
    completed_tasks = [task for task in tasks if "(Completada)" in task]
    listbox_tasks.delete(0, tk.END)  # Limpiar la lista
    for task in completed_tasks:
        listbox_tasks.insert(tk.END, task)  # Insertar solo tareas completadas

# Función para mostrar todas las tareas
def show_all_tasks():
    tasks = listbox_tasks.get(0, tk.END)
    listbox_tasks.delete(0, tk.END)  # Limpiar la lista
    for task in tasks:
        listbox_tasks.insert(tk.END, task)  # Insertar todas las tareas

# Crear la ventana principal
root = tk.Tk()
root.title("Gestión de Tareas")

# Crear el campo de entrada para nuevas tareas
entry_task = tk.Entry(root, width=40)
entry_task.pack(pady=10)
entry_task.bind("<Return>", handle_enter)  # Vincular la tecla Enter para agregar tareas

# Crear la lista de tareas
listbox_tasks = tk.Listbox(root, width=40, height=10)
listbox_tasks.pack(pady=10)

# Crear los botones para las funcionalidades
button_add = tk.Button(root, text="Añadir Tarea", width=20, command=add_task)
button_add.pack(pady=5)

button_complete = tk.Button(root, text="Marcar como Completada", width=20, command=complete_task)
button_complete.pack(pady=5)

button_delete = tk.Button(root, text="Eliminar Tarea", width=20, command=delete_task)
button_delete.pack(pady=5)

button_sort = tk.Button(root, text="Ordenar Tareas", width=20, command=sort_tasks)
button_sort.pack(pady=5)

button_filter_completed = tk.Button(root, text="Filtrar Completadas", width=20, command=filter_completed_tasks)
button_filter_completed.pack(pady=5)

button_show_all = tk.Button(root, text="Mostrar Todas", width=20, command=show_all_tasks)
button_show_all.pack(pady=5)

# Cargar las tareas desde el archivo al inicio
load_tasks()

# Iniciar la aplicación
root.mainloop()
