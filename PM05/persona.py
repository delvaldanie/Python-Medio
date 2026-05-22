class Persona:

    def __init__(self, nombre, edad, DNI):
        self._nombre = nombre 
        self._edad = edad 
        self._DNI = DNI 
    
    def setNombre(self, nombre):
        self._nombre = nombre
    
    def getNombre(self):
        return self._nombre

    def setedad(self, edad):
        self._edad = edad
    
    def getedad(self):
        return self._edad
    
    def setDNI(self, DNI):
        self._DNI = DNI
    
    def getDNI(self):
        return self._DNI
    
    def mostrar(self):
        return list([self._nombre, self._edad, self._DNI])
    
    def esMayorDeEdad(self):
        if self._edad > 18:
            return ("Es mayor de edad")
        else:
            return ("No es mayor de edad")