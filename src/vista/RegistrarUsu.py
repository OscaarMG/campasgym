from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt6 import uic

# Cargar la interfaz generada desde el archivo .ui
Form, Window = uic.loadUiType("./src/vista/ui/RegistroUsu.ui")

class RegistrarUsu(QMainWindow, Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Inicializa los widgets
        self.setFixedSize(self.size())
        self.pushButtonCrear.clicked.connect(self.registrar_usuario)  # Conecta el botón
        self.pushButtonCancelar.clicked.connect(self.volver_panel_principal)
        self.pushButtonCancelar.clicked.connect(self.volver_panel_principal)

    def registrar_usuario(self):
        nombre = self.lineNombre.text()
        apellidos = self.lineApellidos.text()
        email = self.lineEmail.text()
        dni = self.lineDNI.text()
        usuario = self.lineUsuario.text()
        contrasena = self.lineContrasena.text()
        tipo = self.comboBoxTipoUsu.currentText()

        exito, mensaje = self.controlador.registrar_usuario(
            nombre, apellidos, dni, usuario, contrasena, email, tipo
        )

        if exito:
            QMessageBox.information(self, "Éxito", mensaje)
            self.controlador.volver_panel_principal()
            self.close()
        else:
            QMessageBox.warning(self, "Error", mensaje)

    def volver_panel_principal(self):
        if hasattr(self, "controlador"):
            self.controlador.volver_panel_principal()
        self.close()
