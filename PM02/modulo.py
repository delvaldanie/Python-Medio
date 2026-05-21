def mostrar_numero(posicion, lista_numeros):
    try:
        numero = lista_numeros[int(posicion)]
    except ValueError:
        print("Tipo de dato no válido.")
        numero = 400
    except IndexError:
        print("Posicion incorrecta.")
        numero = 401
    return numero