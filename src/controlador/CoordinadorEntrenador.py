from src.vista.CrearClase import CrearClase
from src.vista.CrearRutina import CrearRutina
from src.vista.CrearDieta import CrearDieta

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
    
    def abrir_crear_clase(self):
        self._ventana.close()
        self._ventana = CrearClase()
        self._ventana.controlador = self
        self._ventana.show()

    def registrar_clase(self, claseVO):
        return self._modelo.registrar_clase(claseVO)
    
    def obtener_id_entrenador_por_usuario(self, nombre_usuario):
        return self._modelo.obtener_id_entrenador_por_usuario(nombre_usuario)
    
    def abrir_crear_rutina(self):
        self._ventana.close()
        self._ventana = CrearRutina()
        self._ventana.controlador = self
        self._ventana.show()

    def obtener_solicitudes_rutinas(self):
        return self._modelo.obtener_solicitudes_rutinas()

    def obtener_rutinas(self):
        return self._modelo.obtener_rutinas()

    def crear_rutina(self, rutinaVO):
        return self._modelo.crear_rutina(rutinaVO)
    
    def asignar_rutina(self, asignarVO):
        return self._modelo.asignar_rutina(asignarVO)
    
    def eliminar_rutina(self, id_rutina):
        return self._modelo.eliminar_rutina(id_rutina)

    def abrir_crear_dieta(self):
        self._ventana.close()
        self._ventana = CrearDieta()
        self._ventana.controlador = self
        self._ventana.show()

    def obtener_solicitudes_dietas(self):
        return self._modelo.obtener_solicitudes_dietas()

    def obtener_dietas(self):
        return self._modelo.obtener_dietas()

    def crear_dieta(self, dietaVO):
        return self._modelo.crear_dieta(dietaVO)
    
    def asignar_dieta(self, asignarVO):
        return self._modelo.asignar_dieta(asignarVO)
    
    def eliminar_dieta(self, id_dieta):
        return self._modelo.eliminar_dieta(id_dieta)
