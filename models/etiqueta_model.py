from models import conection


class ModeloEtiqueta:
    def __init__(self):
        self.conn = conection.Conection()
        self.cursor = self.conn.cursor

    def crear_tabla(self):
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS etiquetas (id INT AUTO_INCREMENT PRIMARY KEY, nombre VARCHAR(255) NOT NULL, estado BOOLEAN DEFAULT FALSE)"
        )
        self.conn.commit

    def crear_tabla_tarea_etiqueta(self):
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS tarea_etiqueta (id INT AUTO_INCREMENT PRIMARY KEY, id_etiqueta int, id_tarea int, FOREIGN KEY (id_etiqueta) REFERENCES etiquetas(id), FOREIGN KEY (id_tarea) REFERENCES tareas(id))"
        )
        self.conn.commit

    def agregar_etiqueta(self, etiqueta):
        self.cursor.execute(
            """
                INSERT INTO etiquetas (nombre) VALUES (%s)                            
            """,
            etiqueta,
        )
        self.conn.commit

    def obtener_etiquetas(self):
        self.cursor.execute(
            """
                SELECT * FROM etiquetas
            """
        )
        return self.cursor.fetchall()

    def actualizar_etiqueta(self, id_etiqueta, estado):
        self.cursor.execute(
            """
                UPDATE etiquetas SET estado = %s WHERE id = %s        
            """,
            id_etiqueta,
            estado,
        )
        self.conn.commit

    def eliminar_etiqueta(self, id_etiqueta):
        self.cursor.execute(
            """
            DELETE FROM etiquetas WHERE id = %s
        """,
            id_etiqueta,
        )

    def validar_id(self, id_etiqueta):  # sourcery skip: use-any, use-next
        for tarea in self.obtener_etiquetas():
            if tarea[0] == id_etiqueta:
                return True
        return False

# if __name__ == "__main__":
#     etiqueta = ModeloEtiqueta()
#     etiqueta.crear_tabla_TareaEtiqueta()
