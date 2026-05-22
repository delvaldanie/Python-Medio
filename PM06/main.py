# Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una persona) y cantidad (puede tener decimales). 
# El titular será obligatorio y la cantidad es opcional. Construye los siguientes métodos para la clase:
# Un constructor, donde los datos pueden estar vacíos.
# Los setters y getters para cada uno de los atributos. El atributo no se puede modificar directamente, sólo ingresando o retirando dinero.
# mostrar(): Muestra los datos de la cuenta.
# ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es negativa, no se hará nada.
# retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números rojos.

from cuenta import Cuenta

cuenta1 = Cuenta("Juan", 2000)
print(cuenta1.mostrar())
cuenta1.ingresar(-100)
print(cuenta1.mostrar())
cuenta1.ingresar(+100)
print(cuenta1.mostrar())
cuenta1.retirar(50)
print(cuenta1.mostrar())