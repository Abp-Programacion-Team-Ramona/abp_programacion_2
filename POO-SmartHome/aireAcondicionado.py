import uuid
from dispositivo import Dispositivo


class AireAcondicionado(Dispositivo):
    def __init__(self, id_vivienda, id_rutina: uuid.UUID = None, rutina=None):
        super().__init__(id_vivienda, id_rutina, rutina)
        self.temperatura = 24
        self.velocidad = 1
        self.modo = "frio"

    def get_temperatura(self):
        return self.temperatura

    def get_velocidad(self):
        return self.velocidad

    def get_modo(self):
        return self.modo

    def encender(self):
        if not self.estado:
            print("Encendiendo Aire Acondicionado")
        print("El aire acondicionado ya esta encendido")

    def apagar(self):
        if not self.estado:
            print("Apagando Aire Acondicionado")
        print("El aire acondicionado ya esta apagado.")

    def setTemperatura(self, temperatura: int):
        if 16 <= temperatura <= 30:
            self.temperatura = temperatura
        else:
            raise ValueError("La temperatura debe estar entre 16 y 30 grados")

    def setVelocidad(self, velocidad: int):
        if velocidad in (1, 2, 3):
            self.velocidad = velocidad
        else:
            raise ValueError("La velocidad debe ser 1 (baja), 2 (media) o 3 (alta)")

    def setModo(self, modo: str):
        modos_validos = ("frio", "calor", "auto", "ventilador")
        if modo.lower() in modos_validos:
            self.modo = modo.lower()
        else:
            raise ValueError(f"Modo inválido. Debe ser uno de {modos_validos}")
