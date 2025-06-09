from PyQt6 import uic
from PyQt6.QtWidgets import QWidget, QMessageBox
from PyQt6.QtCore import Qt

class CrearDieta(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('src/vista/ui/CrearDieta.ui', self)
        self.setFixedSize(self.size())
        self.btnCrear.clicked.connect(self.crear_dieta)
        self.btnAsignar.clicked.connect(self.asignar_dieta)
        self.btnEliminar.clicked.connect(self.eliminar_dieta)
        self.btnCancelar.clicked.connect(self.volver_panel_principal)
    @property
    def controlador(self):
        return self._controlador

    @controlador.setter
    def controlador(self, value):
        self._controlador = value
        self.cargar_tablas()

    def cargar_tablas(self):
        self.tablaSolicitudes.setRowCount(0)
        self.tablaDietas.setRowCount(0)

        for row, sol in enumerate(self.controlador.obtener_solicitudes_dietas()):
            self.tablaSolicitudes.insertRow(row)
            for col, val in enumerate(sol):
                self.tablaSolicitudes.setItem(row, col, self._item(str(val)))

        for row, rutina in enumerate(self.controlador.obtener_dietas()):
            self.tablaDietas.insertRow(row)
            for col, val in enumerate(rutina):
                self.tablaDietas.setItem(row, col, self._item(str(val)))

    def _item(self, val):
        from PyQt6.QtWidgets import QTableWidgetItem
        item = QTableWidgetItem(val)
        item.setFlags(Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled)
        return item

    def crear_dieta(self):
        nombre = self.inputNombre.text()
        descripcion = self.inputDescripcion.toPlainText()

        exito, mensaje = self.controlador.crear_dieta(nombre, descripcion)
        if exito:
            QMessageBox.information(self, "Éxito", mensaje)
            self.inputNombre.clear()
            self.inputDescripcion.clear()
            self.cargar_tablas()
        else:
            QMessageBox.warning(self, "Error", mensaje)

    def asignar_dieta(self):
        fila_solicitud = self.tablaSolicitudes.currentRow()
        fila_dieta = self.tablaDietas.currentRow()

        if fila_solicitud == -1 or fila_dieta == -1:
            QMessageBox.warning(self, "Error", "Selecciona una solicitud y una dieta.")
            return

        id_solicitud = int(self.tablaSolicitudes.item(fila_solicitud, 0).text())
        id_socio = int(self.tablaSolicitudes.item(fila_solicitud, 1).text())
        id_dieta = int(self.tablaDietas.item(fila_dieta, 0).text())

        exito, mensaje = self.controlador.asignar_dieta(id_solicitud, id_socio, id_dieta)
        if exito:
            QMessageBox.information(self, "Éxito", mensaje)
            self.cargar_tablas()
        else:
            QMessageBox.warning(self, "Error", mensaje)

    def eliminar_dieta(self):
        fila_dieta = self.tablaDietas.currentRow()
        if fila_dieta == -1:
            QMessageBox.warning(self, "Error", "Selecciona una dieta para eliminar.")
            return

        id_dieta = int(self.tablaDietas.item(fila_dieta, 0).text())
        exito, mensaje = self.controlador.eliminar_dieta(id_dieta)
        if exito:
            QMessageBox.information(self, "Éxito", mensaje)
            self.cargar_tablas()
        else:
            QMessageBox.warning(self, "Error", mensaje)

    def volver_panel_principal(self):
        self.controlador.volver_panel_principal()
        self.close()