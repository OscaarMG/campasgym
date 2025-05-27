class ClaseVO:
    def __init__(self, id_clase=None, nombre="", descripcion="", horario="", lugar="", cupo_maximo=0, id_entrenador=None):
        self._id_clase = id_clase
        self._nombre = nombre
        self._descripcion = descripcion
        self._horario = horario
        self._lugar = lugar
        self._cupo_maximo = cupo_maximo
        self._id_entrenador = id_entrenador