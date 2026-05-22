# Dado un archivo JSON llamado libros.json, que contiene una lista de libros con sus respectivos títulos, autores y años de publicación, 
# escribe un programa que cargue los datos, los muestre en formato legible y cuente cuántos libros fueron publicados después del año 2000.
# Archivo de ejemplo (libros.json):
# [ {"titulo": "Cien años de soledad", "autor": "Gabriel García Márquez", "año": 1967},
#   {"titulo": "El código Da Vinci", "autor": "Dan Brown", "año": 2003},
#   {"titulo": "El señor de los anillos", "autor": "J.R.R. Tolkien", "año": 1954},
#   {"titulo": "Harry Potter y la piedra filosofal", "autor": "J.K. Rowling", "año": 1997},
#   {"titulo": "Los juegos del hambre", "autor": "Suzanne Collins", "año": 2008}]

import json
import os

ruta = os.path.join(os.path.dirname(__file__), 'libros.json')

with open(ruta, 'r', encoding='utf-8') as archivo:
    libros = json.load(archivo)

print("{}".format(list(filter(lambda libro: libro["año"] >= 2000, libros))))



