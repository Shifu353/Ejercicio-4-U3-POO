from ClaseEmpleados import Empleado
class Empleado_Contratado (Empleado):
    def __init__ (self,**dicc):
        try:
            super().__init__(**dicc)
            self.__Fecha_Inicio = dicc["fechaInicio"]
            self.__Fecha_Fin = dicc["FechaFin"]
            self.__Cantidad_horas = int(dicc["CantidadHorasTrabajadas"])
            self.__valor = dicc["Valor"]
        except KeyError:
            print("Error")
    def getCantidadHoras(self):
        return self.__Cantidad_horas

    def setCantidadHoras(self,cantidad_horas):
        self.__Cantidad_horas += cantidad_horas
        return self.getCantidadHoras()
    
    def SueldoEmpleado (self):
        sueldo = 0
        sueldo = int(self.__Cantidad_horas) * float(self.__valor)
        return sueldo
