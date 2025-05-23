from PyQt6.QtWidgets import QWidget, QMessageBox
from PyQt6 import uic
from PyQt6.QtCore import QSortFilterProxyModel, Qt
from PyQt6.QtGui import QStandardItemModel, QStandardItem

class GestionarMaterial(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("./src/vista/ui/GestionarMaterial.ui", self)

        self.btnEliminar.clicked.connect(self.eliminar_material)
        self.btnModificar.clicked.connect(self.modificar_material)
        self.btnAnadir.clicked.connect(self.registrar_material)
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
        self.cargar_materiales()

    def filtrar(self):
        self.proxy_model.setFilterFixedString(self.filterLineEdit.text())


    def cargar_materiales(self):
        materiales = self.controlador.obtener_materiales()
        self._modelo_datos.clear()
        headers = ["ID", "Nombre", "Cantidad", "Estado", "Ubicación", "Fecha Ingreso"]
        self._modelo_datos.setHorizontalHeaderLabels(headers)

        for m in materiales:
            items = [QStandardItem(str(field)) for field in m]
            self._modelo_datos.appendRow(items)

    def obtener_id_seleccionado(self):
        index = self.tableView.currentIndex()
        if not index.isValid():
            return None
        index_source = self.proxy_model.mapToSource(index)
        return int(self._modelo_datos.item(index_source.row(), 0).text())  # columna 0: id_material

    def eliminar_material(self):
        id_material = self.obtener_id_seleccionado()
        if id_material:
            confirmado = QMessageBox.question(self, "Confirmar", "¿Eliminar este material?",
                                            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            if confirmado == QMessageBox.StandardButton.Yes:
                if self.controlador.eliminar_material(id_material):
                    QMessageBox.information(self, "Éxito", "Material eliminado")
                    self.cargar_materiales()
                else:
                    QMessageBox.warning(self, "Error", "No se pudo eliminar")


    def modificar_material(self):
        id_material = self.obtener_id_seleccionado()
        if id_material:
            self.controlador.abrir_modificar_material(id_material)

    def registrar_material(self):
        self.controlador.abrir_registrar_material()

    def volver_panel_principal(self):
        self.controlador.volver_panel_principal()
        self.close()