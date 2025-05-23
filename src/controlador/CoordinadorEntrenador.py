class CoordinadorEntrenador:
    
    def __init__(self, ventana, modelo, coordinador_principal):
        self._ventana = ventana
        self._modelo = modelo
        self._coordinador_principal = coordinador_principal
        self._ventana_principal = ventana

    def cerrarsesion(self):
        self._ventana.close()
        self._coordinador_principal.cerrarsesion()

    def volver_panel_principal(self):
        self._ventana = self._ventana_principal
        self._ventana.show()