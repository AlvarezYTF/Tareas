from models import conection

# Clase para manejar las funciones de las tareas con la BD
class ModeloTarea:
    # Contructor para conectarme a la BD
    def __init__(self):
        self.conn = conection.Conection()
        self.cursor = self.conn.cursor

    # Crear la tabla si no existe en la BD
    def crear_tabla(self):
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS tareas (
                id INT AUTO_INCREMENT PRIMARY KEY,
                titulo VARCHAR(255) NOT NULL,
                descripcion TEXT,
                estado BOOLEAN DEFAULT FALSE
            )
        """
        )
        self.conn.commit

    # Funcion para agregar tarea en BD
    def agregar_tarea(self, titulo, descripcion):
        self._extracted_from_actualizar_tarea_2(
            "INSERT INTO tareas (titulo, descripcion) VALUES (%s, %s)",
            titulo,
            descripcion,
        )

    # Funcion para obtener las tareas de la BD
    def obtener_tareas(self):
        self.cursor.execute("SELECT * FROM tareas")
        return self.cursor.fetchall()

    # Funcion para actualizar las tarea de la BD
    def actualizar_tarea(self, id_tarea, estado):
        query = "UPDATE tareas SET estado = %s WHERE id = %s"
        self._extracted_from_actualizar_tarea_2(
            query, estado, id_tarea
        )

    # TODO Rename this here and in `agregar_tarea` and `actualizar_tarea`
    def _extracted_from_actualizar_tarea_2(self, arg0, arg1, arg2):
        
        a = self.conn.cursor.execute(arg0, (arg1, arg2,))
        print(a, arg0, arg1, arg2)
        # self.cursor.execute(consulta, (arg1, arg2,))
        # self.conn.commit

    # Funcion para eliminar tarea de la BD
    def eliminar_tarea(self, id_tarea):
        consulta = "DELETE FROM tareas WHERE id = %s"
        self.cursor.execute(consulta, (id_tarea,))
        self.conn.commit

    def agregar_etiqueta_tarea(self, id_tarea, id_etiqueta):
        self.cursor.execute(
            """INSERT INTO tarea_etiqueta (id_etiqueta, id_tarea) VALUES (%s, %s)""",
            (id_etiqueta, id_tarea),
        )
        self.conn.commit

    # Funcion para validar que existe el ID
    def validar_id(self, id_tarea):
        for tarea in self.obtener_tareas():
            if tarea[0] == id_tarea:
                return id_tarea

    # Funcion para determinar la existencia de un titulo
    def validar_existencia_titulo(self, titulo):
        for tarea in self.obtener_tareas():
            return tarea[1] == titulo

    # Funcion para validar de que un numero sea entero
    def validar_numero_entero(self, numero):
        return isinstance(numero, int)

    # Funcion para validar de que el usuario halla ingresado un estado correcto
    def validar_nuevo_estado(self, nuevo_estado):
        return nuevo_estado in ["pendiente", "completada"]

    def obtener_ultimo_id_tarea(self):
        self.cursor.execute("""SELECT MAX(id) FROM tareas""")
        return self.cursor.fetchone()[0]    

    def etiqueta_ya_asignada(self, id_tarea, id_etiqueta):
        # sourcery skip: use-any, use-next
        self.cursor.execute("SELECT id_tarea, id_etiqueta FROM tarea_etiqueta")
        result = self.cursor.fetchall()
        for etiquetas_tareas_ids in result:
            if etiquetas_tareas_ids[0] == id_tarea and etiquetas_tareas_ids[0] == id_etiqueta:
                return True
        return False

    def obtener_etiquetas_por_tarea(self, id_tarea):
        self.cursor.execute("""
            SELECT t.titulo, GROUP_CONCAT(e.nombre SEPARATOR ', '), t.estado AS etiquetas
            FROM tareas t
            JOIN tarea_etiqueta te ON t.id = te.id_tarea
            JOIN etiquetas e ON te.id_etiqueta = e.id
            WHERE t.id = %s
            GROUP BY t.id;
        """, (id_tarea,))
        return self.cursor.fetchone()

    def cambiar_estado_booleano(self, estado):
        if estado == "completada":
            return 1
        elif estado == "pendiente":
            return 0


""" if __name__ == "__main__":
    modelotarea = ModeloTarea()
    print(modelotarea.cambiar_estado_booleano("completada")) """
