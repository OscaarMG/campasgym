from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6 import uic
from src.vista.RecuContra1 import RecuContra1

# Cargar la interfaz generada desde el archivo .ui
Form, Window = uic.loadUiType("./src/vista/ui/VistaLogin.ui")

class Login(QMainWindow, Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Inicializa los widgets
        self.setFixedSize(self.size())
        # Conectar el botón a la función
        self.BotonAceptar.clicked.connect(self.on_button_click)
        self.BotonRecuContra.clicked.connect(self.recuperar_contrasena)

    def on_button_click(self):
        print("Botón presionado")
        texto_usuario = self.UsuarioEdit.text() #Obtenet el texto del campo nombre
        texto_password = self.ContrasenaEdit.text()
        self._controlador.iniciarlogin(texto_usuario, texto_password)

    def resetear(self):
        """Limpia los campos del formulario al cerra sesión."""
        self.UsuarioEdit.clear()
        self.ContrasenaEdit.clear()

    def recuperar_contrasena(self):
        self.ventana_recuperar = RecuContra1(self._controlador)
        self.ventana_recuperar.show()
        self.close()

    @property
    def controlador(self):
        return self._controlador
    
    @controlador.setter
    def controlador(self, value):
        self._controlador = value

