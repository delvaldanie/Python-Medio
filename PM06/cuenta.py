class Cuenta:
    def __init__(self, titular, cantidad):
        self.titular = titular
        self.cantidad = cantidad
    
    def mostrar(self):
        return (f"Titular {self.titular}, Catidad {self.cantidad}")
    
    def ingresar(self, ingreso):
        if ingreso > 0:
            self.cantidad += ingreso

    def retirar(self, retiro):
        self.cantidad -= retiro