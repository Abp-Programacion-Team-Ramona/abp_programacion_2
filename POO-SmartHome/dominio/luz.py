import logging
from dispositivo import Dispositivo

logger = logging.getLogger(__name__)

class Luz(Dispositivo):
    tabla = "luces"
    columnas = ["intensidad", "modo"]
    MODOS_VALIDOS = ("fiesta", "diurna", "nocturna")

    def __init__(
        self,
        modo,
        intensidad,
        estado=False,
        modos_validos=None,
        intensidades_validas=(1, 2, 3),
        **kwargs
    ):
        super().__init__(**kwargs)
        self._estado = bool(estado)
        self._modos_validos = tuple(modos_validos) if modos_validos else self.MODOS_VALIDOS
        self._intensidades_validas = tuple(intensidades_validas)
        self._modo = None
        self._intensidad = None
        self.configurar_modo(modo)
        self.configurar_intensidad(intensidad)

    def is_encendida(self):
        return self._estado

    def get_modo(self):
        return self._modo

    def get_intensidad(self):
        return self._intensidad

    def encender(self):
        if not self._estado:
            self._estado = True
        else:
            logger.info("La luz ya está encendida")

    def apagar(self):
        if self._estado:
            self._estado = False
        else:
            logger.info("La luz ya está apagada")

    def configurar_modo(self, modo: str):
        if isinstance(modo, str) and modo.lower() in self._modos_validos:
            self._modo = modo.lower()
        else:
            logger.warning(f"Modo inválido: {modo}. Válidos: {self._modos_validos}")

    def configurar_intensidad(self, intensidad: int):
        if isinstance(intensidad, int) and intensidad in self._intensidades_validas:
            self._intensidad = intensidad
        else:
            logger.warning(
                f"Intensidad inválida: {intensidad}. Válidas: {self._intensidades_validas}"
            )
