from src.modelo.dao.AdminDAO import AdminDAO

class BussinessobjectAdmin:

    def registrar_usuario(self, UserVO):
        admin_dao = AdminDAO()
        return admin_dao.insertar_usuario(UserVO)