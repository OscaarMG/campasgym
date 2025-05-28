from src.modelo.conexion.Conexion import Conexion
from datetime import datetime

class EntrenadorDAO(Conexion):

    def obtener_id_entrenador_por_usuario(self, nombre_usuario):
        try:
            cursor = self.getCursor()
            cursor.execute("SELECT id_entrenador FROM entrenadores WHERE usuario = ?", (nombre_usuario,))
            resultado = cursor.fetchone()
            if resultado:
                return resultado[0]
            else:
                return None
        except Exception as e:
            print(f"Error al buscar ID del entrenador: {e}")
            return None

    def insertar_clase(self, claseVO):
        try:
            cursor = self.getCursor()
            cursor.execute("""
                INSERT INTO clases (nombre, descripcion, horario, lugar, cupo_maximo, id_entrenador)
                VALUES (?, ?, ?, ?, ?, ?)""",
                [claseVO._nombre, claseVO._descripcion, claseVO._horario, claseVO._lugar, claseVO._cupo_maximo, claseVO._id_entrenador])
            return True
        except Exception as e:
            print(f"Error al insertar clase: {e}")
            return False
        
    def obtener_solicitudes_rutinas(self):
        try:
            query = """
                SELECT s.id_solicitud, s.id_socio, s.objetivo, s.fecha_solicitud
                FROM solicitudes_rutina s
                JOIN membresias m ON s.id_socio = m.socio_id
                WHERE m.fecha_fin > CURRENT_DATE
            """
            cursor = self.getCursor()
            cursor.execute(query)
            return cursor.fetchall()
        except Exception as e:
            print(f"Error al obtener solicitudes: {e}")
            return False

    def obtener_rutinas(self):
        try:
            query = "SELECT id_rutina, nombre, descripcion FROM rutinas"
            cursor = self.getCursor()
            cursor.execute(query)
            return cursor.fetchall()
        except Exception as e:
            print(f"Error al insertar obtener rutinas: {e}")
            return False

    def crear_rutina(self, rutinaVO):
        try:
            fecha = datetime.now().strftime("%Y-%m-%d")
            cursor = self.getCursor()
            cursor.execute("INSERT INTO rutinas (nombre, descripcion, fecha_creacion) VALUES (?, ?, ?)", (rutinaVO._nombre, rutinaVO._descripcion, fecha))
            return True
        except Exception as e:
            print(f"Error al insertar crear rutina: {e}")
            return False


    def asignar_rutina(self, asignarVO):
        try:
            fecha = datetime.now().strftime("%Y-%m-%d")
            cur = self.getCursor()
            cur.execute("INSERT INTO RutinaSocio (id_socio, id_rutina, fecha) VALUES (?, ?, ?)",
                        (asignarVO._id_socio, asignarVO._id_asignar, fecha))
            cur.execute("DELETE FROM solicitudes_rutina WHERE id_socio = ? AND id_solicitud = ?", (asignarVO._id_socio, asignarVO._id_solicitud))
            return True
        except Exception as e:
            print(f"Error al insertar asignar rutina: {e}")
            return False

    def eliminar_rutina(self, id_rutina):
        try:
            cursor = self.getCursor()
            cursor.execute("DELETE FROM rutinas WHERE id_rutina = ?", (id_rutina,))
            cursor.execute("DELETE FROM RutinaSocio WHERE id_rutina = ?", (id_rutina,))
            return True
        except Exception as e:
            print(f"Error al eliminar rutina: {e}")
            return False
        
    
    def obtener_solicitudes_dietas(self):
        try:
            query = """
                SELECT s.id_solicitud, s.id_socio, s.objetivo, s.fecha_solicitud
                FROM solicitudes_dieta s
                JOIN membresias m ON s.id_socio = m.socio_id
                WHERE m.fecha_fin > CURRENT_DATE
            """
            cursor = self.getCursor()
            cursor.execute(query)
            return cursor.fetchall()
        except Exception as e:
            print(f"Error al obtener solicitudes: {e}")
            return False

    def obtener_dietas(self):
        try:
            query = "SELECT id_dieta, nombre, descripcion FROM dietas"
            cursor = self.getCursor()
            cursor.execute(query)
            return cursor.fetchall()
        except Exception as e:
            print(f"Error al insertar obtener dietas: {e}")
            return False

    def crear_dieta(self, dietaVO):
        try:
            fecha = datetime.now().strftime("%Y-%m-%d")
            cursor = self.getCursor()
            cursor.execute("INSERT INTO dietas (nombre, descripcion, fecha_creacion) VALUES (?, ?, ?)", (dietaVO._nombre, dietaVO._descripcion, fecha))
            return True
        except Exception as e:
            print(f"Error al insertar crear dieta: {e}")
            return False


    def asignar_dieta(self, asignarVO):
        try:
            fecha = datetime.now().strftime("%Y-%m-%d")
            cur = self.getCursor()
            cur.execute("INSERT INTO DietaSocio (id_socio, id_dieta, fecha) VALUES (?, ?, ?)",
                        (asignarVO._id_socio, asignarVO._id_asignar, fecha))
            cur.execute("DELETE FROM solicitudes_dieta WHERE id_socio = ? AND id_solicitud = ?", (asignarVO._id_socio, asignarVO._id_solicitud))
            return True
        except Exception as e:
            print(f"Error al insertar asignar dieta: {e}")
            return False

    def eliminar_dieta(self, id_dieta):
        try:
            cursor = self.getCursor()
            cursor.execute("DELETE FROM dietas WHERE id_dieta = ?", (id_dieta,))
            cursor.execute("DELETE FROM DietaSocio WHERE id_dieta = ?", (id_dieta,))
            return True
        except Exception as e:
            print(f"Error al eliminar dieta: {e}")
            return False