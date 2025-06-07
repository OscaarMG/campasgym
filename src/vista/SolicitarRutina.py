from PyQt6 import uic
from PyQt6.QtWidgets import QWidget, QMessageBox, QTableWidgetItem
from PyQt6.QtCore import Qt
from src.modelo.vo.SolicitarVO import SolicitarVO
from src.modelo.vo.EliminarVO import EliminarVO

class SolicitarRutina(QWidget):
    def __init__(self, id_socio):
        super().__init__()
        uic.loadUi('src/vista/ui/SolicitarRutina.ui', self)
        self.setFixedSize(self.size())
        self.id_socio = id_socio
        

        self.btnSolicitar.clicked.connect(self.solicitar_rutina)
        self.btnEliminarRutina.clicked.connect(self.eliminar_rutina)
        self.btnCancelar.clicked.connect(self.volver_panel_principal)

    @property
    def controlador(self):
        return self._controlador

    @controlador.setter
    def controlador(self, value):
        self._controlador = value
        self.cargar_rutinas()

    def cargar_rutinas(self):
        rutinas = self.controlador.cargar_rutinas(self.id_socio)
        self.tablaRutinas.setRowCount(len(rutinas))
        for row, (id_rutina, nombre, descripcion) in enumerate(rutinas):
            self.tablaRutinas.setItem(row, 0, QTableWidgetItem(str(id_rutina)))
            self.tablaRutinas.setItem(row, 1, QTableWidgetItem(nombre))
            self.tablaRutinas.setItem(row, 2, QTableWidgetItem(descripcion))

        self.tablaRutinas.setColumnHidden(0, True)

    def solicitar_rutina(self):
        objetivo = self.inputObjetivo.toPlainText().strip()
        if not objetivo:
            QMessageBox.warning(self, "Error", "Debes introducir un objetivo.")
            return
        solicitarVO = SolicitarVO(
            id_socio=self.id_socio,
            objetivo=objetivo
        )
        self.controlador.solicitar_rutina(solicitarVO)
        QMessageBox.information(self, "Solicitud enviada", "Tu solicitud de rutina ha sido registrada.")
        self.inputObjetivo.clear()

    def eliminar_rutina(self):
        fila = self.tablaRutinas.currentRow()
        if fila == -1:
            QMessageBox.warning(self, "Error", "Selecciona una rutina para eliminar.")
            return

        id_rutina = int(self.tablaRutinas.item(fila, 0).text())
        eliminarVO = EliminarVO(
            id_socio=self.id_socio,
            id_elemento=id_rutina
        )
        self.controlador.eliminar_rutina(eliminarVO)
        QMessageBox.information(self, "Éxito", "Rutina eliminada.")
        self.cargar_rutinas()

    def volver_panel_principal(self):
        self.controlador.volver_panel_principal()
        self.close()