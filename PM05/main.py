# Vamos a crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Construye los siguientes métodos para la clase:
# Un constructor, donde los datos pueden estar vacíos.
# Los setters y getters para cada uno de los atributos. Hay que validar las entradas de datos.
# mostrar(): Muestra los datos de la persona.
# esMayorDeEdad(): Devuelve un valor lógico indicando si es mayor de edad.

from persona import Persona

persona1 = Persona("Juan", 12, "123456789Q")

print(f"parte get == Nombre: {persona1.getNombre()}, Edad: {persona1.getedad()}, DNI: {persona1.getDNI()}")
lista_persona = persona1.mostrar()
print(f"Parte mostrar == Nombre: {lista_persona[0]}, Edad: {lista_persona[1]}, DNI: {lista_persona[2]}")
print(persona1.esMayorDeEdad())
persona1.setedad(20)
print(f"Nombre: {persona1.getNombre()}, Edad: {persona1.getedad()}, DNI: {persona1.getDNI()}")
lista_persona = persona1.mostrar()
print(f"Parte mostrar == Nombre: {lista_persona[0]}, Edad: {lista_persona[1]}, DNI: {lista_persona[2]}")
print(persona1.esMayorDeEdad())