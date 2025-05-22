from src.modelo.conexion.Conexion import Conexion

class UserDAO(Conexion):
    def consultaLogin(self, loginVO):
        try:
            cursor = self.getCursor()
            
            # Consulta en tabla 1: administradores
            cursor.execute(
                "SELECT 'administrativo' as tipo FROM administracion WHERE usuario = ? AND contrasena = ?",
                [loginVO.usuario, loginVO.password]
            )
            resultado = cursor.fetchone()
            if resultado:
                return resultado[0]  # Retorna 'admin'
            
            # Consulta en tabla 2: entrenadores
            cursor.execute(
                "SELECT 'entrenador' as tipo FROM entrenadores WHERE usuario = ? AND contrasena = ?",
                [loginVO.usuario, loginVO.password]
            )
            resultado = cursor.fetchone()
            if resultado:
                return resultado[0]  # Retorna 'entrenador'
            
            # Consulta en tabla 3: clientes
            cursor.execute(
                """SELECT 
                    CASE 
                        WHEN m.tipo = 'Premium' THEN 'premium' 
                        WHEN m.tipo = 'Sencillo' THEN 'sencillo' 
                        ELSE 'socio' 
                    END as tipo
                FROM socios so
                LEFT JOIN membresias m ON so.id_socio = m.id_socio
                WHERE so.usuario = ? AND so.contrasena = ?""",
                [loginVO.usuario, loginVO.password]
            )
            resultado = cursor.fetchone()
            
            return resultado[0] if resultado else None
            
        except Exception as e:
            print(f"Error en consultaLogin: {e}")
            return None
