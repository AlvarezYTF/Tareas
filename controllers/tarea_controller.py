from models import etiqueta_model
from views import etiqueta_view
from colorama import Back, Fore, Style, init
init()

# Clase que contrala las tareas
class ControladorTarea:
    # Constructor para conectarse al modelo y la vista
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista
        self.class_etiqueta_model = etiqueta_model.ModeloEtiqueta()
        self.class_etiqueta_view = etiqueta_view.VistaEtiqueta()

    # Funcion para ejecutar las opciones
    def ejecutar(self):  # sourcery skip: de-morgan, low-code-quality
        # Se llama del script modelo para crear la tabla en BD
        self.modelo.crear_tabla()
        while True:
            # Se llama desde la vista la funcion de mostrar menu
            self.vista.mostrar_menu()
            # Match para manejar diferentes opciones
            match self.vista.obtener_opcion_menu():
                case "1":
                    try:
                        while True:
                            # Obtener título y descripción de la tarea
                            titulo = self.vista.obtener_titulo()
                            descripcion = self.vista.obtener_descripcion()

                            # Validar si el título ya existe
                            if self.modelo.validar_existencia_titulo(titulo):
                                # Pedir un nuevo título válido si ya existe
                                while True:
                                    titulo = self.vista.obtener_titulo_valido()
                                    if not self.modelo.validar_existencia_titulo(
                                        titulo
                                    ):
                                        break
                            # Agregar tarea
                            self.modelo.agregar_tarea(titulo, descripcion)
                            # Solicitar etiquetas y permitir añadir múltiples
                            if not self.vista.obtener_confirmacion() != "s":
                                # Agregar la primera etiqueta
                                id_tarea = self.modelo.obtener_ultimo_id_tarea()
                                etiquetas = (
                                    self.class_etiqueta_model.obtener_etiquetas()
                                )
                                self.class_etiqueta_view.mostrar_etiquetas(etiquetas)
                                while True:
                                    id_etiqueta = (
                                        self.class_etiqueta_view.obtener_id_etiqueta()
                                    )
                                    if self.class_etiqueta_model.validar_id(
                                        id_etiqueta
                                    ):
                                        if not self.modelo.etiqueta_ya_asignada(
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
                                                "Esta etiqueta ya está asignada a la tarea. Elige otra.\n"
                                            )
                                    else:
                                        self.vista.mostrar_mensaje(
                                            "El id de la etiqueta no existe. Ingresa uno de los que están en la lista\n"
                                        )
                                while (
                                    not self.vista.obtener_confirmacion_etiquetas()
                                    != "s"
                                ):
                                    id_tarea = self.modelo.obtener_ultimo_id_tarea()
                                    etiquetas = (
                                        self.class_etiqueta_model.obtener_etiquetas()
                                    )
                                    self.class_etiqueta_view.mostrar_etiquetas(
                                        etiquetas
                                    )
                                    while True:
                                        id_etiqueta = (
                                            self.class_etiqueta_view.obtener_id_etiqueta()
                                        )
                                        # Verificar si el id de la etiqueta es válido
                                        if (
                                            self.class_etiqueta_model.validar_id(
                                                id_etiqueta
                                            )
                                            == True
                                        ):
                                            # Verificar si ya se asignó la etiqueta a esta tarea
                                            if (
                                                self.modelo.etiqueta_ya_asignada(
                                                    id_tarea, id_etiqueta
                                                )
                                                == False
                                            ):
                                                if id_etiqueta and id_tarea:
                                                    self.modelo.agregar_etiqueta_tarea(
                                                        id_tarea, id_etiqueta
                                                    )
                                                    break
                                            else:
                                                self.vista.mostrar_mensaje(
                                                    "Esta etiqueta ya está asignada a la tarea. Elige otra.\n"
                                                )
                                        else:
                                            self.vista.mostrar_mensaje(
                                                "El id de la etiqueta no existe. Ingresa uno de los que están en la lista\n"
                                            )
                            self.vista.mostrar_mensaje("¡Tarea agregada correctamente!")
                            break
                    except Exception as e:
                        self.vista.mostrar_mensaje(
                            f"Error al agregar la tarea: typeError({e})"
                        )

                case "2":
                    # try:
                    tareas = self.modelo.obtener_tareas()
                    self.vista.mostrar_tareas(tareas)
                # except Exception as e:
                #     self.vista.mostrar_mensaje(
                #         f"Error al mostras la tareas: typeError({e})"
                #     )
                case "3":
                    # try:
                    while True:
                        id_tarea = self.vista.obtener_id_tarea()
                        if id_tarea > 0:
                            if self.modelo.validar_id(id_tarea):
                                while True:
                                    nuevo_estado = self.vista.obtener_nuevo_estado()
                                    if self.modelo.validar_nuevo_estado(
                                            nuevo_estado
                                        ):
                                        bool_estado = (
                                            self.modelo.cambiar_estado_booleano(
                                                nuevo_estado
                                            )
                                        )

                                        if bool_estado == 1:
                                            self.modelo.actualizar_tarea(
                                                id_tarea, bool_estado
                                            )
                                            
                                            break

                                            self.vista.mostrar_mensaje(
                                                "¡Estado de la tarea actualizado!"
                                            )
                                            break
                                        elif self.modelo.cambiar_estado_booleano(nuevo_estado) == 0:
                                            print("error")
                                            break
                                            self.modelo.actualizar_tarea(
                                                    id_tarea, bool_estado
                                                )
                                            self.vista.mostrar_mensaje(
                                                    "¡Estado de la tarea actualizado!"
                                                )
                                            break
                                    else:
                                        print(
                                                "Estado no existe, ingresa completada/pendiente"
                                            )
                                break
                            else:
                                self.vista.mostrar_mensaje("Id no encontrado")
                        else:
                            self.vista.mostrar_mensaje(
                                    "Ingresa un numero mayor que Cero"
                                )
                # except TypeError as e:
                #     self.vista.mostrar_mensaje("Numero de ID no valido")
                case "4":
                    try:
                        while True:
                            id_tarea = self.vista.obtener_id_tarea()
                            if id_tarea > 0:
                                if self.modelo.validar_id(id_tarea):
                                    confirmacion = (
                                        input(
                                            "¿Estás seguro de que deseas eliminar esta tarea? (s/n): "
                                        )
                                        .strip()
                                        .lower()
                                    )
                                    if confirmacion == "s":
                                        self.modelo.eliminar_tarea(id_tarea)
                                        self.vista.mostrar_mensaje(
                                            "¡Tarea eliminada correctamente!"
                                        )
                                    else:
                                        self.vista.mostrar_mensaje(
                                            "Eliminación cancelada."
                                        )
                                    break
                                else:
                                    self.vista.mostrar_mensaje("\nId no encontrado")
                            else:
                                self.vista.mostrar_mensaje(
                                    "Ingresa un numero mayor que Cero"
                                )
                    except TypeError as e:
                        self.vista.mostrar_mensaje("Numero de ID no valido")
                case "5":
                    try:
                        tareas = self.modelo.obtener_tareas()
                        self.vista.mostrar_tareas(tareas)
                        # Obtener el ID de la tarea
                        id_tarea = self.vista.obtener_id_tarea()

                        # Validar que el ID exista
                        if not self.modelo.validar_id(id_tarea):
                            self.vista.mostrar_mensaje(
                                "El ID de la tarea no existe. Intenta con otro."
                            )
                            return

                        if result := (
                            self.modelo.obtener_etiquetas_por_tarea(
                                id_tarea
                            )
                        ):
                            self.vista.mostrar_mensaje(
                                f"Tarea: {result[0]}, Etiquetas " + Fore.BLUE + Style.BRIGHT + f"[{result[1]}]" + Style.RESET_ALL + f", Estado: {result[2]}"
                            )

                        else:
                            self.vista.mostrar_mensaje(
                                "Esta tarea no tiene etiquetas asignadas."
                            )
                    except Exception as e:
                        self.vista.mostrar_mensaje(
                            f"Error al mostrar las etiquetas: {e}"
                        )

                case "6":
                    self.vista.mostrar_mensaje(
                        "Saliendo del gestor de tareas. ¡Hasta pronto!"
                    )
                    break
                case _:
                    self.vista.mostrar_mensaje(
                        "Opción no válida. Por favor, intente de nuevo."
                    )
