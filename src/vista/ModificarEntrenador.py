from PyQt6.QtWidgets import QWidget, QMessageBox
from PyQt6 import uic
from datetime import datetime
from src.modelo.vo.EntrenadorVO import EntrenadorVO

class ModificarEntrenador(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("./src/vista/ui/ModificarMonitor.ui", self)
        self.setFixedSize(self.size())
        self.btnGuardar.clicked.connect(self.guardar)
        self.btnCancelar.clicked.connect(self.volver_panel_principal)

        self._entrenador = None
        self._modo_registro = False

    @property
    def controlador(self):
        return self._controlador

    @controlador.setter
    def controlador(self, value):
        self._controlador = value

    def cargar_datos(self, entrenadorVO):
        if entrenadorVO is not None:
            self._entrenador = entrenadorVO
            self.lineEditNombre.setText(str(entrenadorVO._nombre))
            self.lineEditApellido1.setText(str(entrenadorVO._apellido1))
            self.lineEditApellido2.setText(str(entrenadorVO._apellido2))
            self.lineEditUsuario.setText(str(entrenadorVO._usuario))
            self.lineEditEspecialidad.setText(str(entrenadorVO._especialidad))
            self.lineEditEmail.setText(str(entrenadorVO._email))
            self.lineEditTelefono.setText(str(entrenadorVO._telefono))
            self.lineEditNCuenta.setText(str(entrenadorVO._n_cuenta))
            self.lineEditHorario.setText(str(entrenadorVO._horario))
            self.labelFechaIngreso.setText(str(entrenadorVO._fecha_ingreso))
            self._modo_registro = False
        else:
            self._modo_registro = True
            self._entrenador = None
            self.lineEditNombre.clear()
            self.lineEditApellido1.clear()
            self.lineEditApellido2.clear()
            self.lineEditUsuario.clear()
            self.lineEditContrasena.clear()
            self.lineEditEspecialidad.clear()
            self.lineEditEmail.clear()
            self.lineEditTelefono.clear()
            self.lineEditNCuenta.clear()
            self.lineEditHorario.clear()
            self.labelFechaIngreso.setText("Fecha actual al guardar")
    
    def guardar(self):
        # Validar mínimo básico
        if not self.lineEditNombre.text() or not self.lineEditUsuario.text() or not self.lineEditApellido1.text():
            QMessageBox.warning(self, "Error", "Nombre, apellido y usuario son obligatorios")
            return

        entrenadorVO = EntrenadorVO(
            id_entrenador=self._entrenador._id_entrenador if self._entrenador else None,
            nombre=self.lineEditNombre.text(),
            apellido1=self.lineEditApellido1.text(),
            apellido2=self.lineEditApellido2.text(),
            usuario=self.lineEditUsuario.text(),
            contrasena=self.lineEditContrasena.text(),
            especialidad=self.lineEditEspecialidad.text(),
            email=self.lineEditEmail.text(),
            telefono=self.lineEditTelefono.text(),
            n_cuenta=self.lineEditNCuenta.text(),
            horario=self.lineEditHorario.text(),
            fecha_ingreso=self._entrenador._fecha_ingreso if self._entrenador else None
        )

        if self._modo_registro:
            # Registrar nuevo Entrenador (fecha_ingreso = ahora en DAO)
            exito = self.controlador.registrar_entrenador(entrenadorVO)
        else:
            exito = self.controlador.modificar_entrenador(entrenadorVO)

        if exito:
            QMessageBox.information(self, "Éxito", "Datos guardados correctamente")
            self.controlador.abrir_gestionar_entrenador()
        else:
            QMessageBox.warning(self, "Error", "No se pudo guardar")

    def volver_panel_principal(self):
        if hasattr(self, "controlador"):
            self.controlador.volver_panel_principal()
        self.close()
