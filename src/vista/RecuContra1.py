from PyQt6.QtWidgets import QMainWindow, QMessageBox
from PyQt6 import uic
from src.vista.RecuContra2 import RecuContra2

Form, Window = uic.loadUiType("./src/vista/ui/RecuContra1.ui")

class RecuContra1(QMainWindow, Form):
    def __init__(self, controlador):
        super().__init__()
        self.setupUi(self)
        self.controlador = controlador
        self.BotonAceptar.clicked.connect(self.abrir_recucontra2)

    def abrir_recucontra2(self):
        usuario = self.UsuarioEdit.text()
        correo = self.controlador.verificarCorreo(usuario)
        if correo:
            self.ventana2 = RecuContra2(correo, self.controlador, usuario)
            self.ventana2.show()
            self.close()
        else:
            QMessageBox.warning(self, "Error", "El correo no está registrado.")
            self.controlador.ventana_login.show()
            self.close()