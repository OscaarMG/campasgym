from PyQt6.QtWidgets import QMainWindow, QMessageBox
from PyQt6 import uic

Form, Window = uic.loadUiType("./src/vista/ui/RecuContra1.ui")

class RecuContra1(QMainWindow, Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(self.size())
        self.BotonAceptar.clicked.connect(self.abrir_recucontra2)

    def abrir_recucontra2(self):
        usuario = self.UsuarioEdit.text()
        correo, mensaje = self.controlador.verificarCorreo(usuario)
        if correo:
            self.controlador.abrir_recucontra2(correo, usuario)
        else:
            QMessageBox.warning(self, "Error", mensaje)
            self.controlador.ventana_login.show()
            self.close()

    @property
    def controlador(self):
        return self._controlador

    @controlador.setter
    def controlador(self, value):
        self._controlador = value
