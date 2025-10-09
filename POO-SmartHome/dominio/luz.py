from dispositivo import Dispositivo

class Luz(Dispositivo):
    tabla = "luces"
    columnas = ["intensidad", "modo"]
    MODOS_VALIDOS = ("normal", "fiesta", "diurna", "nocturna")
    INTENSIDADES_VALIDAS = (1, 2, 3)

    def __init__(self, modo=None, intensidad=None, **kwargs):
        super().__init__(**kwargs)
        self._modo = "normal" if modo is None else modo
        self._intensidad = self.INTENSIDADES_VALIDAS[0] if intensidad is None else intensidad

    def get_modo(self):
        return self._modo

    def get_intensidad(self):
        return self._intensidad

    def configurar_modo(self, modo):
        m = str(modo).lower() if modo is not None else ""
        if m in self.MODOS_VALIDOS:
            self._modo = m
        else:
            print(f"Modo inválido: {modo}. Válidos: {self.MODOS_VALIDOS}")

    def configurar_intensidad(self, intensidad):
        if intensidad in self.INTENSIDADES_VALIDAS:
            self._intensidad = intensidad
        else:
            print(f"Intensidad inválida: {intensidad}. Válidas: {self.INTENSIDADES_VALIDAS}")

    def encender(self):
        try:
            super().encender()
        except AttributeError:
            if hasattr(self, "_estado"):
                if not self._estado:
                    self._estado = True
                else:
                    print("La luz ya está encendida")
            else:
                print("Encender no disponible")

    def apagar(self):
        try:
            super().apagar()
        except AttributeError:
            if hasattr(self, "_estado"):
                if self._estado:
                    self._estado = False
                else:
                    print("La luz ya está apagada")
            else:
                print("Apagar no disponible")
