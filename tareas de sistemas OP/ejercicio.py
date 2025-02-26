import threading
import time
import random


class Barberia:
    def __init__(self, num_sillas):
        self.num_sillas = num_sillas
        self.sillas_disponibles = num_sillas
        self.barbero_durmiendo = threading.Semaphore(0)  # Controla si el barbero está dormido
        self.sillas_mutex = threading.Lock()  # Controla el acceso a las sillas
        self.clientes_atendidos = 0  # Contador de clientes atendidos

    def llega_cliente(self, cliente_id):
        with self.sillas_mutex:
            if self.sillas_disponibles > 0:
                self.sillas_disponibles -= 1
                print(f"💺 Cliente {cliente_id} se sienta a esperar ({self.sillas_disponibles} sillas libres)")
                self.barbero_durmiendo.release()  # Despierta al barbero si está dormido
            else:
                print(f"🚶 Cliente {cliente_id} se va, no hay sillas libres.")

    def cortar_cabello(self):
        while self.clientes_atendidos < 10:  # Límite de 10 clientes
            print("💤 El barbero está durmiendo...")
            self.barbero_durmiendo.acquire()  # Espera a que llegue un cliente

            with self.sillas_mutex:
                self.sillas_disponibles += 1  # Libera una silla porque atiende a un cliente
                self.clientes_atendidos += 1

            print(f"💈 El barbero está cortando el cabello... (Cliente {self.clientes_atendidos})")
            time.sleep(random.randint(3, 5))  # Simula el tiempo de corte de cabello
            print("✅ Cliente atendido.")

        print("🚪 La barbería cierra, no más clientes por hoy.")


# Parámetros
num_sillas = 3
barberia = Barberia(num_sillas)

# Hilo del barbero
barbero = threading.Thread(target=barberia.cortar_cabello)
barbero.start()

# Simular llegada de 10 clientes
for cliente_id in range(1, 11):  # Solo 10 clientes
    time.sleep(random.randint(1, 3))  # Los clientes llegan en intervalos aleatorios
    threading.Thread(target=barberia.llega_cliente, args=(cliente_id,)).start()

barbero.join()  # Esperar a que termine el barbero antes de cerrar el programa
print("🛑 Fin del día en la barbería.")
