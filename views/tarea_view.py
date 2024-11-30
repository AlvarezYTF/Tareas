class VistaTarea:
    @staticmethod
    def mostrar_menu():
        print("\n--- Gestor de Tareas ---")
        print("1. Agregar Tarea")
        print("2. Ver Tareas")
        print("3. Actualizar Estado de Tarea")
        print("4. Eliminar Tarea")
        print("5. Ver etiquetas de una tarea")
        print("6. Salir")

    # Obtener los datos de la tarea
    @staticmethod
    def obtener_titulo():
        try:
            # Bucle para solicitar los datos correctamente
            while True:
                # Validacion para que en el titulo se ingrese un valor
                if titulo := input("Ingrese el título de la tarea: "):
                    return titulo
                else:
                    print("El titulo no puede quedar vacido")
        except Exception as e:
            print(f"Error al obtener el titulo de la tarea: ERROR({e})")

    @staticmethod
    def obtener_descripcion():
        try:
            return input("Ingrese la descripción de la tarea: ")
        except Exception as e:
            print(f"Error al obtener la descripcion de la tarea: ERROR({e})")

    # Funcion para mostrar las tareas existentes
    @staticmethod
    def mostrar_tareas(tareas):
        # try:
            # Validar de que existen tareas
            if tareas:
                print("\n--- Lista de Tareas ---")
                # Imprimir tarea con su descripcion y estado
                for tarea in tareas:
                    # Determina lo contenido en la descripcion e imprime segun si hay o no
                    if tarea[2]:
                        if tarea[2] == 1:
                            print(
                                f"ID: {tarea[0]}, Título: {tarea[1]}, Descripción: {tarea[2]}, Estado: Completada"
                            )
                        else:
                            print(
                                f"ID: {tarea[0]}, Título: {tarea[1]}, Descripción: {tarea[2]}, Estado: Pendiente"
                            )                            
                    else:
                        if tarea[2] == 1:
                            print(
                                f"ID: {tarea[0]}, Título: {tarea[1]}, Descripción: No hay descripcion, Estado: Completada"
                            )
                        else:
                            print(
                                f"ID: {tarea[0]}, Título: {tarea[1]}, Descripción: No hay descripcion, Estado: Pendiente"
                            )
            else:
                print("\n---- No hay tareas por mostrar ----")
        # except Exception as e:
        #     print(f"Error al mostrar las tareas: ERROR({e})")
        #     return

    # Obtener el ID de la tarea
    @staticmethod
    def obtener_id_tarea():
        try:
            return int(input("Ingrese el ID de la tarea: "))
        except Exception as e:
            print("Error a la hora de obtener el ID: ERROR({e})")

    # Obtener el estado de la tarea (pendiente/completada)
    @staticmethod
    def obtener_nuevo_estado():
        try:
            return input("Ingrese el nuevo estado (pendiente/completada): ")
        except Exception as e:
            print("Error a la hora de obtener el ID: ERROR({e})")

    # Mostrar mensaje
    @staticmethod
    def mostrar_mensaje(mensaje):
        try:
            print(f"\n{mensaje}")
        except Exception as e:
            print("Error a la hora de obtener el ID: ERROR({e})")

    # Obtener el opcion del menu
    @staticmethod
    def obtener_opcion_menu():
        try:
            return input("Seleccione una opción: ")
        except Exception as e:
            print("Error a la hora de obtener la opcion: ERROR({e})")

    # Funcion para que ingrese un titulo que no exista
    @staticmethod
    def obtener_titulo_valido():
        try:
            return input("El titulo ya existe. Ingresa un titulo diferente: ")
        except Exception as e:
            print("Error a la hora de obtener el titulo: ERROR({e})")

    @staticmethod
    def obtener_confirmacion_eliminacion():
        while True:
            opcion = input("¿Estás seguro de que deseas eliminar esta tarea? (s/n): ").strip().lower()
            if opcion in ["s", "n"]: 
                return opcion
            else:
                print("Opcion no valida. Ingresa una valida '(s/n)'")

    @staticmethod   
    def obtener_confirmacion_etiquetas():
        while True:
            opcion = input("¿Deseas agregar otra etiqueta? (s/n): ").strip().lower()
            if opcion in ["s", "n"]: 
                return opcion
            else:
                print("Opcion no valida. Ingresa una valida '(s/n)'")

    @staticmethod
    def obtener_confirmacion():
        while True:
            opcion = input("¿Deseas agregar una etiqueta? (s/n): ").strip().lower()
            if opcion in ["s", "n"]: 
                return opcion
            else:
                print("Opcion no valida. Ingresa una valida '(s/n)'")
