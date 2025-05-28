from PyQt6.QtWidgets import QMainWindow, QMessageBox
from PyQt6 import uic

Form, Window = uic.loadUiType("./src/vista/ui/PanelPrincipalSocio.ui")

class SocioWindow(QMainWindow, Form):
    def __init__(self, id_socio):
        super().__init__()
        self.setupUi(self)
        self.id_socio = id_socio
        self.pushButtonCerrar.clicked.connect(self.cerrar_button_click)
        self.pushButtonCancelar.clicked.connect(self.confirmar_baja)  # Botón de baja

    def cerrar_button_click(self):
        print("Cerrando sesión")
        QMessageBox.information(self, "Cerrar sesión", "Sesión cerrada correctamente.")
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

    @property
    def controlador(self):
        return self._controlador
    
    @controlador.setter
    def controlador(self, value):
        self._controlador = value


