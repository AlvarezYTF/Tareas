from binascii import Error
from models import conection


class ModeloEtiqueta(conection.Conection):
    def __init__(self):
        super().__init__()

    # Crear la tabla 'etiquetas'
    def crear_tabla(self):
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS etiquetas (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nombre VARCHAR(255) NOT NULL,
                estado BOOLEAN DEFAULT FALSE
            )
            """
        )
        self.conn.commit()

    # Crear la tabla 'tarea_etiqueta' para relacionar tareas con etiquetas
    def crear_tabla_tarea_etiqueta(self):
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS tarea_etiqueta (
                id INT AUTO_INCREMENT PRIMARY KEY,
                id_etiqueta INT NOT NULL,
                id_tarea INT NOT NULL,
                FOREIGN KEY (id_etiqueta) REFERENCES etiquetas(id),
                FOREIGN KEY (id_tarea) REFERENCES tareas(id)
            )
            """
        )
        self.conn.commit()

    # Agregar una nueva etiqueta
    def agregar_etiqueta(self, nombre):
        try:
            self.cursor.execute(
                "INSERT INTO etiquetas (nombre) VALUES (%s)",
                (nombre,),
            )
            self.conn.commit()
            print("Etiqueta agregada correctamente.")
        except Error as e:
            print(f"Error al agregar la etiqueta: {e}")

    # Obtener todas las etiquetas
    def obtener_etiquetas(self):
        try:
            self.cursor.execute("SELECT * FROM etiquetas")
            return self.cursor.fetchall()
        except Error as e:
            print(f"Error al obtener etiquetas: {e}")
            return []

    # Actualizar el estado de una etiqueta
    def actualizar_etiqueta(self, id_etiqueta, estado):
        try:
            self.cursor.execute(
                "UPDATE etiquetas SET estado = %s WHERE id = %s",
                (estado, id_etiqueta),
            )
            self.conn.commit()
            print("Etiqueta actualizada correctamente.")
        except Error as e:
            print(f"Error al actualizar la etiqueta: {e}")

    # Eliminar una etiqueta por su ID
    def eliminar_etiqueta(self, id_etiqueta):
        try:
            self.cursor.execute("DELETE FROM etiquetas WHERE id = %s", (id_etiqueta,))
            self.conn.commit()
            print("Etiqueta eliminada correctamente.")
        except Error as e:
            print(f"Error al eliminar la etiqueta: {e}")

    # Validar si un ID de etiqueta existe
    def validar_id(self, id_etiqueta):
        try:
            self.cursor.execute(
                "SELECT id FROM etiquetas WHERE id = %s", (id_etiqueta,)
            )
            return self.cursor.fetchone() is not None
        except Error as e:
            print(f"Error al validar el ID: {e}")
            return False

    # Validar si un nombre de etiqueta ya existe
    def validar_existencia_nombre(self, nombre):
        try:
            self.cursor.execute(
                "SELECT nombre FROM etiquetas WHERE nombre = %s", (nombre,)
            )
            return self.cursor.fetchone() is not None
        except Error as e:
            print(f"Error al validar el nombre: {e}")
            return False
    
    def validar_nuevo_estado(self, nuevo_estado):
        return nuevo_estado in ["activo", "inactivo"]

    # Validar si un número es entero
    def validar_numero_entero(self, numero):
        return isinstance(numero, int)

    # Cambiar el estado de una etiqueta (booleano a string)
    def cambiar_estado_booleano(self, estado):
        if estado == "activo":
            return 1
        elif estado == "inactivo":
            return 0

    # Obtener el último ID de etiqueta
    def obtener_ultimo_id_etiqueta(self):
        try:
            self.cursor.execute("SELECT MAX(id) FROM etiquetas")
            return self.cursor.fetchone()[0]
        except Error as e:
            print(f"Error al obtener el último ID: {e}")
            return None

    # Obtener etiquetas relacionadas a una tarea específica
    def obtener_etiquetas_por_tarea(self, id_tarea):
        try:
            self.cursor.execute(
                """
                SELECT e.nombre 
                FROM etiquetas e
                JOIN tarea_etiqueta te ON e.id = te.id_etiqueta
                WHERE te.id_tarea = %s
                """,
                (id_tarea,),
            )
            return self.cursor.fetchall()
        except Error as e:
            print(f"Error al obtener etiquetas por tarea: {e}")
            return []

    # Relacionar una etiqueta con una tarea
    def asignar_etiqueta_a_tarea(self, id_etiqueta, id_tarea):
        try:
            self.cursor.execute(
                "INSERT INTO tarea_etiqueta (id_etiqueta, id_tarea) VALUES (%s, %s)",
                (id_etiqueta, id_tarea),
            )
            self.conn.commit()
            print("Etiqueta asignada a la tarea correctamente.")
        except Error as e:
            print(f"Error al asignar la etiqueta a la tarea: {e}")

    # Validar si una etiqueta ya está asignada a una tarea
    def etiqueta_ya_asignada(self, id_etiqueta, id_tarea):
        try:
            self.cursor.execute(
                "SELECT * FROM tarea_etiqueta WHERE id_etiqueta = %s AND id_tarea = %s",
                (id_etiqueta, id_tarea),
            )
            return self.cursor.fetchone() is not None
        except Error as e:
            print(f"Error al validar si la etiqueta ya está asignada: {e}")
            return False
