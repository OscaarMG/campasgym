from PyQt6.QtWidgets import QWidget, QMessageBox, QListWidgetItem
from PyQt6 import uic
from src.modelo.vo.ClaseVO import ClaseVO

class CrearClase(QWidget):
    def __init__(self, id_entrenador):
        super().__init__()
        uic.loadUi("./src/vista/ui/crear_clase_grupal.ui", self)

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

        # Validación
        if not nombre or not horario or not lugar:
            QMessageBox.warning(self, "Error", "Todos los campos obligatorios deben estar llenos")
            return

        if self.id_entrenador is None:
            QMessageBox.warning(self, "Error", "Entrenador no válido")
            return
        clase = ClaseVO(
            nombre=nombre,
            descripcion=descripcion,
            horario=horario,
            lugar=lugar,
            cupo_maximo=cupo,
            id_entrenador=self.id_entrenador
        )


        if self.controlador.registrar_clase(clase):
            QMessageBox.information(self, "Éxito", "Clase registrada correctamente")
            self.controlador.volver_panel_principal()
            self.close()
        else:
            QMessageBox.warning(self, "Error", "Error al registrar la clase")

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
        if self.controlador.eliminar_clase(id_clase):
            QMessageBox.information(self, "Éxito", "Clase cancelada correctamente.")
            self.cargar_clases()
        else:
            QMessageBox.warning(self, "Error", "Error al cancelar la clase.")


    def cancelar(self):
        self.controlador.volver_panel_principal()
        self.close()

