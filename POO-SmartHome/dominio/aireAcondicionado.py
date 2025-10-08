from dispositivo import Dispositivo


class AireAcondicionado(Dispositivo):
    tabla = "aires_acondicionados"
    columnas = ["temperatura", "velocidad", "modo"]
    modos_validos = ("frio", "calor", "auto", "ventilador")

    def __init__(
        self,
        temperatura: int,
        velocidad: int,
        modo: str,
        **kwargs,
    ):
        super().__init__(**kwargs)
        self._temperatura = temperatura
        self._velocidad = velocidad
        if str.lower(modo) not in self.modos_validos:
            raise ValueError(f"Modo inválido: {str.lower(modo)}")
        self.__modo = modo

    def get_temperatura(self):
        return self.__temperatura

    def get_velocidad(self):
        return self.__velocidad

    def get_modo(self):
        return self.__modo

    def is_encendido(self):
        return self.__estado

    def encender(self):
        if not self.__estado:
            self.__estado = True

    def apagar(self):
        if self.__estado:
            self.__estado = False

    def setTemperatura(self, temperatura: int):
        if 16 <= temperatura <= 30:
            self.__temperatura = temperatura
        else:
            raise ValueError("La temperatura debe estar entre 16 y 30 grados")

    def setVelocidad(self, velocidad: int):
        if velocidad in (1, 2, 3):
            self.__velocidad = velocidad
        else:
            raise ValueError("La velocidad debe ser 1 (baja), 2 (media) o 3 (alta)")
