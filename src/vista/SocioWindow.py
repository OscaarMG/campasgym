from PyQt6.QtWidgets import QMainWindow
from PyQt6 import uic

Form, Window = uic.loadUiType("./src/vista/ui/PanelPrincipalSocio.ui")

class SocioWindow(QMainWindow, Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self._coordinador = None
        self.pushButtonCerrar.clicked.connect(self.cerrar_button_click)

    def cerrar_button_click(self):
        print("Cerrando sesión")
        if self._coordinador:
            self._coordinador.cerrarsesion()

    @property
    def coordinador(self):
        return self._coordinador
    
    @coordinador.setter
    def coordinador(self, value):
        self._coordinador = value


