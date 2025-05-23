from src.modelo.vo.LoginVO import LoginVO
from src.vista.SocioWindow import SocioWindow
from src.vista.EntrenadorWindow import EntrenadorWindow
from src.vista.AdministrativoWindow import AdministrativoWindow
from src.vista.SocioPremiumWindow import SocioPremiumWindow
from src.vista.AdministradorWindow import AdministradorWindow
from src.modelo.BussinessobjectSocio import BussinessobjectSocio
from src.controlador.CoordinadorAdmin import CoordinadorAdmin
from src.modelo.BussinessobjectAdmin import BussinessobjectAdmin
from src.controlador.CoordinadorEntrenador import CoordinadorEntrenador
from src.modelo.BussinessobjectEntrenador import BussinessobjectEntrenador
from src.controlador.CoordinadorSocio import CoordinadorSocio

class CoordinadorPrincipal():

    def __init__(self, ventanaLogin, modelo):
        self._ventanaLogin = ventanaLogin
        self._modelo = modelo
        self._ventanaActual = None

    @property
    def ventana_login(self):
        return self._ventanaLogin
        
    def iniciarlogin(self, usuario, contrasena):
        loginVO = LoginVO(usuario, contrasena)
        tipo_usuario = self._modelo.comprobarLogin(loginVO)
        if not tipo_usuario:
            print("Credenciales incorrectas")
            return

        self._ventanaLogin.close()

        if tipo_usuario == 'administrativo':
            modelo_admin = BussinessobjectAdmin()
            self._ventanaActual = AdministrativoWindow()
            coordinador_admin = CoordinadorAdmin(self._ventanaActual, modelo_admin, self)
            self._ventanaActual.controlador = coordinador_admin
            self._ventanaActual.modelo = modelo_admin
        elif tipo_usuario == 'entrenador':
            modelo_entrenador = BussinessobjectEntrenador()
            self._ventanaActual = EntrenadorWindow()
            coordinador_entrenador = CoordinadorEntrenador(self._ventanaActual, modelo_entrenador, self)
            self._ventanaActual.controlador = coordinador_entrenador
            self._ventanaActual.modelo = modelo_entrenador
        elif tipo_usuario == 'administrador':
            modelo_admin = BussinessobjectAdmin()
            self._ventanaActual = AdministradorWindow()
            coordinador_admin = CoordinadorAdmin(self._ventanaActual, modelo_admin, self)
            self._ventanaActual.controlador = coordinador_admin
            self._ventanaActual.modelo = modelo_admin
        elif tipo_usuario == 'premium':
            modelo_socio = BussinessobjectSocio()
            self._ventanaActual = SocioPremiumWindow()
            coordinador_socio = CoordinadorSocio(self._ventanaActual, modelo_socio, self)
            self._ventanaActual.controlador = coordinador_socio
            self._ventanaActual.modelo = modelo_socio
        else:
            modelo_socio = BussinessobjectSocio()
            self._ventanaActual = SocioWindow()
            coordinador_socio = CoordinadorSocio(self._ventanaActual, modelo_socio, self)
            self._ventanaActual.controlador = coordinador_socio
            self._ventanaActual.modelo = modelo_socio

        self._ventanaActual.show()

    def cerrarsesion(self):
            if self._ventanaActual:
                self._ventanaActual.close()
            self._ventanaLogin.resetear()
            self._ventanaLogin.show()
            self._ventanaActual = None
    
    def actualizarContrasena(self, usuario, contrasena):
        loginVO = LoginVO(usuario, contrasena)
        return self._modelo.actualizarContrasena(loginVO)

    def verificarCorreo(self, usuario):
        return self._modelo.verificarCorreo(usuario)

