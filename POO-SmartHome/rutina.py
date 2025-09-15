import uuid
from datetime import time


class Rutina:
    def __init__(self, horario_inicio: time, horario_apagado: time, horario_encendido: time, estado_rutina: bool):
        self.__id = uuid.uuid4()
        self.__horario_inicio = horario_inicio
        self.__horario_apagado = horario_apagado
        self.__horario_encendido = horario_encendido
        self.__estado_rutina = estado_rutina

    @property
    def id(self):
        return self.__id

    @property
    def horario_inicio(self):
        return self.__horario_inicio

    @horario_inicio.setter
    def horario_inicio(self, nuevo_horario: time):
        self.__horario_inicio = nuevo_horario

    @property
    def horario_apagado(self):
        return self.__horario_apagado

    @horario_apagado.setter
    def horario_apagado(self, nuevo_horario: time):
        self.__horario_apagado = nuevo_horario

    @property
    def horario_encendido(self):
        return self.__horario_encendido

    @horario_encendido.setter
    def horario_encendido(self, nuevo_horario: time):
        self.__horario_encendido = nuevo_horario

    @property
    def estado_rutina(self):
        return self.__estado_rutina

    @estado_rutina.setter
    def estado_rutina(self, nuevo_estado: bool):
        self.__estado_rutina = nuevo_estado

    def cambiar_estado_rutina(self, nuevo_estado: bool) -> str:
        if self.__estado_rutina == nuevo_estado:
            return f"La rutina ya está {'activada' if nuevo_estado else 'desactivada'}."
        else:
            self.__estado_rutina = nuevo_estado
            return f"Rutina ahora {'activada' if nuevo_estado else 'desactivada'}."
