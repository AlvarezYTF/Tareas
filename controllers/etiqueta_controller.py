# Clase que controla las etiquetas
class ControladorEtiqueta:
    # Constructor para conectarse al modelo y la vista
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista

    # Función para ejecutar las opciones
    def ejecutar(self):  # sourcery skip: low-code-quality
        # Se llama del script modelo para crear la tabla en BD
        self.modelo.crear_tabla()
        self.modelo.crear_tabla_tarea_etiqueta()
        while True:
            # Se llama desde la vista la función de mostrar menú
            self.vista.mostrar_menu()
            # Match para manejar diferentes opciones
            match self.vista.obtener_opcion_menu():
                case "1":  # Agregar etiqueta
                    try:
                        while True:
                            # Se llama a la vista para obtener el nombre y la descripción
                            nombre, descripcion = self.vista.obtener_datos_etiqueta()
                            # Validar si el nombre existe llamando al modelo
                            if self.modelo.validar_existencia_nombre(nombre):
                                # Bucle para que el usuario ingrese un nombre diferente
                                while True:
                                    nombre = self.vista.obtener_nombre_valido()
                                    if not self.modelo.validar_existencia_nombre(
                                        nombre
                                    ):
                                        break
                            # Agregar la etiqueta con el nombre nuevo
                            self.modelo.agregar_etiqueta(nombre, descripcion)
                            self.vista.mostrar_mensaje(
                                "¡Etiqueta agregada correctamente!"
                            )
                            break
                    except Exception as e:
                        self.vista.mostrar_mensaje(
                            f"Error al agregar la etiqueta: typeError({e})"
                        )
                case "2":  # Ver etiquetas
                    try:
                        etiquetas = self.modelo.obtener_etiquetas()
                        self.vista.mostrar_etiquetas(etiquetas)
                    except Exception as e:
                        self.vista.mostrar_mensaje(
                            f"Error al mostrar las etiquetas: typeError({e})"
                        )
                case "3":  # Actualizar estado de etiqueta
                    try:
                        while True:
                            id_etiqueta = self.vista.obtener_id_etiqueta()
                            if id_etiqueta > 0:
                                if self.modelo.validar_id(id_etiqueta):
                                    while True:
                                        nuevo_estado = self.vista.obtener_nuevo_estado()
                                        if self.modelo.validar_nuevo_estado(
                                            nuevo_estado
                                        ):
                                            self.modelo.actualizar_estado_etiqueta(
                                                id_etiqueta, nuevo_estado
                                            )
                                            self.vista.mostrar_mensaje(
                                                "¡Estado de la etiqueta actualizado!"
                                            )
                                            break
                                        else:
                                            print(
                                                "Estado no válido, ingrese activo/inactivo"
                                            )
                                    break
                                else:
                                    self.vista.mostrar_mensaje("ID no encontrado")
                            else:
                                self.vista.mostrar_mensaje(
                                    "Ingrese un número mayor que cero"
                                )
                    except TypeError as e:
                        self.vista.mostrar_mensaje("Número de ID no válido")
                case "4":  # Eliminar etiqueta
                    try:
                        while True:
                            id_etiqueta = self.vista.obtener_id_etiqueta()
                            if id_etiqueta > 0:
                                if self.modelo.validar_id(id_etiqueta):
                                    self.modelo.eliminar_etiqueta(id_etiqueta)
                                    self.vista.mostrar_mensaje(
                                        "¡Etiqueta eliminada correctamente!"
                                    )
                                    break
                                else:
                                    self.vista.mostrar_mensaje("ID no encontrado")
                            else:
                                self.vista.mostrar_mensaje(
                                    "Ingrese un número mayor que cero"
                                )
                    except TypeError as e:
                        self.vista.mostrar_mensaje("Número de ID no válido")
                case "5":  # Salir
                    self.vista.mostrar_mensaje(
                        "Saliendo del gestor de etiquetas. ¡Hasta pronto!"
                    )
                    break
                case _:
                    self.vista.mostrar_mensaje(
                        "Opción no válida. Por favor, intente de nuevo."
                    )
