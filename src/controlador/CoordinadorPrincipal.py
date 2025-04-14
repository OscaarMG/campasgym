from src.modelo.vo.LoginVO import LoginVO

class CoordinadorPrincipal():

    def __init__(self, ventanaLogin, modelo):
        self._ventana = ventanaLogin
        self._modelo = modelo

    def iniciarlogin(self, nombre):
        #Comprobaciones
        loginVO = LoginVO(nombre)
        resultado = self._modelo.comprobarLogin(loginVO)
        