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
    
    def abrir_crear_clase(self, id_entrenador):
        self._ventana.close()
        self._ventana = CrearClase(id_entrenador)
        self._ventana.controlador = self
        self._ventana.show()

    def registrar_clase(self, nombre, descripcion, horario, lugar, cupo_maximo, id_entrenador):
        return self._modelo.registrar_clase(nombre, descripcion, horario, lugar, cupo_maximo, id_entrenador)

    def obtener_clases_por_entrenador(self, id_entrenador):
        return self._modelo.obtener_clases_por_entrenador(id_entrenador)

    def eliminar_clase(self, id_clase):
        return self._modelo.eliminar_clase(id_clase)

    def abrir_crear_rutina(self):
        self._ventana.close()
        self._ventana = CrearRutina()
        self._ventana.controlador = self
        self._ventana.show()

    def obtener_solicitudes_rutinas(self):
        return self._modelo.obtener_solicitudes_rutinas()

    def obtener_rutinas(self):
        return self._modelo.obtener_rutinas()

    def crear_rutina(self, nombre, descripcion):
        return self._modelo.crear_rutina(nombre, descripcion)

    def asignar_rutina(self, id_solicitud, id_socio, id_asignar):
        return self._modelo.asignar_rutina(id_solicitud, id_socio, id_asignar)

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

    def crear_dieta(self, nombre, descripcion):
        return self._modelo.crear_dieta(nombre, descripcion)

    def asignar_dieta(self, id_solicitud, id_socio, id_dieta):
        return self._modelo.asignar_dieta(id_solicitud, id_socio, id_dieta)

    def eliminar_dieta(self, id_dieta):
        return self._modelo.eliminar_dieta(id_dieta)
