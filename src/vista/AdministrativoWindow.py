from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6 import uic

# Cargar la interfaz generada desde el archivo .ui
Form, Window = uic.loadUiType("./src/vista/ui/PanelPrincipalAdministrativo.ui")

class AdministrativoWindow(QMainWindow, Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Inicializa los widgets
        self.setFixedSize(self.size())
        # Conectar el botón a la función
        self.pushButtonCerrar.clicked.connect(self.cerrar_button_click)
        self.pushButtonRegistrar.clicked.connect(self.abrir_registrar)
        self.pushButtonGUsu.clicked.connect(self.abrir_gestionar_socio)
        self.pushButtonGMon.clicked.connect(self.abrir_gestionar_monitor)
        self.pushButtonGInv.clicked.connect(self.abrir_gestionar_inventario)


    def cerrar_button_click(self):
        print("Cerrando sesión")
        self._controlador.cerrarsesion()

    def abrir_registrar(self):
        print("Abriendo ventana de registro de usuario")
        self._controlador.abrir_registrar()

    def abrir_gestionar_socio(self):
        print("Abriendo ventana de gestionar socio")
        self._controlador.abrir_gestionar_socio()

    def abrir_gestionar_monitor(self):
        print("Abriendo ventana de gestionar entrenadores")
        self._controlador.abrir_gestionar_entrenador()

    def abrir_gestionar_inventario(self):
        print("Abriendo ventana de gestionar inventario")
        self._controlador.abrir_gestionar_material()

    @property
    def controlador(self):
        return self._controlador
    
    @controlador.setter
    def controlador(self, value):
        self._controlador = value