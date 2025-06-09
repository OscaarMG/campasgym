from PyQt6.QtWidgets import QMainWindow, QMessageBox
from PyQt6 import uic
import random

Form, Window = uic.loadUiType("./src/vista/ui/RecuContra2.ui")

class RecuContra2(QMainWindow, Form):
    def __init__(self, correo, usuario):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(self.size())
        self.correo = correo
        self.usuario = usuario
        self.codigo = str(random.randint(100000, 999999))
        self.mostrar_mensaje()
        self.BotonAceptar.clicked.connect(self.validar_codigo)
        self.BotonCancelar.clicked.connect(self.cerrar_ventana)

    def mostrar_mensaje(self):
        QMessageBox.information(self, "Reestablecer contraseña",
                                f"Hemos mandado un código de verificación al correo {self.correo}.")
        print(f"El código es: {self.codigo}")

    def validar_codigo(self):
        codigo_ingresado = self.CodigoEdit.text()
        nueva_contra = self.NuevaContrasenaEdit.text()

        if codigo_ingresado == self.codigo:
            exito, mensaje = self.controlador.actualizarContrasena(self.usuario, nueva_contra)
            if exito:
                QMessageBox.information(self, "Éxito", mensaje)
                self.controlador.ventana_login.resetear()
                self.controlador.ventana_login.show()
                self.close()
            else:
                QMessageBox.warning(self, "Error", mensaje)
        else:
            QMessageBox.warning(self, "Error", "El código introducido es incorrecto.")
            self.CodigoEdit.clear()

    def cerrar_ventana(self):
        self.controlador.ventana_login.show()
        self.close()

    @property
    def controlador(self):
        return self._controlador

    @controlador.setter
    def controlador(self, value):
        self._controlador = value
