from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6 import uic

# Cargar la interfaz generada desde el archivo .ui
Form, Window = uic.loadUiType("./src/vista/ui/PanelPrincipalEntrenador.ui")

class EntrenadorWindow(QMainWindow, Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Inicializa los widgets
        # Conectar el botón a la función
        self.pushButtonCerrar.clicked.connect(self.cerrar_button_click)


    def cerrar_button_click(self):
        print("Cerrando sesión")
        self._controlador.cerrarsesion()

    @property
    def controlador(self):
        return self._controlador
    
    @controlador.setter
    def controlador(self, value):
        self._controlador = value