from PyQt6.QtWidgets import QMainWindow, QMessageBox
from PyQt6 import uic
import random

Form, Window = uic.loadUiType("./src/vista/ui/RecuContra2.ui")

class RecuContra2(QMainWindow, Form):
    def __init__(self, correo, controlador, usuario):
        super().__init__()
        self.setupUi(self)
        self.correo = correo
        self.controlador = controlador
        self.usuario = usuario
        self.codigo = str(random.randint(100000, 999999))
        self.mostrar_mensaje()
        self.BotonAceptar.clicked.connect(self.validar_codigo)
        self.BotonCancelar.clicked.connect(self.cerrar_ventana)

    def mostrar_mensaje(self):
            QMessageBox.information(self, "Reestablecer contraseña", f"Hemos mandado un código de verificación al correo {self.correo}.\n")
            print(f"El código es: {self.codigo}")


    def validar_codigo(self):
        codigo_introducido = self.CodigoEdit.text()
        nueva_contra = self.NuevaContrasenaEdit.text()
        if codigo_introducido == self.codigo:
            self.controlador.actualizarContrasena(self.usuario, nueva_contra)
            QMessageBox.information(self, "Éxito", "Contraseña actualizada correctamente.")
            self.controlador.ventana_login.resetear()
            self.controlador.ventana_login.show()
            self.close()
        else:
            QMessageBox.warning(self, "Error", "El código introducido es incorrecto.")
            self.CodigoEdit.clear()

    def cerrar_ventana(self):
        self.controlador.ventana_login.show()
        self.close()