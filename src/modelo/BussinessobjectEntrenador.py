from src.modelo.dao.EntrenadorDAO import EntrenadorDAO
from src.modelo.vo.DietaVO import DietaVO
from src.modelo.vo.AsignarVO import AsignarVO
from src.modelo.vo.RutinaVO import RutinaVO
from src.modelo.vo.ClaseVO import ClaseVO 

class BussinessobjectEntrenador:

    def registrar_clase(self, nombre, descripcion, horario, lugar, cupo_maximo, id_entrenador):
        if not nombre or not horario or not lugar:
            return False, "Todos los campos obligatorios deben estar llenos"
        if id_entrenador is None:
            return False, "Entrenador no válido"
        
        claseVO = ClaseVO(
            nombre=nombre,
            descripcion=descripcion,
            horario=horario,
            lugar=lugar,
            cupo_maximo=cupo_maximo,
            id_entrenador=id_entrenador
        )
        exito = EntrenadorDAO().insertar_clase(claseVO)
        if exito:
            return True, "Clase registrada correctamente"
        else:
            return False, "Error al registrar la clase"

    def obtener_clases_por_entrenador(self, id_entrenador):
        return EntrenadorDAO().obtener_clases_por_entrenador(id_entrenador)

    def eliminar_clase(self, id_clase):
        exito = EntrenadorDAO().eliminar_clase(id_clase)
        if exito:
            return True, "Clase cancelada correctamente"
        else:
            return False, "Error al cancelar la clase"

    def obtener_solicitudes_rutinas(self):
        return EntrenadorDAO().obtener_solicitudes_rutinas()
    
    def obtener_rutinas(self):
        return EntrenadorDAO().obtener_rutinas()
    
    def crear_rutina(self, nombre, descripcion):
        if not nombre or not descripcion:
            return False, "Completa todos los campos."
        rutinaVO = RutinaVO(nombre=nombre, descripcion=descripcion)
        EntrenadorDAO().crear_rutina(rutinaVO)
        return True, "Rutina creada."

    def asignar_rutina(self, id_solicitud, id_socio, id_asignar):
        asignarVO = AsignarVO(
            id_solicitud=id_solicitud,
            id_socio=id_socio,
            id_asignar=id_asignar
        )
        EntrenadorDAO().asignar_rutina(asignarVO)
        return True, "Rutina asignada correctamente."

    def eliminar_rutina(self, id_rutina):
        EntrenadorDAO().eliminar_rutina(id_rutina)
        return True, "Rutina eliminada correctamente." 

    def obtener_solicitudes_dietas(self):
        return EntrenadorDAO().obtener_solicitudes_dietas()
    
    def obtener_dietas(self):
        return EntrenadorDAO().obtener_dietas()
    
    def crear_dieta(self, nombre, descripcion):
        if not nombre.strip() or not descripcion.strip():
            return False, "Todos los campos son obligatorios."

        dietaVO = DietaVO(nombre=nombre.strip(), descripcion=descripcion.strip())
        exito = EntrenadorDAO().crear_dieta(dietaVO)

        if exito:
            return True, "Dieta creada correctamente."
        else:
            return False, "Error al crear la dieta."

    def asignar_dieta(self, id_solicitud, id_socio, id_dieta):
        asignarVO = AsignarVO(id_solicitud=id_solicitud, id_socio=id_socio, id_asignar=id_dieta)
        exito = EntrenadorDAO().asignar_dieta(asignarVO)

        if exito:
            return True, "Dieta asignada correctamente."
        else:
            return False, "Error al asignar la dieta."

    def eliminar_dieta(self, id_dieta):
        exito = EntrenadorDAO().eliminar_dieta(id_dieta)
        if exito:
            return True, "Dieta eliminada correctamente."
        else:
            return False, "Error al eliminar la dieta."     