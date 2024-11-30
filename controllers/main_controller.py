from views.main_view import MainView
from controllers.tarea_controller import ControladorTarea
from controllers.etiqueta_controller import ControladorEtiqueta


class MainController:
    def __init__(
        self,
        controlador_tarea: ControladorTarea,
        controlador_etiqueta: ControladorEtiqueta,
    ):
        self.controlador_tarea = controlador_tarea
        self.controlador_etiqueta = controlador_etiqueta
        self.main_view = MainView

    def ejecutar(self):
        while True:
            opcion_principal = self.main_view.mostrar_menu_principal()

            match opcion_principal:
                case "1":  # Gestión de Tareas
                    self.menu_tareas()

                case "2":  # Gestión de Etiquetas
                    self.menu_etiquetas()

                case "3":  # Salir
                    self.main_view.mostrar_mensaje("¡Hasta luego!")
                    break

                case _:
                    self.main_view.mostrar_mensaje(
                        "Opción no válida. Intenta de nuevo."
                    )

    def menu_tareas(self):
            self.controlador_tarea.ejecutar()

    def menu_etiquetas(self):
            self.controlador_etiqueta.ejecutar()
