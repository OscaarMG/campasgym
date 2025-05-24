class AdmVO:
    def __init__(self, id_adm=None, nombre="", apellido1="", apellido2="", usuario="", contrasena="", puesto="", email="", telefono="", n_cuenta="", horario="", fecha_ingreso=None):
        self._id_adm = id_adm
        self._nombre = nombre
        self._apellido1 = apellido1
        self._apellido2 = apellido2
        self._usuario = usuario
        self._contrasena = contrasena
        self._puesto = puesto
        self._email = email
        self._telefono = telefono
        self._n_cuenta = n_cuenta
        self._horario = horario
        self._fecha_ingreso = fecha_ingreso