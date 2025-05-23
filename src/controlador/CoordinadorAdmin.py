from src.vista.RegistrarUsu import RegistrarUsu
from src.modelo.vo.UserVO import UserVO

class CoordinadorAdmin:
    def __init__(self, ventana, modelo, coordinador_principal):
        self._ventana = ventana
        self._modelo = modelo
        self._coordinador_principal = coordinador_principal
        self._ventana_principal = ventana

    def cerrarsesion(self):
        self._ventana.close()
        self._coordinador_principal.cerrarsesion()

    def volver_panel_principal(self):
        self._ventana = self._ventana_principal
        self._ventana.show()

    def abrir_registrar(self):
            self._ventana.close()
            self._ventana = RegistrarUsu()
            self._ventana.controlador = self
            self._ventana.show()


    def registrar_usuario(self, nombre, apellidos, dni, usuario, contrasena, email, tipo):
        user_vo = UserVO(nombre, apellidos, dni, usuario, contrasena, email, tipo)
        return self._modelo.registrar_usuario(user_vo)
