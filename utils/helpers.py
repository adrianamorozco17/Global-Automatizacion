import random

def generar_identificacion_aleatoria():
    """Genera un número de identificación aleatorio de 8 dígitos."""
    return str(random.randint(10000000, 99999999))
