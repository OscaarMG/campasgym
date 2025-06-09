from src.modelo.dao.AdminDAO import AdminDAO
from src.modelo.vo.UserVO import UserVO
from src.modelo.vo.MaterialVO import MaterialVO
from src.modelo.vo.EntrenadorVO import EntrenadorVO
from src.modelo.vo.AdmVO import AdmVO

class BussinessobjectAdmin:

    def registrar_usuario(self, nombre, apellidos, dni, usuario, contrasena, email, tipo):
        if not all([nombre, apellidos, dni, usuario, contrasena, email]):
            return False, "Todos los campos son obligatorios."

        user_vo = UserVO(nombre, apellidos, dni, usuario, contrasena, email, tipo)
        exito = AdminDAO().insertar_usuario(user_vo)
        if exito:
            return True, "Usuario registrado correctamente."
        else:
            return False, "No se pudo registrar el usuario."

    
    def obtener_socios(self):
        admin_dao = AdminDAO()
        return admin_dao.obtener_socios()

    def eliminar_socio(self, id_socio):
        admin_dao = AdminDAO()
        return admin_dao.eliminar_socio(id_socio)

    def modificar_socio(self, datos_usuario):
        # Validación
        campos_obligatorios = ['id', 'nombre', 'apellidos', 'dni', 'usuario', 'email', 'tipo']
        for campo in campos_obligatorios:
            if not datos_usuario.get(campo):
                return False, f"El campo '{campo}' es obligatorio."

        user_vo = UserVO(
            datos_usuario["nombre"],
            datos_usuario["apellidos"],
            datos_usuario["dni"],
            datos_usuario["usuario"],
            "",  # Contraseña no se modifica
            datos_usuario["email"],
            datos_usuario["tipo"]
        )
        user_vo._id = datos_usuario["id"]

        exito = AdminDAO().modificar_socio(user_vo)
        if exito:
            return True, "Socio modificado correctamente."
        else:
            return False, "No se pudo modificar el socio."

    
    def obtener_entrenadores(self):
        admin_dao = AdminDAO()
        return admin_dao.obtener_entrenadores()

    def registrar_entrenador(self, datos):
        campos_obligatorios = ['nombre', 'apellido1', 'usuario', 'contrasena']
        for campo in campos_obligatorios:
            if not datos.get(campo):
                return False, f"El campo '{campo}' es obligatorio."

        entrenador_vo = EntrenadorVO(
            id_entrenador=None,
            nombre=datos["nombre"],
            apellido1=datos.get("apellido1", ""),
            apellido2=datos.get("apellido2", ""),
            usuario=datos["usuario"],
            contrasena=datos["contrasena"],
            especialidad=datos.get("especialidad", ""),
            email=datos.get("email", ""),
            telefono=datos.get("telefono", ""),
            n_cuenta=datos.get("n_cuenta", ""),
            horario=datos.get("horario", ""),
        )

        exito = AdminDAO().insertar_entrenador(entrenador_vo)
        if exito:
            return True, "Entrenador registrado correctamente."
        else:
            return False, "No se pudo registrar el entrenador."

    def modificar_entrenador(self, datos):
        if not datos.get("id_entrenador"):
            return False, "ID de entrenador no válido"

        campos_obligatorios = ['nombre', 'apellido1', 'usuario']
        for campo in campos_obligatorios:
            if not datos.get(campo):
                return False, f"El campo '{campo}' es obligatorio."

        entrenador_vo = EntrenadorVO(
            id_entrenador=datos["id_entrenador"],
            nombre=datos["nombre"],
            apellido1=datos.get("apellido1", ""),
            apellido2=datos.get("apellido2", ""),
            usuario=datos["usuario"],
            contrasena="",  # No se modifica
            especialidad=datos.get("especialidad", ""),
            email=datos.get("email", ""),
            telefono=datos.get("telefono", ""),
            n_cuenta=datos.get("n_cuenta", ""),
            horario=datos.get("horario", ""),
            fecha_ingreso=datos.get("fecha_ingreso")
        )

        exito = AdminDAO().modificar_entrenador(entrenador_vo)
        if exito:
            return True, "Entrenador modificado correctamente."
        else:
            return False, "No se pudo modificar el entrenador."

    def eliminar_entrenador(self, id_entrenador):
        admin_dao = AdminDAO()
        return admin_dao.eliminar_entrenador(id_entrenador)
    
    def obtener_materiales(self):
        return AdminDAO().obtener_materiales()

    def registrar_material(self, datos_material):
        if not datos_material["nombre"]:
            return False, "El nombre es obligatorio."

        materialVO = MaterialVO(
            id_material=None,
            nombre=datos_material["nombre"],
            cantidad=datos_material["cantidad"],
            estado=datos_material["estado"],
            ubicacion=datos_material["ubicacion"],
            fecha_ingreso=None  # Se puede poner la fecha actual si se requiere
        )

        if AdminDAO().insertar_material(materialVO):
            return True, "Material registrado correctamente."
        else:
            return False, "No se pudo registrar el material."

    def modificar_material(self, datos_material):
        if not datos_material["nombre"]:
            return False, "El nombre es obligatorio."

        materialVO = MaterialVO(
            id_material=datos_material["id_material"],
            nombre=datos_material["nombre"],
            cantidad=datos_material["cantidad"],
            estado=datos_material["estado"],
            ubicacion=datos_material["ubicacion"],
            fecha_ingreso=datos_material["fecha_ingreso"]
        )

        if AdminDAO().modificar_material(materialVO):
            return True, "Material modificado correctamente."
        else:
            return False, "No se pudo modificar el material."

    def eliminar_material(self, id_material):
        return AdminDAO().eliminar_material(id_material)
    
    def obtener_adms(self):
        admin_dao = AdminDAO()
        return admin_dao.obtener_adms()

    def registrar_adm(self, datos):
        campos_obligatorios = ['nombre', 'apellido1', 'usuario', 'contrasena']
        for campo in campos_obligatorios:
            if not datos.get(campo):
                return False, f"El campo '{campo}' es obligatorio."

        adm_vo = AdmVO(
            id_adm=None,
            nombre=datos["nombre"],
            apellido1=datos.get("apellido1", ""),
            apellido2=datos.get("apellido2", ""),
            usuario=datos["usuario"],
            contrasena=datos["contrasena"],
            puesto=datos.get("puesto", ""),
            email=datos.get("email", ""),
            telefono=datos.get("telefono", ""),
            n_cuenta=datos.get("n_cuenta", ""),
            horario=datos.get("horario", ""),
        )

        exito = AdminDAO().insertar_adm(adm_vo)
        if exito:
            return True, "Administrativo registrado correctamente."
        else:
            return False, "No se pudo registrar el administrativo."


    def modificar_adm(self, datos):
        if not datos.get("id_adm"):
            return False, "ID de administrativo no válido."

        campos_obligatorios = ['nombre', 'apellido1', 'usuario']
        for campo in campos_obligatorios:
            if not datos.get(campo):
                return False, f"El campo '{campo}' es obligatorio."

        adm_vo = AdmVO(
            id_adm=datos["id_adm"],
            nombre=datos["nombre"],
            apellido1=datos.get("apellido1", ""),
            apellido2=datos.get("apellido2", ""),
            usuario=datos["usuario"],
            contrasena="",  # no se actualiza en modificación
            puesto=datos.get("puesto", ""),
            email=datos.get("email", ""),
            telefono=datos.get("telefono", ""),
            n_cuenta=datos.get("n_cuenta", ""),
            horario=datos.get("horario", ""),
            fecha_ingreso=datos.get("fecha_ingreso")
        )

        exito = AdminDAO().modificar_adm(adm_vo)
        if exito:
            return True, "Administrativo modificado correctamente."
        else:
            return False, "No se pudo modificar el administrativo."


    def eliminar_adm(self, id_adm):
        admin_dao = AdminDAO()
        return admin_dao.eliminar_adm(id_adm)
