def calcular_descuento(monto_total, porcentaje_descuento=20):
    # Calcula el monto del descuento
    descuento = (monto_total * porcentaje_descuento) / 100
    return descuento

# Programa principal
if __name__ == "__main__":
    # Primera llamada: solo monto total
    cocinas = 100
    descuento1 = calcular_descuento(cocinas)
    total_final1 = cocinas - descuento1
    print(f"Compra 1: Monto total: {cocinas}, Descuento: {descuento1}, Total a pagar: {total_final1}")

    # Segunda llamada: monto total y porcentaje de descuento
    monto2 = 200  # Monto total de la compra
    porcentaje2 = 15  # Porcentaje de descuento
    descuento2 = calcular_descuento(monto2, porcentaje2)
    total_final2 = monto2 - descuento2
    print(f"Compra 2: Monto total: {monto2}, Descuento: {descuento2}, Total a pagar: {total_final2}")

