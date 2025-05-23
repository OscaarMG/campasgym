# src/vista/GestionarSocio.py
from PyQt6.QtWidgets import QWidget, QMessageBox
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from PyQt6 import uic

class GestionarSocio(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("./src/vista/ui/GestionUsu.ui", self)
        self.btnEliminar.clicked.connect(self.eliminar_usuario)
        self.btnModificar.clicked.connect(self.modificar_usuario)
        self.filterLineEdit.textChanged.connect(self.filtrar)

    @property
    def controlador(self):
        return self._controlador

    @controlador.setter
    def controlador(self, value):
        self._controlador = value
        self.controlador.cargar_socios()

    def mostrar_socios(self, socios):
        modelo = QStandardItemModel()
        # Define las columnas (encabezados)
        modelo.setHorizontalHeaderLabels(['ID', 'Nombre', 'Apellidos', 'DNI', 'Usuario', 'Email', 'Tipo Membresía'])

        for fila in socios:
            items = []
            for campo in fila:
                item = QStandardItem(str(campo))
                items.append(item)
            modelo.appendRow(items)

        self.tableView.setModel(modelo)

    def filtrar(self):
        texto = self.filterLineEdit.text()
        self.controlador.aplicar_filtro(texto)

    def eliminar_usuario(self):
        id_socio = self.obtener_id_seleccionado()
        if id_socio:
            confirmado = QMessageBox.question(
                self, 
                "Confirmar Eliminación", 
                "¿Estás seguro de eliminar este socio?", 
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
            )
            if confirmado == QMessageBox.StandardButton.Yes:
                eliminado = self.controlador.eliminar_socio(id_socio)
                if eliminado:
                    QMessageBox.information(self, "Éxito", "Socio eliminado correctamente.")
                    self.close()  # Cierra la ventana GestionarSocio
                    self.controlador.volver_panel_principal()  # Vuelve a la pantalla principal
                else:
                    QMessageBox.warning(self, "Error", "No se pudo eliminar el socio.")

    def modificar_usuario(self):
        id_socio = self.obtener_id_seleccionado()
        if id_socio:
            socio = self.controlador.obtener_socio_por_id(id_socio)
            if socio:
                self.controlador.abrir_modificar_socio(socio)
            else:
                QMessageBox.warning(self, "Error", "Socio no encontrado.")

    def obtener_id_seleccionado(self):
        index = self.tableView.currentIndex()
        if not index.isValid():
            return None
        return self.tableView.model().index(index.row(), 0).data()
