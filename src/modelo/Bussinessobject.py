from src.modelo.dao.UserDAO import UserDAO


class BussinessObject():

    def comprobarLogin(self, loginVO):
        user_dao = UserDAO()
        return user_dao.consultaLogin(loginVO)
    
    def verificarCorreo(self, usuario):
        user_dao = UserDAO()
        return user_dao.verificarCorreo(usuario)
    
    def actualizarContrasena(self, loginVO):
        user_dao = UserDAO()
        return user_dao.actualizarContrasena(loginVO)
    