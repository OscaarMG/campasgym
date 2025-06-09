from src.modelo.dao.UserDAO import UserDAO
from src.modelo.vo.LoginVO import LoginVO

class BussinessObject():

    def comprobarLogin(self, usuario, contrasena):
        if not usuario or not contrasena:
            return None, "Usuario y contraseña obligatorios"

        loginVO = LoginVO(usuario, contrasena)
        user = UserDAO().consultaLogin(loginVO)

        if not user:
            return None, "Credenciales incorrectas"

        return user, "Inicio de sesión exitoso"

    def verificarCorreo(self, usuario):
        if not usuario:
            return None, "Debe ingresar el usuario"
        correo = UserDAO().verificarCorreo(usuario)
        if correo:
            return correo, "Correo verificado"
        return None, "El correo no está registrado"

    def actualizarContrasena(self, usuario, nueva_contrasena):
        if not nueva_contrasena or len(nueva_contrasena) < 6:
            return False, "La contraseña debe tener al menos 6 caracteres"
        loginVO = LoginVO(usuario, nueva_contrasena)
        exito = UserDAO().actualizarContrasena(loginVO)
        if exito:
            return True, "Contraseña actualizada correctamente"
        return False, "No se pudo actualizar la contraseña"

    