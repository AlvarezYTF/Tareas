class MainView:
    @staticmethod
    def mostrar_menu_principal():
        print("\n--- Menú Principal ---")
        print("1. Gestionar Tareas")
        print("2. Gestionar Etiquetas")
        print("3. Salir")
        return input("Selecciona una opción: ")

    @staticmethod
    def mostrar_menu_tareas():
        print("\n--- Menú de Gestión de Tareas ---")
        print("1. Crear Tarea")
        print("2. Ver Tareas")
        print("3. Editar Tarea")
        print("4. Eliminar Tarea")
        print("5. Volver al Menú Principal")
        return input("Selecciona una opción: ")

    @staticmethod
    def mostrar_menu_etiquetas():
        print("\n--- Menú de Gestión de Etiquetas ---")
        print("1. Crear Etiqueta")
        print("2. Ver Etiquetas")
        print("3. Editar Etiqueta")
        print("4. Eliminar Etiqueta")
        print("5. Volver al Menú Principal")
        return input("Selecciona una opción: ")

    @staticmethod
    def mostrar_mensaje(mensaje):
        print(mensaje)
