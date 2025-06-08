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

        if not nombre or not apellidos or not email or not dni or not usuario or not contrasena:
            QMessageBox.warning(self, "Error", "Todos los campos son obligatorios.")
        else:
            if self.controlador.registrar_usuario(nombre, apellidos, dni, usuario, contrasena, email, tipo):
                QMessageBox.information(self, "Éxito", "Usuario registrado correctamente.")
            else:
                QMessageBox.warning(self, "Error", "No se pudo registrar el usuario.")

            self.controlador.volver_panel_principal()
            self.close()

    def volver_panel_principal(self):
        if hasattr(self, "controlador"):
            self.controlador.volver_panel_principal()
        self.close()
