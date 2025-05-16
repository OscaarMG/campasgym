from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6 import uic

# Cargar la interfaz generada desde el archivo .ui
Form, Window = uic.loadUiType("./src/vista/ui/VistaLogin.ui")

class Login(QMainWindow, Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Inicializa los widgets
        # Conectar el botón a la función
        self.BotonAceptar.clicked.connect(self.on_button_click)


    def on_button_click(self):
        print("Botón presionado")
        texto_usuario = self.UsuarioEdit.text() #Obtenet el texto del campo nombre
        texto_password = self.ContrasenaEdit.text()
        self._controlador.iniciarlogin(texto_usuario, texto_password)

    @property
    def controlador(self):
        return self._controlador
    
    @controlador.setter
    def controlador(self, value):
        self._controlador = value