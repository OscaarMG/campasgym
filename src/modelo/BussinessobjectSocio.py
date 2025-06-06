from src.modelo.dao.SocioDAO import SocioDAO

class BussinessobjectSocio:
    
    def obtener_clases_disponibles(self):
        return SocioDAO().obtener_clases_disponibles()

    def inscribirse_a_clase(self, inscribirseVO):
        return SocioDAO().insertar_inscripcion(inscribirseVO)
    
    def obtener_rutinas_asignadas(self, id_socio):
        return SocioDAO().obtener_rutinas_asignadas(id_socio)
    
    def eliminar_rutina_asignada(self, eliminarVO):
        return SocioDAO().eliminar_rutina_asignada(eliminarVO)
    
    def solicitar_rutina(self, solicitarVO):
        return SocioDAO().solicitar_rutina(solicitarVO)
    
    def obtener_dietas_asignadas(self, id_socio):
        return SocioDAO().obtener_dietas_asignadas(id_socio)
    
    def eliminar_dieta_asignada(self, eliminarVO):
        return SocioDAO().eliminar_dieta_asignada(eliminarVO)
    
    def solicitar_dieta(self, solicitarVO):
        return SocioDAO().solicitar_dieta(solicitarVO)

    def eliminar_socio(self, id_socio):
        return SocioDAO().eliminar_socio(id_socio)

    def renovar_suscripcion(self, id_socio, tipo):
        return SocioDAO().renovar_suscripcion(id_socio, tipo)
