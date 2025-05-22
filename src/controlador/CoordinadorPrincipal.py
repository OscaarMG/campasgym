from src.modelo.vo.LoginVO import LoginVO
from src.vista.SocioWindow import SocioWindow
from src.vista.EntrenadorWindow import EntrenadorWindow
from src.vista.AdministrativoWindow import AdministrativoWindow
from src.vista.SocioPremiumWindow import SocioPremiumWindow

class CoordinadorPrincipal():

    def __init__(self, ventanaLogin, modelo):
        self._ventanaLogin = ventanaLogin
        self._modelo = modelo
        self._ventanaActual = None

    def iniciarlogin(self, usuario, contrasena):
        loginVO = LoginVO(usuario, contrasena)
        tipo_usuario = self._modelo.comprobarLogin(loginVO)
        if not tipo_usuario:
            print("Credenciales incorrectas")
            return

        self._ventanaLogin.close()

        if tipo_usuario == 'administrativo':
            self._ventanaActual = AdministrativoWindow()
        elif tipo_usuario == 'entrenador':
            self._ventanaActual = EntrenadorWindow()
        elif tipo_usuario == 'premium':
            self._ventanaActual = SocioPremiumWindow()
        else:
            self._ventanaActual = SocioWindow()

        # Asignar el coordinador a la nueva ventana
        self._ventanaActual.controlador = self
        self._ventanaActual.show()

    def cerrarsesion(self):
        if self._ventanaActual:
            self._ventanaActual.close()
            self._ventanaLogin.resetear()
            self._ventanaLogin.show()
            self._ventanaActual = None
