from PyQt6 import uic
from PyQt6.QtWidgets import QWidget, QMessageBox
from PyQt6.QtCore import Qt
from src.modelo.vo.RutinaVO import RutinaVO
from src.modelo.vo.AsignarVO import AsignarVO

class CrearRutina(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('src/vista/ui/CrearRutina.ui', self)
        self.setFixedSize(self.size())
        self.btnCrear.clicked.connect(self.crear_rutina)
        self.btnAsignar.clicked.connect(self.asignar_rutina)
        self.btnEliminar.clicked.connect(self.eliminar_rutina)
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
        self.tablaRutinas.setRowCount(0)

        for row, sol in enumerate(self.controlador.obtener_solicitudes_rutinas()):
            self.tablaSolicitudes.insertRow(row)
            for col, val in enumerate(sol):
                self.tablaSolicitudes.setItem(row, col, self._item(str(val)))

        for row, rutina in enumerate(self.controlador.obtener_rutinas()):
            self.tablaRutinas.insertRow(row)
            for col, val in enumerate(rutina):
                self.tablaRutinas.setItem(row, col, self._item(str(val)))

    def _item(self, val):
        from PyQt6.QtWidgets import QTableWidgetItem
        item = QTableWidgetItem(val)
        item.setFlags(Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled)
        return item

    def crear_rutina(self):
        rutinaVO = RutinaVO(
        nombre = self.inputNombre.text(),
        descripcion = self.inputDescripcion.toPlainText()
        )
        if not rutinaVO._nombre or not rutinaVO._descripcion:
            QMessageBox.warning(self, "Error", "Completa todos los campos.")
            return

        self.controlador.crear_rutina(rutinaVO)
        QMessageBox.information(self, "Éxito", "Rutina creada.")
        self.cargar_tablas()
        self.inputNombre.clear()
        self.inputDescripcion.clear()

    def asignar_rutina(self):
        fila_solicitud = self.tablaSolicitudes.currentRow()
        fila_rutina = self.tablaRutinas.currentRow()

        if fila_solicitud == -1 or fila_rutina == -1:
            QMessageBox.warning(self, "Error", "Selecciona una solicitud y una rutina.")
            return
        asignarVO = AsignarVO(
            id_solicitud = int(self.tablaSolicitudes.item(fila_solicitud, 0).text()),
            id_socio = int(self.tablaSolicitudes.item(fila_solicitud, 1).text()),
            id_asignar = int(self.tablaRutinas.item(fila_rutina, 0).text())
        )
        self.controlador.asignar_rutina(asignarVO)
        QMessageBox.information(self, "Éxito", "Rutina asignada correctamente.")
        self.cargar_tablas()

    def eliminar_rutina(self):
        fila_rutina = self.tablaRutinas.currentRow()
        if fila_rutina == -1:
            QMessageBox.warning(self, "Error", "Selecciona una rutina para eliminar.")
            return

        id_rutina = int(self.tablaRutinas.item(fila_rutina, 0).text())
        self.controlador.eliminar_rutina(id_rutina)
        QMessageBox.information(self, "Éxito", "Rutina eliminada correctamente.")
        self.cargar_tablas()

    def volver_panel_principal(self):
        self.controlador.volver_panel_principal()
        self.close()