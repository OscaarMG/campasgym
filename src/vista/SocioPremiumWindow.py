from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6 import uic

# Cargar la interfaz generada desde el archivo .ui
Form, Window = uic.loadUiType("./src/vista/ui/PanelPrincipalSocioPre.ui")

class SocioPremiumWindow(QMainWindow, Form):
    def __init__(self, id_socio):
        super().__init__()
        self.setupUi(self)  # Inicializa los widgets
        self.id_socio = id_socio
        # Conectar el botón a la función
        self.pushButtonCerrar.clicked.connect(self.cerrar_button_click)
        self.pushButtonClase.clicked.connect(self.abrir_apuntarse_clase)
        self.pushButtonRutina.clicked.connect(self.abrir_rutina)
        self.pushButtonDieta.clicked.connect(self.abrir_dieta)

    def cerrar_button_click(self):
        print("Cerrando sesión")
        self._controlador.cerrarsesion()

    @property
    def controlador(self):
        return self._controlador
    
    @controlador.setter
    def controlador(self, value):
        self._controlador = value

    def abrir_apuntarse_clase(self):
        print("Abriendo ventana de clases grupales")
        self._controlador.abrir_apuntarse_clase(self.id_socio)

    def abrir_rutina(self):
        print("Abriendo ventana de rutinas")
        self._controlador.abrir_rutina(self.id_socio)

    def abrir_dieta(self):
        print("Abriendo ventana de dietas")
        self._controlador.abrir_dieta(self.id_socio)