from models import etiqueta_model
from views import etiqueta_view
from colorama import Back, Fore, Style, init

init()


# Clase que controla las tareas
class ControladorTarea:
    # Constructor para conectarse al modelo y la vista
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista
        self.class_etiqueta_model = etiqueta_model.ModeloEtiqueta()
        self.class_etiqueta_view = etiqueta_view.VistaEtiqueta()

    # Función para ejecutar las opciones
    def ejecutar(self):
        # Se llama del script modelo para crear la tabla en BD
        self.modelo.crear_tabla()
        while True:
            # Mostrar menú desde la vista
            self.vista.mostrar_menu()
            # Match para manejar diferentes opciones
            match self.vista.obtener_opcion_menu():
                case "1":  # Agregar tarea
                    intentos = 3
                    while intentos > 0:
                        try:
                            # Obtener título y descripción
                            titulo = self.vista.obtener_titulo()
                            descripcion = self.vista.obtener_descripcion()

                            # Validar si el título ya existe
                            if self.modelo.validar_existencia_titulo(titulo):
                                self.vista.mostrar_mensaje(
                                    "El título ya existe. Intente con otro."
                                )
                                intentos -= 1
                                continue

                            # Agregar tarea al modelo
                            self.modelo.agregar_tarea(titulo, descripcion)

                            # Asignar etiquetas si el usuario lo desea
                            if self.vista.obtener_confirmacion() == "s":
                                id_tarea = self.modelo.obtener_ultimo_id_tarea()
                                etiquetas = (
                                    self.class_etiqueta_model.obtener_etiquetas()
                                )
                                self.class_etiqueta_view.mostrar_etiquetas(etiquetas)

                                if etiquetas:
                                    while True:
                                        intentos = 3
                                        while intentos > 0:
                                            id_etiqueta = (
                                                self.class_etiqueta_view.obtener_id_etiqueta()
                                            )
                                            if self.class_etiqueta_model.validar_id(
                                                id_etiqueta
                                            ) and not self.modelo.etiqueta_ya_asignada(
                                                id_tarea, id_etiqueta
                                            ):
                                                self.modelo.agregar_etiqueta_tarea(
                                                    id_tarea, id_etiqueta
                                                )
                                                self.vista.mostrar_mensaje(
                                                    "Etiqueta asignada correctamente."
                                                )
                                                break
                                            else:
                                                self.vista.mostrar_mensaje(
                                                    "Etiqueta no válida o ya asignada."
                                                )
                                                intentos -= 1
                                                continue
                                        else:
                                            self.vista.mostrar_mensaje(
                                                "Intentos agotados para asignar etiquetas."
                                            )
                            self.vista.mostrar_mensaje("¡Tarea agregada correctamente!")
                            break
                        except Exception as e:
                            self.vista.mostrar_mensaje(f"Error: {e}")
                            intentos -= 1
                    if intentos == 0:
                        self.vista.mostrar_mensaje(
                            "Intentos agotados. Regresando al menú principal."
                        )

                case "2":  # Ver tareas
                    try:
                        tareas = self.modelo.obtener_tareas()
                        self.vista.mostrar_tareas(tareas)
                    except Exception as e:
                        self.vista.mostrar_mensaje(f"Error al mostrar las tareas: {e}")

                case "3":  # Actualizar estado de tarea
                    intentos = 3
                    while intentos > 0:
                        try:
                            id_tarea = self.vista.obtener_id_tarea()
                            if self.modelo.validar_id(id_tarea):
                                nuevo_estado = self.vista.obtener_nuevo_estado()
                                if self.modelo.validar_nuevo_estado(nuevo_estado):
                                    bool_estado = self.modelo.cambiar_estado_booleano(
                                        nuevo_estado
                                    )
                                    self.modelo.actualizar_tarea(id_tarea, bool_estado)
                                    self.vista.mostrar_mensaje(
                                        "¡Estado de la tarea actualizado!"
                                    )
                                    break
                                else:
                                    self.vista.mostrar_mensaje(
                                        "Estado no válido. Intente nuevamente."
                                    )
                                    intentos -= 1
                            else:
                                self.vista.mostrar_mensaje("ID de tarea no encontrado.")
                                intentos -= 1
                        except Exception as e:
                            self.vista.mostrar_mensaje(f"Error: {e}")
                            intentos -= 1
                    if intentos == 0:
                        self.vista.mostrar_mensaje(
                            "Intentos agotados. Regresando al menú principal."
                        )

                case "4":  # Eliminar tarea
                    intentos = 3
                    while intentos > 0:
                        try:
                            id_tarea = self.vista.obtener_id_tarea()
                            if self.modelo.validar_id(id_tarea):
                                confirmacion = (
                                    self.vista.obtener_confirmacion_eliminacion()
                                )
                                if confirmacion == "s":
                                    self.modelo.eliminar_tarea(id_tarea)
                                    self.vista.mostrar_mensaje(
                                        "¡Tarea eliminada correctamente!"
                                    )
                                    break
                                else:
                                    self.vista.mostrar_mensaje("Eliminación cancelada.")
                                    break
                            else:
                                self.vista.mostrar_mensaje("ID de tarea no encontrado.")
                                intentos -= 1
                        except Exception as e:
                            self.vista.mostrar_mensaje(f"Error: {e}")
                            intentos -= 1
                    if intentos == 0:
                        self.vista.mostrar_mensaje(
                            "Intentos agotados. Regresando al menú principal."
                        )

                case "5":  # Ver etiquetas de una tarea
                    intentos = 3
                    while intentos > 0:
                        try:
                            id_tarea = self.vista.obtener_id_tarea()
                            if self.modelo.validar_id(id_tarea):
                                etiquetas = self.modelo.obtener_etiquetas_por_tarea(
                                    id_tarea
                                )
                                if etiquetas:
                                    color_etiquetas = self.modelo.asignar_color_etiquetas(etiquetas[1].split(", "))
                                    self.vista.mostrar_mensaje(
                                        f"Tarea: {etiquetas[0]}, Etiquetas:"
                                    )
                                    for etiqueta_color in color_etiquetas:
                                        self.vista.mostrar_mensaje(
                                            f"  - {etiqueta_color}"
                                        )
                                    self.vista.mostrar_mensaje(f"Estado: {etiquetas[2]}")
                                else:
                                    self.vista.mostrar_mensaje(
                                        "Esta tarea no tiene etiquetas asignadas."
                                    )
                                break
                            else:
                                self.vista.mostrar_mensaje("ID de tarea no encontrado.")
                                intentos -= 1
                        except Exception as e:
                            self.vista.mostrar_mensaje(f"Error: {e}")
                            intentos -= 1
                    if intentos == 0:
                        self.vista.mostrar_mensaje(
                            "Intentos agotados. Regresando al menú principal."
                        )

                case "6":  # Salir
                    self.vista.mostrar_mensaje(
                        "Saliendo del gestor de tareas. ¡Hasta pronto!"
                    )
                    break

                case _:
                    self.vista.mostrar_mensaje(
                        "Opción no válida. Por favor, intente nuevamente."
                    )
