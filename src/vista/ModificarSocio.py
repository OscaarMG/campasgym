from PyQt6.QtWidgets import QWidget, QMessageBox
from PyQt6 import uic
from src.modelo.vo.UserVO import UserVO

class ModificarSocio(QWidget):
    def __init__(self, datos_socio):
        super().__init__()
        uic.loadUi("./src/vista/ui/ModificarSocio.ui", self)
        self.setFixedSize(self.size())
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
        datos_usuario = {
            "id": self.id_socio,
            "nombre": self.txtNombre.text(),
            "apellidos": self.txtApellidos.text(),
            "dni": self.txtDNI.text(),
            "usuario": self.txtUsuario.text(),
            "email": self.txtEmail.text(),
            "tipo": self.txtTipo.text()
        }

        exito, mensaje = self.controlador.modificar_socio(datos_usuario)
        
        if exito:
            QMessageBox.information(self, "Éxito", mensaje)
            self.close()
            self.controlador.volver_panel_principal()
        else:
            QMessageBox.warning(self, "Error", mensaje)

    def volver_panel_principal(self):
        if hasattr(self, "controlador"):
            self.controlador.volver_panel_principal()
        self.close()
