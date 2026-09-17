# Este archivo contiene las funciones para analizar el consumo eléctrico.
# Aquí se clasifican los niveles de consumo, se calculan costos y se generan recomendaciones.
# Estas operaciones permiten convertir los datos en información útil para el usuario.

def determinar_rango(consumo):
    if consumo <= 100:
        return "Bajo"
    elif consumo <= 300:
        return "Medio"
    elif consumo <= 500:
        return "Alto"
    else:
        return "Muy alto"


def obtener_tarifa(consumo):
    if consumo <= 100:
        return 0.12
    elif consumo <= 300:
        return 0.15
    elif consumo <= 500:
        return 0.20
    else:
        return 0.25


def calcular_costo(consumo, tarifa):
    return consumo * tarifa


def obtener_recomendaciones(consumo, elevado):
    recomendaciones = [
        "Apagar luces y equipos cuando no se utilicen.",
        "Usar focos LED y aprovechar la luz natural.",
    ]

    if elevado:
        recomendaciones.append("Revisar los equipos de mayor consumo y evitar dejarlos en espera.")
    elif consumo > 300:
        recomendaciones.append("Programar una revision del consumo de los equipos principales.")

    return recomendacione