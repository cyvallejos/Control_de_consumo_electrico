# Este archivo contiene las validaciones del sistema.
# Aquí se comprueba que los datos ingresados sean correctos antes de usarlos.
# Esto ayuda a evitar errores y a mantener el programa más seguro.


def validar_consumo(valor):
    try:
        consumo = float(valor)
    except ValueError:

        raise ValueError("El consumo debe ser un valor numerico.")

    if consumo <= 0:
        raise ValueError("El consumo debe ser mayor que cero.")

    return consumo


def es_consumo_elevado(consumo):
    return consumo > 500