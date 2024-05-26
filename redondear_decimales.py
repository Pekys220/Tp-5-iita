def redondear(numero):
    entero = int(numero)
    fraccion = numero - entero
    if fraccion > 0.50:
        return entero + 1
    else:
        return entero
