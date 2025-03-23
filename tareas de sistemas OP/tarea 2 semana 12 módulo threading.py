import threading
# Creamos una barrera para sincronizar dos hilos
# La barrera hace que los hilos esperen hasta que todos los hilos alcanzan la barrera
# En este caso, hemos definido 2 hilos que deben esperar hasta que ambos lleguen a este punto
barrera = threading.Barrier(2)
# Definimos una función que ejecutará cada hilo
# Esta función realiza una tarea (imprimir un mensaje) y luego espera en la barrera
def tarea():
    print("Hilo iniciado")  # Imprime un mensaje al inicio de la ejecución del hilo
    # Los hilos se bloquean en la barrera. Esperan hasta que ambos lleguen aquí.
    barrera.wait()  # El hilo espera hasta que el otro hilo también llegue a este punto
    print("Hilo continuando")  # Imprime un mensaje cuando ambos hilos han pasado la barrera
# Creamos dos hilos que ejecutarán la misma función `tarea`
hilo1 = threading.Thread(target=tarea)  # Crea el primer hilo
hilo2 = threading.Thread(target=tarea)  # Crea el segundo hilo

# Iniciamos los hilos
# Ambos hilos comenzarán a ejecutarse en paralelo, llamando a la función `tarea`
hilo1.start()
hilo2.start()

# Esperamos a que ambos hilos terminen su ejecución
# El hilo principal se bloquea hasta que ambos hilos hayan terminado
hilo1.join()  # Espera a que hilo1 termine
hilo2.join()  # Espera a que hilo2 termine

# Imprimimos un mensaje final indicando que el programa ha terminado
print("Programa terminado")  # Este mensaje se imprimirá después de que ambos hilos finalicen
