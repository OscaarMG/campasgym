from src.vista.VerClasesDisponibles import VerClasesDisponibles
from src.vista.SolicitarRutina import SolicitarRutina
from src.vista.SolicitarDieta import SolicitarDieta
from src.vista.RenovarSuscripcion import RenovarSuscripcion

class CoordinadorSocio:

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

    def abrir_apuntarse_clase(self, id_socio):
        self._ventana.close()
        self._ventana = VerClasesDisponibles(id_socio)
        self._ventana.controlador = self
        self._ventana.show()

    def obtener_clases_disponibles(self):
        return self._modelo.obtener_clases_disponibles()
    
    def apuntarse_a_clase(self, id_socio, id_clase):
        return self._modelo.inscribirse_a_clase(id_socio, id_clase)
    
    def cargar_rutinas(self, id_socio):
        return self._modelo.obtener_rutinas_asignadas(id_socio)

    def eliminar_rutina(self, id_socio, id_rutina):
        return self._modelo.eliminar_rutina_asignada(id_socio, id_rutina)

    def renovar_suscripcion(self, id_socio, tipo, cuenta, cvc, fecha_cad):
        return self._modelo.renovar_suscripcion(id_socio, tipo, cuenta, cvc, fecha_cad)

    def solicitar_rutina(self, id_socio, objetivo):
        return self._modelo.solicitar_rutina(id_socio, objetivo)
    
    def abrir_rutina(self, id_socio):
        self._ventana.close()
        self._ventana = SolicitarRutina(id_socio)
        self._ventana.controlador = self
        self._ventana.show()

    def cargar_dietas(self, id_socio):
        return self._modelo.obtener_dietas_asignadas(id_socio)

    def eliminar_dieta(self, id_socio, id_dieta):
        return self._modelo.eliminar_dieta_asignada(id_socio, id_dieta)

    def solicitar_dieta(self, id_socio, objetivo):
        return self._modelo.solicitar_dieta(id_socio, objetivo)
    
    def abrir_dieta(self, id_socio):
        self._ventana.close()
        self._ventana = SolicitarDieta(id_socio)
        self._ventana.controlador = self
        self._ventana.show()

    def dar_de_baja_socio(self, id_socio):
        return self._modelo.eliminar_socio(id_socio)

    def abrir_renovar_suscripcion(self, id_socio):
        self._ventana.close()
        self._ventana = RenovarSuscripcion(id_socio)
        self._ventana.controlador = self
        self._ventana.show()
