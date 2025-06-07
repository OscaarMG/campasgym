from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6 import uic
from src.vista.Login import Login
from src.modelo.Bussinessobject import BussinessObject
from src.controlador.CoordinadorPrincipal import CoordinadorPrincipal
import recursos_rc

if __name__ == "__main__":
    app = QApplication([])

    ventanaLogin = Login()
    modelo = BussinessObject()
    coordinador = CoordinadorPrincipal(ventanaLogin, modelo)
    ventanaLogin.controlador = coordinador
    ventanaLogin.show()

    app.exec()

