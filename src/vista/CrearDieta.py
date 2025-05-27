from PyQt6 import uic
from PyQt6.QtWidgets import QWidget, QMessageBox
from PyQt6.QtCore import Qt
from src.modelo.vo.DietaVO import DietaVO
from src.modelo.vo.AsignarVO import AsignarVO

class CrearDieta(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('src/vista/ui/CrearDieta.ui', self)

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
        dietaVO = DietaVO(
        nombre = self.inputNombre.text(),
        descripcion = self.inputDescripcion.toPlainText()
        )
        if not dietaVO._nombre or not dietaVO._descripcion:
            QMessageBox.warning(self, "Error", "Completa todos los campos.")
            return

        self.controlador.crear_dieta(dietaVO)
        QMessageBox.information(self, "Éxito", "Dieta creada.")
        self.cargar_tablas()
        self.inputNombre.clear()
        self.inputDescripcion.clear()

    def asignar_dieta(self):
        fila_solicitud = self.tablaSolicitudes.currentRow()
        fila_dieta = self.tablaDietas.currentRow()

        if fila_solicitud == -1 or fila_dieta == -1:
            QMessageBox.warning(self, "Error", "Selecciona una solicitud y una dieta.")
            return
        asignarVO = AsignarVO(
            id_solicitud = int(self.tablaSolicitudes.item(fila_solicitud, 0).text()),
            id_socio = int(self.tablaSolicitudes.item(fila_solicitud, 1).text()),
            id_asignar = int(self.tablaDietas.item(fila_dieta, 0).text())
        )
        self.controlador.asignar_dieta(asignarVO)
        QMessageBox.information(self, "Éxito", "Dieta asignada correctamente.")
        self.cargar_tablas()

    def eliminar_dieta(self):
        fila_dieta = self.tablaDietas.currentRow()
        if fila_dieta == -1:
            QMessageBox.warning(self, "Error", "Selecciona una dieta para eliminar.")
            return

        id_dieta = int(self.tablaDietas.item(fila_dieta, 0).text())
        self.controlador.eliminar_dieta(id_dieta)
        QMessageBox.information(self, "Éxito", "Dieta eliminada correctamente.")
        self.cargar_tablas()

    def volver_panel_principal(self):
        self.controlador.volver_panel_principal()
        self.close()