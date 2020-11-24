from ClaseEmpleados import Empleado
class Empleado_Externo (Empleado):
    def __init__(self,**dicc):
        super().__init__(**dicc)
        self.__FechaInicio = dicc["FechaInicio"]
        self.__FechaFin = dicc["FechaFin"]
        self.__Tarea = dicc["Tarea"]
        self.__MontoViatico = dicc["MontoViatico"]
        self.__Costo_de_la_obra = dicc["Costo"]
        self.__Monto_seguro_de_vida = dicc["MontoSeguro"]
    
    def getFechaFin (self):
        return self.__FechaFin

    def getTarea (self):
        return self.__Tarea
    
    def getCostoObra (self):
        return self.__Costo_de_la_obra
    
    def SueldoEmpleado (self):
        sueldo = 0
        sueldo = float(self.__Costo_de_la_obra) - int(self.__MontoViatico) - float(self.__Monto_seguro_de_vida)
        return sueldo
