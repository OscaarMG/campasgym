from PyQt6.QtWidgets import QWidget, QMessageBox
from PyQt6 import uic
from PyQt6.QtCore import QSortFilterProxyModel, Qt
from PyQt6.QtGui import QStandardItemModel, QStandardItem

class GestionarEntrenador(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("./src/vista/ui/GestionarEnt.ui", self)

        self.btnEliminar.clicked.connect(self.eliminar_entrenador)
        self.btnModificar.clicked.connect(self.modificar_entrenador)
        self.btnRegistrar.clicked.connect(self.registrar_entrenador)
        self.btnCancelar.clicked.connect(self.volver_panel_principal)
        self.filterLineEdit.textChanged.connect(self.filtrar)

        self._modelo_datos = QStandardItemModel()
        self.proxy_model = QSortFilterProxyModel()
        self.proxy_model.setSourceModel(self._modelo_datos)
        self.proxy_model.setFilterCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)
        self.tableView.setModel(self.proxy_model)
        self.tableView.setSortingEnabled(True)

    @property
    def controlador(self):
        return self._controlador

    @controlador.setter
    def controlador(self, value):
        self._controlador = value
        self.cargar_entrenadores()

    def cargar_entrenadores(self):
        entrenadores = self.controlador.obtener_entrenadores()
        self._modelo_datos.clear()
        headers = ["ID", "Nombre", "Apellido1", "Apellido2", "Usuario", "Especialidad", "Email", "Teléfono", "Nº Cuenta", "Horario", "Fecha Ingreso"]
        self._modelo_datos.setHorizontalHeaderLabels(headers)

        for en in entrenadores:
            items = [QStandardItem(str(field)) for field in en]
            self._modelo_datos.appendRow(items)

    def filtrar(self):
        texto = self.filterLineEdit.text()
        self.proxy_model.setFilterFixedString(texto)

    def obtener_id_seleccionado(self):
        index = self.tableView.currentIndex()
        if not index.isValid():
            return None
        index_source = self.proxy_model.mapToSource(index)
        return int(self._modelo_datos.item(index_source.row(), 0).text())

    def eliminar_entrenador(self):
        id_entrenador = self.obtener_id_seleccionado()
        if id_entrenador:
            confirmado = QMessageBox.question(self, "Confirmar Eliminación", "¿Eliminar este entrenador?", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            if confirmado == QMessageBox.StandardButton.Yes:
                if self.controlador.eliminar_entrenador(id_entrenador):
                    QMessageBox.information(self, "Éxito", "entrenador eliminado")
                    self.cargar_entrenadores()
                else:
                    QMessageBox.warning(self, "Error", "No se pudo eliminar")

    def modificar_entrenador(self):
        id_entrenador = self.obtener_id_seleccionado()
        if id_entrenador:
            self.controlador.abrir_modificar_entrenador(id_entrenador)

    def registrar_entrenador(self):
        self.controlador.abrir_registrar_entrenador()

    def volver_panel_principal(self):
        if hasattr(self, "controlador"):
            self.controlador.volver_panel_principal()
        self.close()