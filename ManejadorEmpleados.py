import numpy as np
from ClaseEmpleados import Empleado
from ClaseContratado import Empleado_Contratado
from ClaseExterno import Empleado_Externo
from ClasedePlanta import Empleado_de_Planta
class Arreglo_Empleados ():
    def __init__ (self,dimencion=10):
        self.__array = np.empty(dimencion, dtype=Empleado)
        self.__cantidad = 0
        self.__dimencion = dimencion
    
    def addArray (self,empleado):
        if self.__cantidad < self.__dimencion:
            self.__array[self.__cantidad] = empleado
            self.__cantidad += 1
    
    def CargarArreglo (self):
        import csv
        archivo1 = open("contratados.csv")
        archivo2 = open("externos.csv")
        archivo3 = open("planta.csv")
        leer1 = csv.DictReader(archivo1,delimiter=";")
        leer2 = csv.DictReader(archivo2,delimiter=";")
        leer3 = csv.DictReader(archivo3,delimiter=";")
        for contratado in leer1:
            self.addArray(Empleado_Contratado(**contratado))
        for externo in leer2:
            self.addArray(Empleado_Externo(**externo))
        for deplanta in leer3:
            self.addArray(Empleado_de_Planta(**deplanta))

    def Buscar_empleado_por_dni (self,dni):
        i = 0
        while i<len(self.__array) and int(self.__array[i].getDni()) != dni:
            i += 1
        if i<len(self.__array):
            return i
        return -1

    def Registrar_Hora (self,dni,cantidad_horas):
        buscar_dni = self.Buscar_empleado_por_dni(dni)
        if buscar_dni != -1:
            if isinstance(self.__array[buscar_dni],Empleado_Contratado):
                print("Cantidad de horas del empleado antes de incrementar: ",int(self.__array[buscar_dni].getCantidadHoras()))
                print("Cantidad de horas trabajadas despues de incrementar: ",int(self.__array[buscar_dni].setCantidadHoras(cantidad_horas)))
            else:
                print("El empleado no es contratado, por favor ingrese un empleado que sea contratado")
        else:
            print("El dni no se encontro, vuelva a intentarlo")

    def Mostrar_total_de_tarea (self,nombre_tarea):
        from datetime import datetime
        acum = 0
        Fecha_Actual = datetime.now()
        for empleado in self.__array:
            if isinstance(empleado,Empleado_Externo):
                if str(empleado.getTarea().lower()) == nombre_tarea.lower():
                    if str(Fecha_Actual) > empleado.getFechaFin():
                        acum += float(empleado.getCostoObra())
        if acum == 0:
            print("No hay empleado disponibles para la tarea ingresada o ya se finalizo la tarea")
        else:
            print("El costo total es de",acum)

    def Ayuda_Solidaria (self):
        print("Empleados que necesitan ayuda solidaria:")
        for empledao in self.__array:
            if empledao.SueldoEmpleado() < 25000:
                print("Nombre {}\nDireccion {}\nDni {}".format(empledao.getNombre(),empledao.getDireccion(),empledao.getDni()))
                print("--------------")
    
    def Calcular_Sueldo (self):
        for empledado in self.__array:
            print("Nombre del Empleado:",empledado.getNombre())
            print("Telefono:",empledado.getTelefono())
            print("Sueldo:",empledado.SueldoEmpleado())
            print("----------------------------")
