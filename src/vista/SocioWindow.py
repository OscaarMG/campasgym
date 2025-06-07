from PyQt6.QtWidgets import QMainWindow, QMessageBox
from PyQt6 import uic

Form, Window = uic.loadUiType("./src/vista/ui/PanelPrincipalSocio.ui")

class SocioWindow(QMainWindow, Form):
    def __init__(self, id_socio):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(self.size())
        self.id_socio = id_socio
        self.pushButtonCerrar.clicked.connect(self.cerrar_button_click)
        self.pushButtonCancelar.clicked.connect(self.confirmar_baja)
        self.pushButtonRenovar.clicked.connect(self.abrir_renovar_suscripcion)  # Botón de baja

    def cerrar_button_click(self):
        print("Cerrando sesión")
        if self._controlador:
            self._controlador.cerrarsesion()

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

    @property
    def controlador(self):
        return self._controlador
    
    @controlador.setter
    def controlador(self, value):
        self._controlador = value


