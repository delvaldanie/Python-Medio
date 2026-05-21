

def suma(a,b):
    return a + b

def resta(b, d):
    try:
        valor = b - d   
    except TypeError:
        print("Tipo de dato no válido.")
        valor = 1
    return valor  

def producto(b1, b2):
    return b1 * b2

def division(a, c):
    try:
        valor = a / c   
    except ZeroDivisionError:
        print("No es posible dividir entre cero.")
        valor = 1
    return valor  