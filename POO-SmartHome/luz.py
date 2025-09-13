import uuid
from dispositivo import Dispositivo


class Luz(Dispositivo):
    def __init__(self, id_vivienda: uuid.UUID, id_rutina: uuid.UUID = None, rutina=None):
        super().__init__(id_vivienda, id_rutina, rutina)
        self.modo = "apagado"
        self.intensidad = 1

    def encender(self):
        print("La Luz se encendió")

    def apagar(self):
        print("La Luz se apagó")

    def setModo(self, modo: str):
        modos_validos = ("encendido", "apagado")
        if modo.lower() in modos_validos:
            self.modo = modo.lower()
        else:
            raise ValueError(f"Modo no valido. Debe ser uno de {modos_validos}")

    def setIntensidad(self, intensidad: int):
        if intensidad in (1, 2, 3):
            self.intensidad = intensidad
        else:
            raise ValueError("La intensidad debe ser 1 (baja), 2 (media) o 3 (alta)")
