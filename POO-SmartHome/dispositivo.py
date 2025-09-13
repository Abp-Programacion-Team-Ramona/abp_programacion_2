import uuid


class Dispositivo:
    def __init__(self, id_vivienda: uuid.UUID, id_rutina: uuid.UUID = None, rutina=None):
        self.id = uuid.uuid4()
        self.id_vivienda = id_vivienda
        self.id_rutina = id_rutina
        self.estado = False
        self.rutina = rutina

    def encender(self):
        self.estado = True

    def apagar(self):
        self.estado = False

    def asignar_rutina(self, rutina):
        self.rutina = rutina
        self.id_rutina = getattr(rutina, "id", uuid.uuid4())
