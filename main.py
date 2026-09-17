# Este archivo es el punto de entrada del programa.
# Aquí se ejecuta la lógica principal: pedir datos, validarlos y mostrar resultados.
# Sirve como conexión entre las validaciones, los cálculos y la presentación.

from validaciones import es_consumo_elevado, validar_consumo
from calculos import (
    calcular_costo,
    determinar_rango,
    obtener_recomendaciones,
    obtener_tarifa,
)
from reportes import mostrar_error, mostrar_resumen, mostrar_titulo


def ejecutar_programa():
    mostrar_titulo()

    try:
        dato_consumo = input("Ingrese el consumo mensual en kWh: ")
        consumo = validar_consumo(dato_consumo)
        rango = determinar_rango(consumo)
        tarifa = obtener_tarifa(consumo)
        costo = calcular_costo(consumo, tarifa)
        elevado = es_consumo_elevado(consumo)
        recomendaciones = obtener_recomendaciones(consumo, elevado)
        mostrar_resumen(consumo, rango, tarifa, costo, elevado, recomendaciones)
    except ValueError as error:
        mostrar_error(str(error))
    finally:
        print("\nFin del programa.")


if __name__ == "__main__":
    ejecutar_programa(