class Empleado (object):
    def __init__ (self,**dicc):
        self.__dni = dicc["dni"]
        self.__nombre = dicc["nombre"]
        self.__direccion = dicc["direccion"]
        self.__telefono = dicc["telefono"]
    
    def getDni (self):
        return self.__dni
    
    def getNombre (self):
        return self.__nombre
    
    def getDireccion (self):
        return self.__direccion
    
    def getTelefono (self):
        return self.__telefono
