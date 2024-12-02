import mysql.connector
from mysql.connector import Error


class Conection:
    def __init__(self):
        try:
            self.conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="gestor_tareas",
                charset="utf8mb4"
            )
            if not self.conn.is_connected():
                raise Error("No se pudo establecer la conexión.")
            self.cursor = self.conn.cursor()
            self.commit = self.conn.commit()
        except Error as e:
            print(f"Error al conectar con la base de datos: {e}")
            self.conn = None
            self.cursor = None

    def cerrar_conexion(self):
        if self.conn and self.conn.is_connected():
            try:
                self.cursor.close()
                self.conn.close()
                print("Conexión cerrada correctamente.")
            except Error as e:
                print(f"Error al cerrar la conexión: {e}")
        else:
            print("No hay conexión activa para cerrar.")
