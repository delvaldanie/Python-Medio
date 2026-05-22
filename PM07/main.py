# Ejercicio 
# Escribir una función que reciba un diccionario con las notas de los alumnos de un curso y devuelva una serie con las notas de los alumnos
# aprobados ordenadas de mayor a menor.
import pandas as pd

def notas_aprobados(alumnos: list[dict]) -> pd.Series:
    """
    Recibe una lista de diccionarios con las notas de los alumnos
    y devuelve una Serie con las notas de los aprobados (>= 5),
    ordenadas de mayor a menor.
    """
    notas = {a["nombre"]: a["nota"] for a in alumnos}
    serie = pd.Series(notas)
    return serie[serie >= 5].sort_values(ascending=False)

alumnos = [
    {"nombre": "Ana García", "nota": 9.2},
    {"nombre": "Carlos López", "nota": 6.5},
    {"nombre": "María Fernández", "nota": 7.8},
    {"nombre": "David Martínez", "nota": 4.3},
    {"nombre": "Lucía Sánchez", "nota": 8.6},
    {"nombre": "Pablo Ruiz", "nota": 5.9},
]

resultado = notas_aprobados(alumnos)
print(resultado)
