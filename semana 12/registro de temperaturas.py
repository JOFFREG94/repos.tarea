import random

# Definimos las ciudades y el número de semanas y días
ciudades = ["Quito", "Cuenca", "Loja"]
num_semanas = 4
num_dias = 7

# Creamos una estructura para almacenar las temperaturas
temperaturas = {}
for ciudad in ciudades:
    temperaturas[ciudad] = []
    for semana in range(num_semanas):
        semana_temperaturas = [random.randint(10, 25) for _ in range(num_dias)]  # Temperaturas entre 10 y 25 grados
        temperaturas[ciudad].append(semana_temperaturas)

# Función para calcular el promedio de una semana
def calcular_promedio_semanal(temperaturas_semana):
    return sum(temperaturas_semana) / len(temperaturas_semana)

# Calculamos y mostramos los promedios
for ciudad, datos_ciudad in temperaturas.items():
    print(f"Ciudad: {ciudad}")
    for semana, temperaturas_semana in enumerate(datos_ciudad, start=1):
        promedio = calcular_promedio_semanal(temperaturas_semana)
        print(f"  Semana {semana}: Promedio = {promedio:.2f}°C")