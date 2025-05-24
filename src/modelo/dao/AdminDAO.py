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
        
    def obtener_socios(self):
        try:
            cursor = self.getCursor()
            cursor.execute("SELECT s.id_socio, s.nombre, s.apellidos, s.dni, s.usuario, s.email, m.tipo FROM socios s LEFT JOIN membresias m ON s.id_socio = m.id_socio")
            socios = cursor.fetchall()
            return socios
        except Exception as e:
            print(f"Error en obtener_socios: {e}")
            return []

    def eliminar_socio(self, id_socio):
        try:
            cursor = self.getCursor()
            cursor.execute("DELETE FROM Membresias WHERE id_socio = ?", [id_socio])
            cursor.execute("DELETE FROM Socios WHERE id_socio = ?", [id_socio])
            return True
        except Exception as e:
            print(f"Error en eliminar_socio: {e}")
            return False

    def modificar_socio(self, UserVO):
        try:
            cursor = self.getCursor()
            cursor.execute(
                "UPDATE Socios SET nombre = ?, apellidos = ?, dni = ?, usuario = ?, email = ? WHERE id_socio = ?",
                [UserVO._nombre, UserVO._apellidos, UserVO._DNI, UserVO._usuario, UserVO._email, UserVO._id]
            )
            cursor.execute(
                "UPDATE Membresias SET tipo = ? WHERE id_socio = ?",
                [UserVO._tipo, UserVO._id]
            )
            return True
        except Exception as e:
            print(f"Error en modificar_socio: {e}")
            return False
        
    def obtener_entrenadores(self):
        try:
            cursor = self.getCursor()
            cursor.execute("""SELECT id_entrenador, nombre, apellido1, apellido2, usuario, especialidad, email, telefono, n_cuenta, horario, fecha_ingreso FROM entrenadores""")
            return cursor.fetchall()
        except Exception as e:
            print(f"Error en obtener_entrenadores: {e}")
            return []

    def insertar_entrenador(self, entrenadorVO):
        try:
            cursor = self.getCursor()
            fecha_ingreso = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            cursor.execute("""
                INSERT INTO entrenadores 
                (nombre, apellido1, apellido2, usuario, contrasena, especialidad, email, telefono, n_cuenta, horario, fecha_ingreso)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                [entrenadorVO._nombre, entrenadorVO._apellido1, entrenadorVO._apellido2, entrenadorVO._usuario, entrenadorVO._contrasena, entrenadorVO._especialidad,
                 entrenadorVO._email, entrenadorVO._telefono, entrenadorVO._n_cuenta, entrenadorVO._horario, fecha_ingreso])
            return True
        except Exception as e:
            print(f"Error en insertar_entrenador: {e}")
            return False

    def eliminar_entrenador(self, id_entrenador):
        try:
            cursor = self.getCursor()
            cursor.execute("DELETE FROM entrenadores WHERE id_entrenador = ?", [id_entrenador])
            return True
        except Exception as e:
            print(f"Error en eliminar_entrenador: {e}")
            return False

    def modificar_entrenador(self, entrenadorVO):
        try:
            cursor = self.getCursor()
            cursor.execute("UPDATE entrenadores SET nombre = ?, apellido1 = ?, apellido2 = ?, usuario = ?, contrasena = ?, especialidad = ?, email = ?, telefono = ?, n_cuenta = ?, horario = ? WHERE id_entrenador = ?", [
                entrenadorVO._nombre, entrenadorVO._apellido1, entrenadorVO._apellido2, entrenadorVO._usuario, entrenadorVO._contrasena, entrenadorVO._especialidad,
                entrenadorVO._email, entrenadorVO._telefono, entrenadorVO._n_cuenta, entrenadorVO._horario, entrenadorVO._id_entrenador])
            return True
        except Exception as e:
            print(f"Error en modificar_entrenador: {e}")
            return False
        
    def obtener_materiales(self):
        try:
            cursor = self.getCursor()
            cursor.execute("SELECT id_material, nombre, cantidad, estado, ubicacion, fecha_ingreso FROM Material")
            return cursor.fetchall()
        except Exception as e:
            print(f"Error en obtener_materiales: {e}")
            return []

    def insertar_material(self, materialVO):
        try:
            cursor = self.getCursor()
            fecha_ingreso = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            cursor.execute("""
                INSERT INTO Material (nombre, cantidad, estado, ubicacion, fecha_ingreso)
                VALUES (?, ?, ?, ?, ?)
            """, [materialVO._nombre, materialVO._cantidad, materialVO._estado, materialVO._ubicacion, fecha_ingreso])
            return True
        except Exception as e:
            print(f"Error en insertar_material: {e}")
            return False

    def modificar_material(self, materialVO):
        try:
            cursor = self.getCursor()
            print(materialVO._nombre)
            print(materialVO._id_material)
            cursor.execute("""
                UPDATE Material SET nombre = ?, cantidad = ?, estado = ?, ubicacion = ?
                WHERE id_material = ?
            """, [materialVO._nombre, materialVO._cantidad, materialVO._estado, materialVO._ubicacion, materialVO._id_material])
            return True
        except Exception as e:
            print(f"Error en modificar_material: {e}")
            return False

    def eliminar_material(self, id_material):
        try:
            cursor = self.getCursor()
            cursor.execute("DELETE FROM Material WHERE id_material = ?", [id_material])
            return True
        except Exception as e:
            print(f"Error en eliminar_material: {e}")
            return False

    def obtener_adms(self):
        try:
            cursor = self.getCursor()
            cursor.execute("""SELECT id_admin, nombre, apellido1, apellido2, usuario, puesto, email, telefono, n_cuenta, horario, fecha_ingreso FROM administracion""")
            return cursor.fetchall()
        except Exception as e:
            print(f"Error en obtener_adms: {e}")
            return []

    def insertar_adm(self, admVO):
        try:
            cursor = self.getCursor()
            fecha_ingreso = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            cursor.execute("""
                INSERT INTO administracion 
                (nombre, apellido1, apellido2, usuario, contrasena, puesto, email, telefono, n_cuenta, horario, fecha_ingreso)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                [admVO._nombre, admVO._apellido1, admVO._apellido2, admVO._usuario, admVO._contrasena, admVO._puesto,
                 admVO._email, admVO._telefono, admVO._n_cuenta, admVO._horario, fecha_ingreso])
            return True
        except Exception as e:
            print(f"Error en insertar_adm: {e}")
            return False

    def eliminar_adm(self, id_adm):
        try:
            cursor = self.getCursor()
            cursor.execute("DELETE FROM administracion WHERE id_admin = ?", [id_adm])
            return True
        except Exception as e:
            print(f"Error en eliminar_adm: {e}")
            return False

    def modificar_adm(self, admVO):
        try:
            cursor = self.getCursor()
            cursor.execute("UPDATE administracion SET nombre = ?, apellido1 = ?, apellido2 = ?, usuario = ?, contrasena = ?, puesto = ?, email = ?, telefono = ?, n_cuenta = ?, horario = ? WHERE id_admin = ?", [
                admVO._nombre, admVO._apellido1, admVO._apellido2, admVO._usuario, admVO._contrasena, admVO._puesto,
                admVO._email, admVO._telefono, admVO._n_cuenta, admVO._horario, admVO._id_adm])
            return True
        except Exception as e:
            print(f"Error en modificar_adm: {e}")
            return False