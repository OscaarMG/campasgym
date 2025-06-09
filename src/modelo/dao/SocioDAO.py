from src.modelo.conexion.Conexion import Conexion
from datetime import datetime, timedelta

class SocioDAO(Conexion):
    
    def obtener_clases_disponibles(self):
        try:
            query = """
            SELECT c.id_clase, c.nombre, c.horario, c.cupo_maximo, COUNT(i.id_socio) AS apuntados
            FROM clases c
            LEFT JOIN inscripciones i ON c.id_clase = i.id_clase
            WHERE c.horario > CURRENT_TIMESTAMP
            GROUP BY c.id_clase
            HAVING COUNT(i.id_socio) < c.cupo_maximo
            """
            cursor = self.getCursor()
            cursor.execute(query)
            return cursor.fetchall()
        except Exception as e:
            print("Error al obtener clases disponibles:", e)
            return []
    
    def insertar_inscripcion(self, inscribirseVO):
        try:
            fecha_inscripcion_dt = datetime.now()
            fecha_incripcion = fecha_inscripcion_dt.strftime("%Y-%m-%d %H:%M:%S")
            cursor = self.getCursor()
            cursor.execute("""
                INSERT INTO inscripciones (id_socio, id_clase, fecha_inscripcion)
                VALUES (?, ?, ?)
            """, [inscribirseVO._id_socio, inscribirseVO._id_clase, fecha_incripcion])
            return True
        except Exception as e:
            print("Error al insertar inscripción:", e)
            return False
        
    def obtener_rutinas_asignadas(self, id_socio):
        try:
            cursor = self.getCursor()
            cursor.execute("""
                SELECT r.id_rutina, r.nombre, r.descripcion
                FROM RutinaSocio rs
                JOIN Rutinas r ON rs.id_rutina = r.id_rutina
                WHERE rs.id_socio = ?
            """, (id_socio,))
            return cursor.fetchall()
        except Exception as e:
            print("Error al insertar obtener_rutinas_asignadas:", e)
            return False

    def eliminar_rutina_asignada(self, eliminarVO):
        try:
            cursor = self.getCursor()
            cursor.execute("""
                DELETE FROM RutinaSocio
                WHERE id_socio = ? AND id_rutina = ?
            """, (eliminarVO._id_socio, eliminarVO._id_elemento))
            return True
        except Exception as e:
            print("Error al insertar eliminar_rutina_asignada:", e)
            return False

    def solicitar_rutina(self, solicitarVO):
        try:
            cursor = self.getCursor()
            cursor.execute("""
                INSERT INTO solicitudes_rutina (id_socio, objetivo)
                VALUES (?, ?)
            """, (solicitarVO._id_socio, solicitarVO._objetivo))
            return True
        except Exception as e:
            print("Error al insertar solicitar_rutina:", e)
            return False
        
    def obtener_dietas_asignadas(self, id_socio):
        try:
            cursor = self.getCursor()
            cursor.execute("""
                SELECT d.id_dieta, d.nombre, d.descripcion
                FROM DietaSocio ds
                JOIN Dietas d ON ds.id_dieta = d.id_dieta
                WHERE ds.id_socio = ?
            """, (id_socio,))
            return cursor.fetchall()
        except Exception as e:
            print("Error al insertar obtener_dietas_asignadas:", e)
            return False

    def eliminar_dieta_asignada(self, eliminarVO):
        try:
            cursor = self.getCursor()
            cursor.execute("""
                DELETE FROM DietaSocio
                WHERE id_socio = ? AND id_dieta = ?
            """, (eliminarVO._id_socio, eliminarVO._id_elemento))
            return True
        except Exception as e:
            print("Error al insertar eliminar_dieta_asignada:", e)
            return False

    def solicitar_dieta(self, solicitarVO):
        try:
            cursor = self.getCursor()
            cursor.execute("""
                INSERT INTO solicitudes_dieta (id_socio, objetivo)
                VALUES (?, ?)
            """, (solicitarVO._id_socio, solicitarVO._objetivo))
            return True
        except Exception as e:
            print("Error al insertar solicitar_dieta:", e)
            return False

    def eliminar_socio(self, id_socio):
        try:
            cursor = self.getCursor()
            sql = "DELETE FROM socios WHERE id_socio = ?"
            cursor.execute(sql, (id_socio,))
        except Exception as e:
            print("Error al eliminar socio:", e)
            return False

    def renovar_suscripcion(self, id_socio, tipo):
        try:
            conexion = Conexion().createConnection()
            cursor = conexion.cursor()
            nueva_fecha = (datetime.now() + timedelta(days=30)).strftime('%Y-%m-%d')
            sql = "UPDATE Membresias SET tipo = ?, fecha_fin = ? WHERE id_socio = ?"
            cursor.execute(sql, (tipo, nueva_fecha, id_socio))
            cursor.close()
        except Exception as e:
            print("Error al renovar suscripción:", e)
