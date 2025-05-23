from src.modelo.conexion.Conexion import Conexion
from datetime import datetime
from dateutil.relativedelta import relativedelta

class AdminDAO(Conexion):

    def insertar_usuario(self, UserVO):
        try:
            cursor = self.getCursor()
            fecha_alta_dt = datetime.now()
            fecha_alta = fecha_alta_dt.strftime("%Y-%m-%d %H:%M:%S")
            fecha_fin_dt = fecha_alta_dt + relativedelta(months=1)
            fecha_fin = fecha_fin_dt.strftime("%Y-%m-%d %H:%M:%S")
            cursor.execute(
                "INSERT INTO Socios (nombre, apellidos, DNI, usuario, contrasena, email, fecha_alta) VALUES (?, ?, ?, ?, ?, ?, ?)",
                [UserVO._nombre, UserVO._apellidos, UserVO._DNI, UserVO._usuario, UserVO._contrasena, UserVO._email, fecha_alta]
            )
            cursor.execute(
                "SELECT id_socio FROM Socios WHERE usuario = ?",
                [UserVO._usuario]
            )
            id_socio = cursor.fetchone()
            if id_socio:
                cursor.execute(
                    "INSERT INTO Membresias (id_socio, fecha_inicio, fecha_fin, tipo) VALUES (?, ?, ?, ?)",
                    [id_socio[0], fecha_alta, fecha_fin, UserVO._tipo]
                )
            return True
        except Exception as e:
            print(f"Error en insertar_usuario: {e}")
            return False