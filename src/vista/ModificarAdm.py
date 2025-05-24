from PyQt6.QtWidgets import QWidget, QMessageBox
from PyQt6 import uic
from datetime import datetime
from src.modelo.vo.AdmVO import AdmVO

class ModificarAdm(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("./src/vista/ui/ModificarAdm.ui", self)

        self.btnGuardar.clicked.connect(self.guardar)
        self.btnCancelar.clicked.connect(self.volver_panel_principal)

        self._adm = None
        self._modo_registro = False

    @property
    def controlador(self):
        return self._controlador

    @controlador.setter
    def controlador(self, value):
        self._controlador = value

    def cargar_datos(self, admVO):
        if admVO is not None:
            self._adm = admVO
            self.lineEditNombre.setText(str(admVO._nombre))
            self.lineEditApellido1.setText(str(admVO._apellido1))
            self.lineEditApellido2.setText(str(admVO._apellido2))
            self.lineEditUsuario.setText(str(admVO._usuario))
            self.lineEditPuesto.setText(str(admVO._puesto))
            self.lineEditEmail.setText(str(admVO._email))
            self.lineEditTelefono.setText(str(admVO._telefono))
            self.lineEditNCuenta.setText(str(admVO._n_cuenta))
            self.lineEditHorario.setText(str(admVO._horario))
            self.labelFechaIngreso.setText(str(admVO._fecha_ingreso))
            self._modo_registro = False
        else:
            self._modo_registro = True
            self._entrenador = None
            self.lineEditNombre.clear()
            self.lineEditApellido1.clear()
            self.lineEditApellido2.clear()
            self.lineEditUsuario.clear()
            self.lineEditContrasena.clear()
            self.lineEditPuesto.clear()
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

        admVO = AdmVO(
            id_adm=self._adm._id_adm if self._adm else None,
            nombre=self.lineEditNombre.text(),
            apellido1=self.lineEditApellido1.text(),
            apellido2=self.lineEditApellido2.text(),
            usuario=self.lineEditUsuario.text(),
            contrasena=self.lineEditContrasena.text(),
            puesto=self.lineEditPuesto.text(),
            email=self.lineEditEmail.text(),
            telefono=self.lineEditTelefono.text(),
            n_cuenta=self.lineEditNCuenta.text(),
            horario=self.lineEditHorario.text(),
            fecha_ingreso=self._adm._fecha_ingreso if self._adm else None
        )

        if self._modo_registro:
            # Registrar nuevo Administrativo (fecha_ingreso = ahora en DAO)
            exito = self.controlador.registrar_adm(admVO)
        else:
            exito = self.controlador.modificar_adm(admVO)

        if exito:
            QMessageBox.information(self, "Éxito", "Datos guardados correctamente")
            self.controlador.abrir_gestionar_adm()
        else:
            QMessageBox.warning(self, "Error", "No se pudo guardar")

    def volver_panel_principal(self):
        if hasattr(self, "controlador"):
            self.controlador.volver_panel_principal()
        self.close()