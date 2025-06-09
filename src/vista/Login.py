from PyQt6.QtWidgets import QMainWindow
from PyQt6 import uic

from src.vista.RecuContra1 import RecuContra1

Form, Window = uic.loadUiType("./src/vista/ui/VistaLogin.ui")

class Login(QMainWindow, Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(self.size())
        self.BotonAceptar.clicked.connect(self.on_button_click)
        self.BotonRecuContra.clicked.connect(self.recuperar_contrasena)

    def on_button_click(self):
        usuario = self.UsuarioEdit.text()
        contrasena = self.ContrasenaEdit.text()
        self._controlador.iniciarlogin(usuario, contrasena)

    def resetear(self):
        self.UsuarioEdit.clear()
        self.ContrasenaEdit.clear()

    def recuperar_contrasena(self):
        self._controlador.abrir_recucontra1()

    @property
    def controlador(self):
        return self._controlador

    @controlador.setter
    def controlador(self, value):
        self._controlador = value


