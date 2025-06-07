from PyQt6.QtWidgets import QWidget, QMessageBox
from PyQt6 import uic
from PyQt6.QtCore import QSortFilterProxyModel, Qt
from PyQt6.QtGui import QStandardItemModel, QStandardItem

class GestionarAdm(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("./src/vista/ui/GestionarAdm.ui", self)
        self.setFixedSize(self.size())
        self.btnEliminar.clicked.connect(self.eliminar_adm)
        self.btnModificar.clicked.connect(self.modificar_adm)
        self.btnRegistrar.clicked.connect(self.registrar_adm)
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
        self.cargar_adms()

    def cargar_adms(self):
        adms = self.controlador.obtener_adms()
        self._modelo_datos.clear()
        headers = ["ID", "Nombre", "Apellido1", "Apellido2", "Usuario", "Puesto", "Email", "Teléfono", "Nº Cuenta", "Horario", "Fecha Ingreso"]
        self._modelo_datos.setHorizontalHeaderLabels(headers)

        for a in adms:
            items = [QStandardItem(str(field)) for field in a]
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

    def eliminar_adm(self):
        id_adm = self.obtener_id_seleccionado()
        if id_adm:
            confirmado = QMessageBox.question(self, "Confirmar Eliminación", "¿Eliminar este administrativo?", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            if confirmado == QMessageBox.StandardButton.Yes:
                if self.controlador.eliminar_adm(id_adm):
                    QMessageBox.information(self, "Éxito", "administrativo eliminado")
                    self.cargar_adms()
                else:
                    QMessageBox.warning(self, "Error", "No se pudo eliminar")

    def modificar_adm(self):
        id_adm = self.obtener_id_seleccionado()
        if id_adm:
            self.controlador.abrir_modificar_adm(id_adm)

    def registrar_adm(self):
        self.controlador.abrir_registrar_adm()

    def volver_panel_principal(self):
        if hasattr(self, "controlador"):
            self.controlador.volver_panel_principal()
        self.close()