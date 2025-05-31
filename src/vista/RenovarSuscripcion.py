from PyQt6.QtWidgets import QMainWindow, QMessageBox
from PyQt6 import uic

Form, _ = uic.loadUiType("src/vista/ui/RenovarSuscripcion.ui")

class RenovarSuscripcion(QMainWindow, Form):
    def __init__(self, controlador, id_socio):
        super().__init__()
        self.setupUi(self)
        self.controlador = controlador
        self.id_socio = id_socio

        self.pushButtonAceptar.clicked.connect(self.renovar)
        self.pushButtonCancelar.clicked.connect(self.close)

    def renovar(self):
        tipo = self.comboBoxTipo.currentText().lower()
        cvc = self.lineEditCVC.text().strip()
        cuenta = self.lineEditCuenta.text().strip()
        fecha_cad = self.dateEditCaducidad.date().toPyDate()

        if not cvc or not cuenta or not fecha_cad:
            QMessageBox.warning(self, "Error", "Todos los campos son obligatorios.")
            return

        try:
            self.controlador.renovar_suscripcion(self.id_socio, tipo)
            QMessageBox.information(self, "Éxito", "Suscripción renovada correctamente.")
            self.close()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Fallo al renovar: {str(e)}")
