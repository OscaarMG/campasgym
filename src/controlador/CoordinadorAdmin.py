from src.vista.RegistrarUsu import RegistrarUsu
from src.vista.GestionarSocio import GestionarSocio
from src.vista.ModificarSocio import ModificarSocio
from src.modelo.vo.UserVO import UserVO
from src.vista.GestionarEntrenador import GestionarEntrenador
from src.vista.ModificarEntrenador import ModificarEntrenador
from src.modelo.vo.EntrenadorVO import EntrenadorVO
from src.vista.GestionarMaterial import GestionarMaterial
from src.vista.ModificarMaterial import ModificarMaterial
from src.modelo.vo.MaterialVO import MaterialVO
from src.vista.ModificarMaterial import ModificarMaterial

class CoordinadorAdmin:
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

    def abrir_registrar(self):
            self._ventana.close()
            self._ventana = RegistrarUsu()
            self._ventana.controlador = self
            self._ventana.show()


    def registrar_usuario(self, nombre, apellidos, dni, usuario, contrasena, email, tipo):
        user_vo = UserVO(nombre, apellidos, dni, usuario, contrasena, email, tipo)
        return self._modelo.registrar_usuario(user_vo)

    def abrir_gestionar_socio(self):
        self._ventana.close()
        self._ventana = GestionarSocio()
        self._ventana.controlador = self  # Esto ya carga los socios
        self._ventana.show()

    def cargar_socios(self):
        socios = self.obtener_socios()  # Obtiene los datos desde el modelo
        self._ventana.mostrar_socios(socios)

    def obtener_socios(self):
        return self._modelo.obtener_socios()
    
    def aplicar_filtro(self, texto):
        socios = self.obtener_socios()
        if texto:
            texto = texto.lower()
            socios_filtrados = [s for s in socios if texto in str(s).lower()]
        else:
            socios_filtrados = socios
        self._ventana.mostrar_socios(socios_filtrados)


    def eliminar_socio(self, id_socio):
        return self._modelo.eliminar_socio(id_socio)
    
    def modificar_socio(self, user_vo):
        return self._modelo.modificar_socio(user_vo)
    
    def obtener_socio_por_id(self, id_socio):
        socios = self.obtener_socios()
        for socio in socios:
            if str(socio[0]) == str(id_socio):
                return socio
        return None

    def abrir_modificar_socio(self, datos_socio):
        self._ventana.close()
        self._ventana = ModificarSocio(datos_socio)
        self._ventana.controlador = self
        self._ventana.show()

    def abrir_gestionar_entrenador(self):
        self._ventana.close()
        self._ventana = GestionarEntrenador()
        self._ventana.controlador = self
        self._ventana.show()

    def obtener_entrenadores(self):
        return self._modelo.obtener_entrenadores()

    def eliminar_entrenador(self, id_entrenador):
        return self._modelo.eliminar_entrenador(id_entrenador)

    def abrir_modificar_entrenador(self, id_entrenador):
        self._ventana.close()
        self._ventana = ModificarEntrenador()
        self._ventana.controlador = self

        entrenadores = self.obtener_entrenadores()
        entrenador_datos = None
        for en in entrenadores:
            if str(en[0]) == str(id_entrenador):
                entrenador_datos = en
                break

        if not entrenador_datos:
            print("Entrenador no encontrado")
            return

        entrenadorVO = EntrenadorVO(
            id_entrenador=entrenador_datos[0],
            nombre=entrenador_datos[1],
            apellido1=entrenador_datos[2],
            apellido2=entrenador_datos[3],
            usuario=entrenador_datos[4],
            contrasena="",  # Por seguridad
            especialidad=entrenador_datos[5],
            email=entrenador_datos[6],
            telefono=entrenador_datos[7],
            n_cuenta=entrenador_datos[8],
            horario=entrenador_datos[9],
            fecha_ingreso=entrenador_datos[10]
        )

        self._ventana.cargar_datos(entrenadorVO)
        self._ventana.show()


    def abrir_registrar_entrenador(self):
        self._ventana.close()
        self._ventana = ModificarEntrenador()
        self._ventana.controlador = self
        self._ventana.cargar_datos(None)
        self._ventana.show()

    def registrar_entrenador(self, entrenador_vo: EntrenadorVO):
        return self._modelo.registrar_entrenador(entrenador_vo)
    
    def modificar_entrenador(self, entrenador_vo):
        return self._modelo.modificar_entrenador(entrenador_vo)
    
    def abrir_gestionar_material(self):
        self._ventana.close()
        self._ventana = GestionarMaterial()
        self._ventana.controlador = self
        self._ventana.show()

    def obtener_materiales(self):
        return self._modelo.obtener_materiales()

    def abrir_modificar_material(self, id_material):
        self._ventana.close()
        self._ventana = ModificarMaterial()
        self._ventana.controlador = self

        materiales = self.obtener_materiales()
        for mat in materiales:
            if str(mat[0]) == str(id_material):
                vo = MaterialVO(
                    id_material=mat[0],
                    nombre=mat[1],
                    cantidad=mat[2],
                    estado=mat[3],
                    ubicacion=mat[4],
                    fecha_ingreso=mat[5]
                )
                self._ventana.cargar_datos(vo)
                break

        self._ventana.show()

    def eliminar_material(self, id_material):
        return self._modelo.eliminar_material(id_material)

    def abrir_registrar_material(self):
        self._ventana.close()
        self._ventana = ModificarMaterial()
        self._ventana.controlador = self
        self._ventana.cargar_datos(None)
        self._ventana.show()

    def registrar_material(self, materialVO):
        return self._modelo.registrar_material(materialVO)

    def modificar_material(self, materialVO):
        return self._modelo.modificar_material(materialVO)