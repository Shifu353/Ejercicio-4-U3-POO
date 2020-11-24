from ClaseEmpleados import Empleado
class Empleado_de_Planta (Empleado):
    def __init__ (self,**dicc):
        super().__init__(**dicc)
        self.__SueldoBasico = dicc["SueldoBasico"]
        self.__Antiguedad = dicc["Antiguedad"]

    def SueldoEmpleado (self):
        sueldo = 0
        sueldo = float(self.__SueldoBasico) + (float(self.__SueldoBasico)/100) * int(self.__Antiguedad)
        return sueldo
