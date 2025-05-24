from src.modelo.dao.AdminDAO import AdminDAO

class BussinessobjectAdmin:

    def registrar_usuario(self, UserVO):
        admin_dao = AdminDAO()
        return admin_dao.insertar_usuario(UserVO)
    
    def obtener_socios(self):
        admin_dao = AdminDAO()
        return admin_dao.obtener_socios()

    def eliminar_socio(self, id_socio):
        admin_dao = AdminDAO()
        return admin_dao.eliminar_socio(id_socio)

    def modificar_socio(self, userVO):
        admin_dao = AdminDAO()
        return admin_dao.modificar_socio(userVO)
    
    def obtener_entrenadores(self):
        admin_dao = AdminDAO()
        return admin_dao.obtener_entrenadores()

    def registrar_entrenador(self, entrenadorVO):
        admin_dao = AdminDAO()
        return admin_dao.insertar_entrenador(entrenadorVO)

    def eliminar_entrenador(self, id_entrenador):
        admin_dao = AdminDAO()
        return admin_dao.eliminar_entrenador(id_entrenador)

    def modificar_entrenador(self, entrenadorVO):
        admin_dao = AdminDAO()
        return admin_dao.modificar_entrenador(entrenadorVO)
    
    def obtener_materiales(self):
        return AdminDAO().obtener_materiales()

    def registrar_material(self, materialVO):
        return AdminDAO().insertar_material(materialVO)

    def modificar_material(self, materialVO):
        return AdminDAO().modificar_material(materialVO)

    def eliminar_material(self, id_material):
        return AdminDAO().eliminar_material(id_material)
    
    def obtener_adms(self):
        return AdminDAO().obtener_adms()

    def registrar_adm(self, admVO):
        return AdminDAO().insertar_adm(admVO)

    def modificar_adm(self, admVO):
        return AdminDAO().modificar_adm(admVO)

    def eliminar_adm(self, id_adm):
        return AdminDAO().eliminar_adm(id_adm)
