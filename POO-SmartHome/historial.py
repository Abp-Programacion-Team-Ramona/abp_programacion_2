import uuid

class Historial:
    def __init__(self,id_dispositivo,fecha,descripcion):
        self._id=uuid.uuid4()
        self._id_dispositivo=id_dispositivo
        self._fecha=fecha
        self._descripcion=descripcion

    @property
    def id(self):
        return self._id

    @property
    def id_dispositivo(self):
        return self._id_dispositivo

    @property
    def fecha(self):
        return self.fecha

    @property
    def descripcion(self):
        return self.descripcion
