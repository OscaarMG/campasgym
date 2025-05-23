class MaterialVO:
    def __init__(self, id_material=None, nombre="", cantidad=0, estado="", ubicacion="", fecha_ingreso=None):
        self._id_material = id_material
        self._nombre = nombre
        self._cantidad = cantidad
        self._estado = estado
        self._ubicacion = ubicacion
        self._fecha_ingreso = fecha_ingreso
