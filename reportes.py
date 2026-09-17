# Este archivo se encarga de mostrar la información al usuario.
# Aquí se presentan mensajes, resúmenes y errores de forma clara y legible.
# La idea es que la salida del programa sea fácil de entender.

def mostrar_titulo():
    print("\n========================================")
    print("   CONTROL DE CONSUMO ELECTRICO")
    print("========================================")


def mostrar_resumen(consumo, rango, tarifa, costo, elevado, recomendaciones):
    print("\n----------- RESUMEN DEL CONSUMO -----------")
    print(f"Consumo registrado: {consumo:.2f} kWh")
    print(f"Rango de consumo: {rango}")
    print(f"Tarifa aplicada: ${tarifa:.2f} por kWh")
    print(f"Costo estimado: ${costo:.2f}")

    if elevado:
        print("Advertencia: el consumo es elevado.")
    else:
        print("El consumo no supera el nivel elevado.")

    print("\nRecomendaciones de ahorro:")
    for recomendacion in recomendaciones:
        print(f"- {recomendacion}")
    print("-------------------------------------------")


def mostrar_error(mensaje):
    print(f"Error: {mensaje}"
