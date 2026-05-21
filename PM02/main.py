# Manejo de excepciones con listas
# Crea un programa que: 
# Tenga una lista de números.
# Pida al usuario una posición.
# Muestre el elemento de esa posición.
# Controle los posibles errores usando try y except.
# ValueError → cuando el usuario escribe texto en vez de números.
# IndexError → cuando la posición no existe en la lista.
# finally → código que siempre se ejecuta
from modulo import *

lista_numero = [5,8,9,6,4,7,8,2,3,5,7,2]

print(f"contiene {mostrar_numero(input(f"dame un posicion entre 0 y {len(lista_numero)} "), lista_numero)}")