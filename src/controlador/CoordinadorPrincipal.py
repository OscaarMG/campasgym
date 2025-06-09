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
from src.vista.RecuContra2 import RecuContra2
from src.vista.RecuContra1 import RecuContra1

class CoordinadorPrincipal():

    def __init__(self, ventanaLogin, modelo):
        self._ventanaLogin = ventanaLogin
        self._modelo = modelo
        self._ventanaActual = None

    @property
    def ventana_login(self):
        return self._ventanaLogin
        
    def iniciarlogin(self, usuario, contrasena):

        usuario, mensaje = self._modelo.comprobarLogin(usuario, contrasena)
        if not usuario:
            print(mensaje)
            return

        self._ventanaLogin.close()

        if usuario[0] == 'administrativo':
            modelo_admin = BussinessobjectAdmin()
            self._ventanaActual = AdministrativoWindow()
            coordinador_admin = CoordinadorAdmin(self._ventanaActual, modelo_admin, self)
            self._ventanaActual.controlador = coordinador_admin
            self._ventanaActual.modelo = modelo_admin
        elif usuario[0] == 'entrenador':
            modelo_entrenador = BussinessobjectEntrenador()
            self._ventanaActual = EntrenadorWindow(usuario[1])
            coordinador_entrenador = CoordinadorEntrenador(self._ventanaActual, modelo_entrenador, self)
            self._ventanaActual.controlador = coordinador_entrenador
            self._ventanaActual.modelo = modelo_entrenador
        elif usuario[0] == 'administrador':
            modelo_admin = BussinessobjectAdmin()
            self._ventanaActual = AdministradorWindow()
            coordinador_admin = CoordinadorAdmin(self._ventanaActual, modelo_admin, self)
            self._ventanaActual.controlador = coordinador_admin
            self._ventanaActual.modelo = modelo_admin
        elif usuario[0] == 'premium':
            modelo_socio = BussinessobjectSocio()
            self._ventanaActual = SocioPremiumWindow(usuario[1])
            coordinador_socio = CoordinadorSocio(self._ventanaActual, modelo_socio, self)
            self._ventanaActual.controlador = coordinador_socio
            self._ventanaActual.modelo = modelo_socio
        else:
            modelo_socio = BussinessobjectSocio()
            self._ventanaActual = SocioWindow(usuario[1])
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
        return self._modelo.actualizarContrasena(usuario, contrasena)

    def verificarCorreo(self, usuario):
        return self._modelo.verificarCorreo(usuario)
    
    def abrir_recucontra1(self):
        self._ventanaLogin.close()
        self._ventanaActual = RecuContra1()
        self._ventanaActual.controlador = self
        self._ventanaActual.show()
    
    def abrir_recucontra2(self, correo, usuario):
        self._ventanaLogin.close()
        self._ventanaActual = RecuContra2(correo, usuario)
        self._ventanaActual.controlador = self
        self._ventanaActual.show()