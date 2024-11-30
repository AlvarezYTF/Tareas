from models.tarea_model import ModeloTarea
from views.tarea_view import VistaTarea
from controllers.tarea_controller import ControladorTarea
from models.etiqueta_model import ModeloEtiqueta
from views.etiqueta_view import VistaEtiqueta
from controllers.etiqueta_controller import ControladorEtiqueta
from controllers.main_controller import MainController

if __name__ == "__main__":
    # Crear instancias de modelos y vistas
    modeloTarea = ModeloTarea()
    vistaTarea = VistaTarea()
    controladorTarea = ControladorTarea(modeloTarea, vistaTarea)

    modeloEtiqueta = ModeloEtiqueta()
    vistaEtiqueta = VistaEtiqueta()
    controladorEtiqueta = ControladorEtiqueta(modeloEtiqueta, vistaEtiqueta)

    # Crear y ejecutar el controlador principal
    main_controller = MainController(controladorTarea, controladorEtiqueta)
    main_controller.ejecutar()
