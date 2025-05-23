class EntrenadorVO:
    def __init__(self, id_entrenador=None, nombre="", apellido1="", apellido2="", usuario="", contrasena="", especialidad="", email="", telefono="", n_cuenta="", horario="", fecha_ingreso=None):
        self._id_entrenador = id_entrenador
        self._nombre = nombre
        self._apellido1 = apellido1
        self._apellido2 = apellido2
        self._usuario = usuario
        self._contrasena = contrasena
        self._especialidad = especialidad
        self._email = email
        self._telefono = telefono
        self._n_cuenta = n_cuenta
        self._horario = horario
        self._fecha_ingreso = fecha_ingreso