from PyQt6.QtWidgets import QWidget, QMessageBox
from PyQt6 import uic
from src.modelo.vo.MaterialVO import MaterialVO

class ModificarMaterial(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("./src/vista/ui/ModificarMaterial.ui", self)
        self.setFixedSize(self.size())
        self.btnGuardar.clicked.connect(self.guardar)
        self.btnCancelar.clicked.connect(self.volver_panel_principal)
        self._material = None
        self._modo_registro = False

    @property
    def controlador(self):
        return self._controlador

    @controlador.setter
    def controlador(self, value):
        self._controlador = value

    def cargar_datos(self, materialVO):
        if materialVO is not None:
            self._material = materialVO
            self.lineEditNombre.setText(str(materialVO._nombre))
            self.spinBoxCantidad.setValue(int(materialVO._cantidad))  # <--- aquí
            self.comboBoxEstado.setCurrentText(str(materialVO._estado))
            self.lineEditUbicacion.setText(str(materialVO._ubicacion))
            self.labelFechaIngreso.setText(str(materialVO._fecha_ingreso))
            self._modo_registro = False
        else:
            self._modo_registro = True
            self._material = None
            self.lineEditNombre.clear()
            self.spinBoxCantidad.setValue(1)
            self.lineEditUbicacion.clear()
            self.labelFechaIngreso.setText("Fecha al guardar")

    def guardar(self):
        # Recolectar datos del formulario
        datos_material = {
            "id_material": self._material._id_material if self._material else None,
            "nombre": self.lineEditNombre.text(),
            "cantidad": self.spinBoxCantidad.value(),
            "estado": self.comboBoxEstado.currentText(),
            "ubicacion": self.lineEditUbicacion.text(),
            "fecha_ingreso": self._material._fecha_ingreso if self._material else None
        }

        # Llamar al controlador
        if self._modo_registro:
            exito, mensaje = self.controlador.registrar_material(datos_material)
        else:
            exito, mensaje = self.controlador.modificar_material(datos_material)

        if exito:
            QMessageBox.information(self, "Éxito", mensaje)
            self.controlador.abrir_gestionar_material()
        else:
            QMessageBox.warning(self, "Error", mensaje)
            
    def volver_panel_principal(self):
        if hasattr(self, "controlador"):
            self.controlador.volver_panel_principal()
        self.close()
