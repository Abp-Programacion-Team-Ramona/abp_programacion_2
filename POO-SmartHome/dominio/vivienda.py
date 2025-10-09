import uuid

class Vivienda:
    def __init__(
        self,
        nombre: str,
        id_usuario: str,
        calle: str,
        altura: str,
        piso=None,
        nota: str = None,
        id: uuid.UUID = None
    ):
        self.__id = id or uuid.uuid4()
        self.__id_usuario = id_usuario
        self.__nombre = nombre
        self.__calle = calle
        self.__altura = altura
        self.__piso = piso
        self.__nota = nota
        self.__dispositivos = []

    @property
    def id(self):
        return self.__id

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        if isinstance(nuevo_nombre, str) and nuevo_nombre.strip():
            self.__nombre = nuevo_nombre

    @property
    def id_usuario(self):
        return self.__id_usuario

    @property
    def calle(self):
        return self.__calle

    @calle.setter
    def calle(self, nueva_calle):
        if isinstance(nueva_calle, str) and nueva_calle.strip():
            self.__calle = nueva_calle

    @property
    def altura(self):
        return self.__altura

    @altura.setter
    def altura(self, nueva_altura):
        if isinstance(nueva_altura, str) and nueva_altura.strip():
            self.__altura = nueva_altura

    @property
    def piso(self):
        return self.__piso

    @piso.setter
    def piso(self, nuevo_piso):
        self.__piso = nuevo_piso

    @property
    def nota(self):
        return self.__nota

    @nota.setter
    def nota(self, nueva_nota):
        self.__nota = nueva_nota

    @property
    def dispositivos(self):
        return self.__dispositivos


    def agregar_dispositivo(self, dispositivo=None):
        if dispositivo is not None:
            if dispositivo and dispositivo not in self.__dispositivos:
                self.__dispositivos.append(dispositivo)
            return

        success = False
        while not success:
            print("Indique el nombre del dispositivo que desea agregar:")
            dispositivo = input().strip()

            if not dispositivo:
                print("El nombre del dispositivo no puede estar vacío")
            elif not isinstance(dispositivo, str):
                print("Tipo inválido, debe ingresar texto")
            elif dispositivo in self.__dispositivos:
                print(f"El dispositivo '{dispositivo}' ya existe en {self.__nombre}")
            else:
                self.__dispositivos.append(dispositivo)
                print(f"Dispositivo '{dispositivo}' agregado a {self.__nombre}")
                success = True

    def quitar_dispositivo(self, dispositivo=None):
        if dispositivo is not None:
            if dispositivo in self.__dispositivos:
                self.__dispositivos.remove(dispositivo)
            return

        success = False
        while not success:
            if not self.__dispositivos:
                print(f"{self.__nombre} no tiene dispositivos registrados")
                success = True
            else:
                print("Indique el nombre del dispositivo que desea quitar:")
                dispositivo = input().strip()

                if dispositivo in self.__dispositivos:
                    self.__dispositivos.remove(dispositivo)
                    print(f"Dispositivo '{dispositivo}' eliminado de la vivienda {self.__nombre}")
                    success = True
                else:
                    print(f"No se encontró el dispositivo '{dispositivo}' en {self.__nombre}")

    def mostrar_dispositivos(self):
        if not self.__dispositivos:
            print(f"{self.__nombre} no tiene dispositivos registrados")
            return False  
        else:
            print(f"Dispositivos en {self.__nombre}:")
            for disp in self.__dispositivos:
                print(f" - {disp}")
            return True
