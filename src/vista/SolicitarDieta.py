from PyQt6 import uic
from PyQt6.QtWidgets import QWidget, QMessageBox, QTableWidgetItem
from PyQt6.QtCore import Qt
from src.modelo.vo.SolicitarVO import SolicitarVO
from src.modelo.vo.EliminarVO import EliminarVO

class SolicitarDieta(QWidget):
    def __init__(self, id_socio):
        super().__init__()
        uic.loadUi('src/vista/ui/SolicitarDieta.ui', self)
        self.setFixedSize(self.size())
        self.id_socio = id_socio
        

        self.btnSolicitar.clicked.connect(self.solicitar_dieta)
        self.btnEliminarRutina.clicked.connect(self.eliminar_dieta)
        self.btnCancelar.clicked.connect(self.volver_panel_principal)

    @property
    def controlador(self):
        return self._controlador

    @controlador.setter
    def controlador(self, value):
        self._controlador = value
        self.cargar_dietas()

    def cargar_dietas(self):
        dietas = self.controlador.cargar_dietas(self.id_socio)
        self.tablaDietas.setRowCount(len(dietas))
        for row, (id_dieta, nombre, descripcion) in enumerate(dietas):
            self.tablaDietas.setItem(row, 0, QTableWidgetItem(str(id_dieta)))
            self.tablaDietas.setItem(row, 1, QTableWidgetItem(nombre))
            self.tablaDietas.setItem(row, 2, QTableWidgetItem(descripcion))

        self.tablaDietas.setColumnHidden(0, True)

    def solicitar_dieta(self):
        objetivo = self.inputObjetivo.toPlainText().strip()
        exito, mensaje = self.controlador.solicitar_dieta(self.id_socio, objetivo)
        if exito:
            QMessageBox.information(self, "Solicitud enviada", mensaje)
            self.inputObjetivo.clear()
        else:
            QMessageBox.warning(self, "Error", mensaje)

    def eliminar_dieta(self):
        fila = self.tablaDietas.currentRow()
        if fila == -1:
            QMessageBox.warning(self, "Error", "Selecciona una dieta para eliminar.")
            return

        id_dieta = int(self.tablaDietas.item(fila, 0).text())
        exito, mensaje = self.controlador.eliminar_dieta(self.id_socio, id_dieta)
        if exito:
            QMessageBox.information(self, "Éxito", mensaje)
            self.cargar_dietas()
        else:
            QMessageBox.warning(self, "Error", mensaje)


    def volver_panel_principal(self):
        self.controlador.volver_panel_principal()
        self.close()