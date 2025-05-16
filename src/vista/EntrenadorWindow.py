from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6 import uic

# Cargar la interfaz generada desde el archivo .ui
Form, Window = uic.loadUiType("./src/vista/ui/PanelPrincipalUsuario.ui")

class EntrenadorWindow(QMainWindow, Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Inicializa los widgets
        # Conectar el botón a la función