import uuid


class Rutina:
    def __init__(self, horario_inicio, horario_apagado, horario_encendido, estado_rutina):
        self._id = uuid.uuid4()
        self._horario_inicio = horario_inicio
        self._horario_apagado = horario_apagado
        self._horario_encendido = horario_encendido
        self._estado_rutina = estado_rutina

    @property
    def id(self):
        return self._id

    @property
    def horario_inicio(self):
        return self._horario_inicio

    @horario_inicio.setter
    def horario_inicio(self, nuevo_horario):
        self._horario_inicio = nuevo_horario

    @property
    def horario_apagado(self):
        return self._horario_apagado

    @horario_apagado.setter
    def horario_apagado(self, nuevo_horario):
        self._horario_apagado = nuevo_horario

    @property
    def horario_encendido(self):
        return self._horario_encendido

    @horario_encendido.setter
    def horario_encendido(self, nuevo_horario):
        self._horario_encendido = nuevo_horario

    @property
    def estado_rutina(self):
        return self._estado_rutina

    def cambiar_estado_rutina(self, nuevo_estado: bool):
        if self._estado_rutina == nuevo_estado:
            print(f"La rutina ya está {'activada' if nuevo_estado else 'desactivada'}.")
        else:
            self._estado_rutina = nuevo_estado
            print(f"Rutina ahora {'activada' if nuevo_estado else 'desactivada'}.")
