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
        self._modo = modo

    def get_temperatura(self):
        return self._temperatura

    def get_velocidad(self):
        return self._velocidad

    def get_modo(self):
        return self._modo

    def is_encendido(self):
        return self._estado

    def encender(self):
        if not self._estado:
            self._estado = True
        else:
            print("El dispositivo ya esta encendido")

    def apagar(self):
        if self._estado:
            self._estado = False
        else:
            print("El dispositivo ya esta apagado")

    def cambiar_modo(self):
        success = False
        while not success:
            print("Indique el nuevo modo: Frio, Calor, Auto, Ventilador")
            modo = str.lower(input())
            if modo not in self.modos_validos:
                print(f"El modo: {modo} es invalido")
            else:
                self._modo = modo
                success = True

    def cambiar_temperatura(self):
        success = False
        while not success:
            print("Indique una temperatura entre 16 y 30 grados")
            temperatura = int(input())
            if 16 <= temperatura <= 30:
                self._temperatura = temperatura
                success = True
            else:
                print("La temperatura debe estar entre 16 y 30 grados")

    def cambiar_velocidad(self):
        success = False
        while not success:
            print("Indique una velocidad entre 1 y 3")
            velocidad = int(input())
            if velocidad in (1, 2, 3):
                self._velocidad = velocidad
                success = True
            else:
                print("La velocidad debe ser 1 (baja), 2 (media) o 3 (alta)")
