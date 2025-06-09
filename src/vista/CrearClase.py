from PyQt6.QtWidgets import QWidget, QMessageBox, QListWidgetItem
from PyQt6 import uic

class CrearClase(QWidget):
    def __init__(self, id_entrenador):
        super().__init__()
        uic.loadUi("./src/vista/ui/crear_clase_grupal.ui", self)
        self.setFixedSize(self.size())
        self.btnGuardar.clicked.connect(self.guardar_clase)
        self.btnCancelarClase.clicked.connect(self.cancelar_clase_seleccionada)
        self.btnCancelar.clicked.connect(self.cancelar)
        self.id_entrenador = id_entrenador

    @property
    def controlador(self):
        return self._controlador

    @controlador.setter
    def controlador(self, value):
        self._controlador = value
        self.cargar_clases()

    def guardar_clase(self):
        nombre = self.comboBoxTipoClase.currentText().strip()
        descripcion = self.textEdit.toPlainText().strip()
        horario = self.lineEditHorario.text().strip()
        lugar = self.comboBoxSala.currentText().strip()
        cupo = self.spinBoxCupoMaximo.value()

        exito, mensaje = self.controlador.registrar_clase(
            nombre, descripcion, horario, lugar, cupo, self.id_entrenador
        )

        if exito:
            QMessageBox.information(self, "Éxito", mensaje)
            self.controlador.volver_panel_principal()
            self.close()
        else:
            QMessageBox.warning(self, "Error", mensaje)

    def cargar_clases(self):
        self.listWidgetClases.clear()
        clases = self.controlador.obtener_clases_por_entrenador(self.id_entrenador)
        for clase in clases:
            item = QListWidgetItem(f"{clase['id']} - {clase['nombre']} ({clase['horario']})")
            item.setData(256, clase['id'])  # Qt.UserRole
            self.listWidgetClases.addItem(item)

    def cancelar_clase_seleccionada(self):
        item = self.listWidgetClases.currentItem()
        if not item:
            QMessageBox.warning(self, "Error", "Selecciona una clase para cancelar.")
            return
        id_clase = item.data(256)
        exito, mensaje = self.controlador.eliminar_clase(id_clase)
        if exito:
            QMessageBox.information(self, "Éxito", mensaje)
            self.cargar_clases()
        else:
            QMessageBox.warning(self, "Error", mensaje)

    def cancelar(self):
        self.controlador.volver_panel_principal()
        self.close()


