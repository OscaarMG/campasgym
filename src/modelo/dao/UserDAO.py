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
                return resultado[0]  # Retorna 'administrativo'
            
            cursor.execute(
                "SELECT 'administrador' as tipo FROM administrador WHERE usuario = ? AND contrasena = ?",
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
        
    def verificarCorreo(self, usuario):
        try:
            cursor = self.getCursor()
            cursor.execute(
                "SELECT email FROM Socios WHERE usuario = ?",
                [usuario]
            )
            email = cursor.fetchone()
            return email[0] if email else None
        
        except Exception as e:
            print(f"Error en verificarCorreo: {e}")
            return None
        
    def actualizarContrasena(self, loginVO):
        try:
            cursor = self.getCursor()
            cursor.execute(
                "UPDATE Socios SET contrasena = ? WHERE usuario = ?",
                [loginVO.password, loginVO.usuario]
            )
            return True
        except Exception as e:
            print(f"Error en actualizarContrasena: {e}")
            return False

