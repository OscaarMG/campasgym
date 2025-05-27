from PyQt6 import uic
from PyQt6.QtWidgets import QWidget, QMessageBox, QTableWidgetItem
from PyQt6.QtCore import Qt
from src.modelo.vo.InscribirseVO import InscribirseVO

class VerClasesDisponibles(QWidget):
    def __init__(self, id_socio):
        super().__init__()
        uic.loadUi('src/vista/ui/VerClasesDisponibles.ui', self)
        self.id_socio = id_socio

        self.btnApuntarse.clicked.connect(self.apuntarse_clase)
        self.btnVolver.clicked.connect(self.volver_panel_principal)
    
    @property
    def controlador(self):
        return self._controlador

    @controlador.setter
    def controlador(self, value):
        self._controlador = value
        self.cargar_tabla()

    def cargar_tabla(self):
        clases = self._controlador.obtener_clases_disponibles()
        self.tablaClases.setRowCount(len(clases))
        self.tablaClases.setColumnCount(4)
        self.tablaClases.setHorizontalHeaderLabels(["ID", "Nombre", "Horario", "Apuntados"])

        for row_idx, clase in enumerate(clases):
            id_clase, nombre, horario, cupo_max, apuntados = clase
            self.tablaClases.setItem(row_idx, 0, self._item(str(id_clase)))
            self.tablaClases.setItem(row_idx, 1, self._item(nombre))
            self.tablaClases.setItem(row_idx, 2, self._item(horario))
            self.tablaClases.setItem(row_idx, 3, self._item(f"{apuntados}/{cupo_max}"))

        self.tablaClases.setColumnHidden(0, True)

    def apuntarse_clase(self):
        fila = self.tablaClases.currentRow()
        if fila == -1:
            QMessageBox.warning(self, "Error", "Selecciona una clase")
            return

        id_clase = int(self.tablaClases.item(fila, 0).text())
        inscribirseVO = InscribirseVO(
            id_socio=self.id_socio,
            id_clase=id_clase
        )
        if self.controlador.inscribirse_a_clase(inscribirseVO):
            QMessageBox.information(self, "Éxito", "Inscripción realizada")
            self.cargar_tabla()
        else:
            QMessageBox.warning(self, "Error", "Ya estás inscrito o ocurrió un error")

    def _item(self, texto):
        item = QTableWidgetItem(texto)
        flags = Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled
        item.setFlags(flags)
        return item
    
    def volver_panel_principal(self):
        self.controlador.volver_panel_principal()
        self.close()
