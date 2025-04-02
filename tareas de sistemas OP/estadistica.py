import numpy as np
import pandas as pd

# Datos
horas_ejercicio = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                   2, 4, 5, 6, 3, 8, 9, 7, 4, 5,
                   10, 12, 11, 13, 14]

reduccion_peso = [1.2, 1.4, 1.5, 1.8, 2.0, 2.2, 2.4, 2.6, 2.8, 3.0,
                  1.6, 2.1, 2.3, 2.5, 1.7, 2.7, 2.9, 2.5, 2.0, 2.2,
                  3.1, 3.5, 3.3, 3.7, 3.9]

# Convertir en DataFrame
df = pd.DataFrame({'Horas de Ejercicio': horas_ejercicio, 'Reducción de Peso': reduccion_peso})

# Calcular la correlación de Pearson manualmente
n = len(horas_ejercicio)
sum_x = sum(horas_ejercicio)
sum_y = sum(reduccion_peso)
sum_xy = sum(x*y for x, y in zip(horas_ejercicio, reduccion_peso))
sum_x2 = sum(x**2 for x in horas_ejercicio)
sum_y2 = sum(y**2 for y in reduccion_peso)

# Fórmula de Pearson
numerador = (n * sum_xy) - (sum_x * sum_y)
denominador = np.sqrt((n * sum_x2 - sum_x**2) * (n * sum_y2 - sum_y**2))
r = numerador / denominador

# Mostrar resultados
print(f"Coeficiente de correlación de Pearson: {r:.4f}")

# Validar con la función de numpy
r_numpy = np.corrcoef(horas_ejercicio, reduccion_peso)[0, 1]
print(f"Validación con numpy: {r_numpy:.4f}")

