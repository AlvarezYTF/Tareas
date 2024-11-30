class VistaEtiqueta:
    @staticmethod
    def mostrar_menu():
        print("\n--- Gestor de Etiquetas ---")
        print("1. Agregar Etiqueta")
        print("2. Ver Etiquetas")
        print("3. Actualizar Estado de Etiqueta")
        print("4. Eliminar Etiqueta")
        print("5. Salir")

    # Obtener los datos de las etiquetas
    @staticmethod
    def obtener_datos_etiquetas():
        try:
            # Bucle para solicitar los datos correctamente
            while True:
                # Validación para que en el nombre se ingrese un valor
                if nombre := input("Ingrese el nombre de la etiqueta: "):
                    return nombre
                else:
                    print(
                        "El nombre de la etiqueta no puede estar vacío. Por favor ingrese un nuevo valor."
                    )
        except Exception as e:
            print(f"Error al obtener los datos de la etiqueta: ERROR({e})")

    # Función para mostrar las etiquetas existentes
    @staticmethod
    def mostrar_etiquetas(etiquetas):
        try:
            # Validar que existen etiquetas
            if etiquetas:
                print("\n--- Lista de Etiquetas ---")
                # Imprimir etiqueta y su estado
                for etiqueta in etiquetas:
                    print(
                        f"ID: {etiqueta[0]}, Nombre: {etiqueta[1]}"
                    )
            else:
                print("\n---- No hay etiquetas por mostrar ----")
        except Exception as e:
            print(f"Error al mostrar las etiquetas: ERROR({e})")
            return

    # Obtener el ID de la etiqueta
    @staticmethod
    def obtener_id_etiqueta():
        try:
            return int(input("Ingrese el ID de la etiqueta: "))
        except ValueError:
            print("Por favor ingrese un número válido para el ID.")
        except Exception as e:
            print(f"Error al obtener el ID: ERROR({e})")

    # Obtener el estado de la etiqueta (activo/inactivo)
    @staticmethod
    def obtener_nuevo_estado():
        try:
            return input("Ingrese el nuevo estado (activo/inactivo): ")
        except Exception as e:
            print(f"Error al obtener el estado: ERROR({e})")

    # Mostrar mensaje
    @staticmethod
    def mostrar_mensaje(mensaje):
        try:
            print(f"\n{mensaje}")
        except Exception as e:
            print(f"Error al mostrar el mensaje: ERROR({e})")

    # Obtener la opción del menú
    @staticmethod
    def obtener_opcion_menu():
        try:
            return input("Seleccione una opción: ")
        except Exception as e:
            print(f"Error al obtener la opción del menú: ERROR({e})")

    # Función para ingresar un nombre que no exista
    @staticmethod
    def obtener_nombre_valido():
        try:
            return input("El nombre ya existe. Ingresa un nombre diferente: ")
        except Exception as e:
            print(f"Error al obtener el nombre: ERROR({e})")
