from src.modelo.dao.SocioDAO import SocioDAO
from src.modelo.vo.InscribirseVO import InscribirseVO
from src.modelo.vo.EliminarVO import EliminarVO
from src.modelo.vo.SolicitarVO import SolicitarVO

class BussinessobjectSocio:
    
    def obtener_clases_disponibles(self):
        return SocioDAO().obtener_clases_disponibles()
    
    def obtener_rutinas_asignadas(self, id_socio):
        return SocioDAO().obtener_rutinas_asignadas(id_socio)
    
    def obtener_dietas_asignadas(self, id_socio):
        return SocioDAO().obtener_dietas_asignadas(id_socio)
    
    def inscribirse_a_clase(self, id_socio, id_clase):
        vo = InscribirseVO(id_socio=id_socio, id_clase=id_clase)
        if SocioDAO().insertar_inscripcion(vo):
            return True, "Inscripción realizada correctamente."
        else:
            return False, "Ya estás inscrito o hubo un error."

    def solicitar_rutina(self, id_socio, objetivo):
        if not objetivo:
            return False, "Debes introducir un objetivo."
        vo = SolicitarVO(id_socio=id_socio, objetivo=objetivo)
        if SocioDAO().solicitar_rutina(vo):
            return True, "Tu solicitud ha sido registrada."
        else:
            return False, "Error al registrar la solicitud."

    def eliminar_rutina(self, id_socio, id_rutina):
        vo = EliminarVO(id_socio=id_socio, id_elemento=id_rutina)
        if SocioDAO().eliminar_rutina_asignada(vo):
            return True, "Rutina eliminada correctamente."
        else:
            return False, "No se pudo eliminar la rutina."

    def solicitar_dieta(self, id_socio, objetivo):
        if not objetivo:
            return False, "Debes introducir un objetivo."
        vo = SolicitarVO(id_socio=id_socio, objetivo=objetivo)
        if SocioDAO().solicitar_dieta(vo):
            return True, "Tu solicitud ha sido registrada."
        else:
            return False, "Error al registrar la solicitud."

    def eliminar_dieta(self, id_socio, id_dieta):
        vo = EliminarVO(id_socio=id_socio, id_elemento=id_dieta)
        if SocioDAO().eliminar_dieta_asignada(vo):
            return True, "Dieta eliminada correctamente."
        else:
            return False, "No se pudo eliminar la dieta."

    def renovar_suscripcion(self, id_socio, tipo, cuenta, cvc, fecha_cad):
        if not tipo or not cuenta or not cvc or not fecha_cad:
            return False, "Todos los campos son obligatorios."

        try:
            SocioDAO().renovar_suscripcion(id_socio, tipo)
            return True, "Suscripción renovada correctamente."
        except Exception as e:
            return False, f"Fallo al renovar: {str(e)}"
    

