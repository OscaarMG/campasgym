from src.modelo.conexion.Conexion import Conexion
from src.modelo.vo.UserVO import UserVO

class UserDAO(Conexion):
    SQL_SELECT = 'SELECT socio_id, nombre, apellidos, DNI, usuario, contrsena, email, telefono, fecha_alta'
    SQL_CONSULTA = 'SELECT  1 FROM nombre WHERE nombre = ?'
    def consultaLogin(self, loginVO):
        cursor = self.getCursor()
        cursor.execute(self.SQL_CONSULTA, [loginVO.nombre])
        rows = cursor.fetchall()
        return rows



    def select(self) -> list[UserVO]:
        cursor = self.getCursor()
        usuarios = []

        cursor.execute(self.SQL_SELECT)
        rows = cursor.fetchall()

        for row in rows:
            socio_id, nombre, apellidos, DNI, usuario, contrsena, email, telefono, fecha_alta = row
            usuario = UserVO(socio_id, nombre, apellidos, DNI, usuario, contrsena, email, telefono, fecha_alta) #UserVO(row)
            usuarios.append(usuario)

        return usuarios
