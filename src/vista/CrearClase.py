from PyQt6.QtWidgets import QWidget, QMessageBox
from PyQt6 import uic
from src.modelo.vo.ClaseVO import ClaseVO

class CrearClase(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("./src/vista/ui/crear_clase_grupal.ui", self)

        self.btnGuardar.clicked.connect(self.guardar_clase)
        self.btnCancelar.clicked.connect(self.cancelar)

    @property
    def controlador(self):
        return self._controlador

    @controlador.setter
    def controlador(self, value):
        self._controlador = value

    def guardar_clase(self):
        nombre = self.comboBoxTipoClase.currentText().strip()
        descripcion = self.textEdit.toPlainText().strip()
        horario = self.lineEditHorario.text().strip()
        lugar = self.comboBoxSala.currentText().strip()
        cupo = self.spinBoxCupoMaximo.value()
        usuario_entrenador = self.lineEditNombreEnt.text().strip()

        # Validación
        if not nombre or not horario or not lugar or not usuario_entrenador:
            QMessageBox.warning(self, "Error", "Todos los campos obligatorios deben estar llenos")
            return

        id_entrenador = self.controlador.obtener_id_entrenador_por_usuario(usuario_entrenador)
        if id_entrenador is None:
            QMessageBox.warning(self, "Error", "Nombre de usuario de entrenador no válido")
            return

        clase = ClaseVO(
            nombre=nombre,
            descripcion=descripcion,
            horario=horario,
            lugar=lugar,
            cupo_maximo=cupo,
            id_entrenador=id_entrenador
        )

        if self.controlador.registrar_clase(clase):
            QMessageBox.information(self, "Éxito", "Clase registrada correctamente")
            self.controlador.volver_panel_principal()
            self.close()
        else:
            QMessageBox.warning(self, "Error", "Error al registrar la clase")


    def cancelar(self):
        self.controlador.volver_panel_principal()
        self.close()

