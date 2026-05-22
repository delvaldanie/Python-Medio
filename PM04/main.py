# Dado un archivo JSON llamado empleados.json que contiene una lista de empleados con sus nombres y salarios, escribe un programa que aumente
#  el salario de cada empleado en un 10% y guarde el archivo actualizado.
# Archivo de ejemplo (empleados.json):
# [{"nombre": "Juan Pérez", "salario": 3500},
#     {"nombre": "Ana Gómez", "salario": 4200},
#     {"nombre": "Luis Rodríguez", "salario": 2800},
#     {"nombre": "María Fernández", "salario": 3900}]

import json
import os

ruta = os.path.join(os.path.dirname(__file__), "empleados.json")

with open(ruta, "r", encoding='utf-8') as archivo:
    empleados = json.load(archivo)

empleados_sueldo_aumentado = list(map(
    lambda empleado: {**empleado, "salario": empleado["salario"] * 1.1},
    empleados
))

print(empleados_sueldo_aumentado)