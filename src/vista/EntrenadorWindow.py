from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6 import uic

# Cargar la interfaz generada desde el archivo .ui
Form, Window = uic.loadUiType("./src/vista/ui/PanelPrincipalEntrenador.ui")

class EntrenadorWindow(QMainWindow, Form):
    def __init__(self, id_entrenador):
        super().__init__()
        self.setupUi(self)  # Inicializa los widgets
        # Conectar el botón a la función
        self.id_entrenador = id_entrenador
        self.pushButtonCerrar.clicked.connect(self.cerrar_button_click)
        self.pushButtonClase.clicked.connect(self.abrir_crear_clase)
        self.pushButtonRutina.clicked.connect(self.abrir_crear_rutina)
        self.pushButtonDieta.clicked.connect(self.abrir_crear_dieta)

    def cerrar_button_click(self):
        print("Cerrando sesión")
        self._controlador.cerrarsesion()

    def abrir_crear_clase(self):
        print("Abriendo ventana de crear clase")
        self._controlador.abrir_crear_clase(self.id_entrenador)

    def abrir_crear_rutina(self):
        print("Abriendo ventana de crear rutina")
        self._controlador.abrir_crear_rutina()

    def abrir_crear_rutina(self):
        print("Abriendo ventana de crear rutina")
        self._controlador.abrir_crear_rutina()

    def abrir_crear_dieta(self):
        print("Abriendo ventana de crear dieta")
        self._controlador.abrir_crear_dieta()

    @property
    def controlador(self):
        return self._controlador
    
    @controlador.setter
    def controlador(self, value):
        self._controlador = value