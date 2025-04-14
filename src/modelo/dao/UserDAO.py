from src.modelo.conexion.Conexion import Conexion
from src.modelo.vo.UserVO import UserVO

class UserDAO(Conexion):
    SQL_SELECT = 'SELECT actor_id, first_name, last_name, last_update'
    SQL_CONSULTA = 'SELECT  1 FROM first_name WHERE nombre = ?'
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
            actor_id, first_name, last_name, last_update = row
            usuario = UserVO(actor_id, first_name, last_name, last_update) #UserVO(row)
            usuarios.append(usuario)

        return usuarios
