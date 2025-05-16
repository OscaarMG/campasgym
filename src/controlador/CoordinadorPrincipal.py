from src.modelo.vo.LoginVO import LoginVO
from src.vista.SocioWindow import SocioWindow
from src.vista.EntrenadorWindow import EntrenadorWindow
from src.vista.AdministrativoWindow import AdministrativoWindow

class CoordinadorPrincipal():

    def __init__(self, ventanaLogin, modelo):
        self._ventanaLogin = ventanaLogin
        self._modelo = modelo
        self._ventanaActual = None

    def iniciarlogin(self, usuario, contrasena):
        #Comprobaciones
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
        else:  # socio
            self._ventanaActual = SocioWindow()
            
        self._ventanaActual.show()