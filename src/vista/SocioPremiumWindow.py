from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt6 import uic

# Cargar la interfaz generada desde el archivo .ui
Form, Window = uic.loadUiType("./src/vista/ui/PanelPrincipalSocioPre.ui")

class SocioPremiumWindow(QMainWindow, Form):
    def __init__(self, id_socio):
        super().__init__()
        self.setupUi(self)  # Inicializa los widgets
        self.setFixedSize(self.size())
        self.id_socio = id_socio
        # Conectar el botón a la función
        self.pushButtonCerrar.clicked.connect(self.cerrar_button_click)
        self.pushButtonClase.clicked.connect(self.abrir_apuntarse_clase)
        self.pushButtonRutina.clicked.connect(self.abrir_rutina)
        self.pushButtonDieta.clicked.connect(self.abrir_dieta)
        self.pushButtonCancelar.clicked.connect(self.confirmar_baja)
        self.pushButtonRenovar.clicked.connect(self.abrir_renovar_suscripcion)  

    def confirmar_baja(self):
        respuesta = QMessageBox.question(
            self,
            "Confirmar baja",
            "¿Está seguro que desea darse de baja?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )

        if respuesta == QMessageBox.StandardButton.Yes:
            if self._controlador:
                self._controlador.dar_de_baja_socio(self.id_socio)
                QMessageBox.information(self, "Cuenta eliminada", "Su cuenta ha sido eliminada.")
                self._controlador.cerrarsesion()
    
    def abrir_renovar_suscripcion(self):
        self._controlador.abrir_renovar_suscripcion(self.id_socio)

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