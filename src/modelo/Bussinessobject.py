from src.modelo.dao.UserDAO import UserDAO

class BussinessObject():
    def pruebaselect(self):
        userdao = UserDAO()
        usuarios = userdao.select()

        for usuario in usuarios:
            print(usuario._nombre)

    def comprobarLogin(self, loginVO):
        user_dao = UserDAO()
        return user_dao.consultaLogin(loginVO)