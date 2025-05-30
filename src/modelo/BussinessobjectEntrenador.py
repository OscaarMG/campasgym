from src.modelo.dao.EntrenadorDAO import EntrenadorDAO

class BussinessobjectEntrenador:

    def registrar_clase(self, claseVO):
        return EntrenadorDAO().insertar_clase(claseVO)
    
    def obtener_clases_por_entrenador(self, id_entrenador):
        return EntrenadorDAO().obtener_clases_por_entrenador(id_entrenador)
    
    def eliminar_clase(self, id_clase):
        return EntrenadorDAO().eliminar_clase(id_clase)

    def obtener_solicitudes_rutinas(self):
        return EntrenadorDAO().obtener_solicitudes_rutinas()
    
    def obtener_rutinas(self):
        return EntrenadorDAO().obtener_rutinas()
    
    def crear_rutina(self, rutinaVO):
        return EntrenadorDAO().crear_rutina(rutinaVO)
    
    def asignar_rutina(self, asginarVO):
        return EntrenadorDAO().asignar_rutina(asginarVO)

    def eliminar_rutina(self, id_rutina):
        return EntrenadorDAO().eliminar_rutina(id_rutina) 

    def obtener_solicitudes_dietas(self):
        return EntrenadorDAO().obtener_solicitudes_dietas()
    
    def obtener_dietas(self):
        return EntrenadorDAO().obtener_dietas()
    
    def crear_dieta(self, dietaVO):
        return EntrenadorDAO().crear_dieta(dietaVO)
    
    def asignar_dieta(self, asignarVO):
        return EntrenadorDAO().asignar_dieta(asignarVO)

    def eliminar_dieta(self, id_dieta):
        return EntrenadorDAO().eliminar_dieta(id_dieta)       