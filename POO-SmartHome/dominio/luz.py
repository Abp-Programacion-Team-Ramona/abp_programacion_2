from dispositivo import Dispositivo


class Luz(Dispositivo):
    tabla = "luces"
    columnas = ["intensidad", "modo"]

    def __init__(self, modo, intensidad, estado, **kwargs):
        super().__init__(**kwargs)
        self._modo = modo
        self._intensidad = intensidad

    def is_encendida(self):
        return self.__estado

    def get_modo(self):
        return self.__modo

    def get_intensidad(self):
        return self.__intensidad

    def encender(self):
        if not self.__estado:
            self.__estado = True
        else:
            raise RuntimeError("La luz ya está encendida")

    def apagar(self):
        if self.__estado:
            self.__estado = False
        else:
            raise RuntimeError("La luz ya está apagada")

    def setModo(self, modo: str):
        modos_validos = ("fiesta", "diurna", "nocturna")
        if modo.lower() in modos_validos:
            self.__modo = modo.lower()
        else:
            raise ValueError(f"Modo no válido. Debe ser uno de {modos_validos}")

    def setIntensidad(self, intensidad: int):
        if intensidad in (1, 2, 3):
            self.__intensidad = intensidad
        else:
            raise ValueError("La intensidad debe ser 1 (baja), 2 (media) o 3 (alta)")
