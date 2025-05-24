from PyQt6.QtWidgets import QWidget, QMessageBox
from PyQt6 import uic
from src.modelo.vo.UserVO import UserVO

class ModificarSocio(QWidget):
    def __init__(self, datos_socio):
        super().__init__()
        uic.loadUi("./src/vista/ui/ModificarSocio.ui", self)

        # Rellenar campos
        self.id_socio = datos_socio[0]
        self.txtNombre.setText(datos_socio[1])
        self.txtApellidos.setText(datos_socio[2])
        self.txtDNI.setText(datos_socio[3])
        self.txtUsuario.setText(datos_socio[4])
        self.txtEmail.setText(datos_socio[5])
        self.txtTipo.setText(datos_socio[6])  # si es un QLineEdit o usa comboBox, adapta

        self.btnGuardar.clicked.connect(self.guardar_cambios)
        self.btnCancelar.clicked.connect(self.volver_panel_principal)

    def guardar_cambios(self):
        user_vo = UserVO(
            self.txtNombre.text(),
            self.txtApellidos.text(),
            self.txtDNI.text(),
            self.txtUsuario.text(),
            "",  # Contraseña no se modifica aquí
            self.txtEmail.text(),
            self.txtTipo.text()
        )
        user_vo._id = self.id_socio

        if self.controlador.modificar_socio(user_vo):
            QMessageBox.information(self, "Éxito", "Socio modificado correctamente.")
            self.close()
            self.controlador.volver_panel_principal()
        else:
            QMessageBox.warning(self, "Error", "No se pudo modificar el socio.")

    def volver_panel_principal(self):
        if hasattr(self, "controlador"):
            self.controlador.volver_panel_principal()
        self.close()

from PyQt6.QtWidgets import QWidget, QMessageBox
from PyQt6 import uic
from src.modelo.vo.UserVO import UserVO

class ModificarSocio(QWidget):
    def __init__(self, datos_socio):
        super().__init__()
        uic.loadUi("./src/vista/ui/ModificarSocio.ui", self)

        # Rellenar campos
        self.id_socio = datos_socio[0]
        self.txtNombre.setText(datos_socio[1])
        self.txtApellidos.setText(datos_socio[2])
        self.txtDNI.setText(datos_socio[3])
        self.txtUsuario.setText(datos_socio[4])
        self.txtEmail.setText(datos_socio[5])
        self.txtTipo.setText(datos_socio[6])  # si es un QLineEdit o usa comboBox, adapta

        self.btnGuardar.clicked.connect(self.guardar_cambios)
        self.btnCancelar.clicked.connect(self.volver_panel_principal)

    def guardar_cambios(self):
        user_vo = UserVO(
            self.txtNombre.text(),
            self.txtApellidos.text(),
            self.txtDNI.text(),
            self.txtUsuario.text(),
            "",  # Contraseña no se modifica aquí
            self.txtEmail.text(),
            self.txtTipo.text()
        )
        user_vo._id = self.id_socio

        if self.controlador.modificar_socio(user_vo):
            QMessageBox.information(self, "Éxito", "Socio modificado correctamente.")
            self.close()
            self.controlador.volver_panel_principal()
        else:
            QMessageBox.warning(self, "Error", "No se pudo modificar el socio.")

    def volver_panel_principal(self):
        if hasattr(self, "controlador"):
            self.controlador.volver_panel_principal()
        self.close()
