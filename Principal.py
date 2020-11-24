if __name__ == "__main__":
    from ManejadorEmpleados import Arreglo_Empleados
    import os
    try:
        dimencion = int(input("Ingrese tamaño del arreglo (Por defecto es 10): "))
        while dimencion >10 and dimencion>0:
            if dimencion >11 and dimencion>0:
                print("Debe ingresar un numero entero entre el intervalo [0,10]")
            dimencion = int(input("Ingrese tamaño del arreglo (Por defecto es 10): "))
        ManejaEmpleados = Arreglo_Empleados(dimencion)
        ManejaEmpleados.CargarArreglo()

        def op1 ():
            os.system("cls")
            dni = int(input("Ingrese dni del empleado para registrar hora: "))
            cantidad_hora_trabajadas = int(input("Ingrese la cantidad de horas trabajadas hoy del empleado: "))
            ManejaEmpleados.Registrar_Hora(dni,cantidad_hora_trabajadas)
            input("Precione una tecla para continuar..")
            os.system("cls")
        
        def op2 ():
            os.system("cls")
            print("Nota: Solo hay 3 tipo de tareas, carpintería, electricidad y plomería")
            tarea = str(input("Ingrese nombre de la tarea: "))
            ManejaEmpleados.Mostrar_total_de_tarea(tarea)
            input("Precione una tecla para continuar..")
            os.system("cls")
        
        def op3 ():
            os.system("cls")
            ManejaEmpleados.Ayuda_Solidaria()
            input("Precione una tecla para continuar..")
            os.system("cls")

        def op4 ():
            os.system("cls")
            ManejaEmpleados.Calcular_Sueldo()
            input("Precione una tecla para continuar..")
            os.system("cls")

        def op5 ():
            print("Cerrando Programa...")

        opcion = None
        diccionario = {1:op1,2:op2,3:op3,4:op4,5:op5}
        while opcion != 5:
            print("Ingrese 1 para registrar hora")
            print("Ingrese 2 para ver el total de tarea")
            print("Ingrese 3 para ayudar a los empleados")
            print("Ingrese 4 para calcular el sueldo")
            print("Ingrese 5 para cerrar el programa")
            opcion = int(input("Ingrese una opcion: "))
            op = diccionario.get(opcion, lambda: print("Opcion incorrecta"))
            op()
    except ValueError:
        print("Ingrese un entero..")
