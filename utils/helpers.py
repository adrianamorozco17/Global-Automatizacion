import random
import string


def generar_identificacion_aleatoria():
    """Genera un número de identificación aleatorio de 8 dígitos."""
    return str(random.randint(10000000, 99999999))

def generar_numero_telefono():
    return str(random.randint(600000000, 699999999))

def generar_correo_aleatorio():
    dominios = ["gmail.com", "hotmail.com", "yahoo.com", "outlook.com"]
    nombre = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    return f"{nombre}@{random.choice(dominios)}"