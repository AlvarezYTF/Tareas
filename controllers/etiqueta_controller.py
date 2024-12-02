# Clase que controla las etiquetas
class ControladorEtiqueta:
    # Constructor para conectarse al modelo y la vista
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista

    # Función para ejecutar las opciones
    def ejecutar(self):
        # Se llama del script modelo para crear la tabla en BD
        self.modelo.crear_tabla()
        self.modelo.crear_tabla_tarea_etiqueta()
        while True:
            # Se llama desde la vista la función de mostrar menú
            self.vista.mostrar_menu()
            # Match para manejar diferentes opciones
            match self.vista.obtener_opcion_menu():
                case "1":  # Agregar etiqueta
                    intentos = 3
                    while intentos > 0:
                        nombre = self.vista.obtener_datos_etiquetas()
                        if self.modelo.validar_existencia_nombre(nombre):
                            self.vista.mostrar_mensaje("El nombre ya existe.")
                            intentos -= 1
                        else:
                            self.modelo.agregar_etiqueta(nombre)
                            self.vista.mostrar_mensaje(
                                "¡Etiqueta agregada correctamente!"
                            )
                            break
                    if intentos == 0:
                        self.vista.mostrar_mensaje(
                            "Intentos agotados. Regresando al menú."
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
                    intentos = 3
                    while intentos > 0:
                        id_etiqueta = self.vista.obtener_id_etiqueta()
                        if id_etiqueta > 0 and self.modelo.validar_id(id_etiqueta):
                            while True:
                                nuevo_estado = self.vista.obtener_nuevo_estado()
                                if self.modelo.validar_nuevo_estado(nuevo_estado):
                                    bool_estado = self.modelo.cambiar_estado_booleano(
                                        nuevo_estado
                                    )
                                    self.modelo.actualizar_etiqueta(
                                        id_etiqueta, bool_estado
                                    )
                                    self.vista.mostrar_mensaje(
                                        "¡Estado de la etiqueta actualizado!"
                                    )
                                    break
                                else:
                                    self.vista.mostrar_mensaje(
                                        "Estado no válido, ingrese activo/inactivo"
                                    )
                            break
                        else:
                            self.vista.mostrar_mensaje(
                                "ID no válido. Intente de nuevo."
                            )
                            intentos -= 1
                    if intentos == 0:
                        self.vista.mostrar_mensaje(
                            "Intentos agotados. Regresando al menú."
                        )
                case "4":  # Eliminar etiqueta
                    intentos = 3
                    while intentos > 0:
                        id_etiqueta = self.vista.obtener_id_etiqueta()
                        if id_etiqueta > 0 and self.modelo.validar_id(id_etiqueta):
                            self.modelo.eliminar_etiqueta(id_etiqueta)
                            self.vista.mostrar_mensaje(
                                "¡Etiqueta eliminada correctamente!"
                            )
                            break
                        else:
                            self.vista.mostrar_mensaje(
                                "ID no válido. Intente de nuevo."
                            )
                            intentos -= 1
                    if intentos == 0:
                        self.vista.mostrar_mensaje(
                            "Intentos agotados. Regresando al menú."
                        )
                case "5":  # Salir
                    self.vista.mostrar_mensaje(
                        "Saliendo del gestor de etiquetas. ¡Hasta pronto!"
                    )
                    break
                case _:
                    self.vista.mostrar_mensaje(
                        "Opción no válida. Por favor, intente de nuevo."
                    )
