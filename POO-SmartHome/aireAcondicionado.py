import uuid
from dispositivo import Dispositivo


class AireAcondicionado(Dispositivo):
    def __init__(self, id_vivienda, id_rutina: uuid.UUID = None, rutina=None):
        super().__init__(id_vivienda, id_rutina, rutina)
        self.__temperatura = 24
        self.__velocidad = 1
        self.__modo = "frio"
        self.__estado = False

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

    def setModo(self, modo: str):
        modos_validos = ("frio", "calor", "auto", "ventilador")
        if modo.lower() in modos_validos:
            self.__modo = modo.lower()
        else:
            raise ValueError(f"Modo inválido. Debe ser uno de {modos_validos}")
