from dispositivo import Dispositivo


class Ventilador(Dispositivo):
    tabla = "ventiladores"
    columnas = ["velocidad", "giro"]

    def __init__(self, velocidad: int, giro: bool, **kwargs):
        super().__init__(**kwargs)
        self._velocidad = velocidad
        self._giro = giro

    @property
    def id_vivienda(self):
        return self._id_vivienda

    @property
    def velocidad(self):
        return self._velocidad

    @property
    def giro(self):
        return self._giro

    def encender(self):
        print("Se encendio el ventilador")

    def apagar(self):
        print("Se apago el ventilador")

    def ajustar_velocidad(self, nueva_velocidad):
        if 0 <= nueva_velocidad <= 3:
            self.__velocidad = nueva_velocidad
            print(f"Velocidad ajustada a {nueva_velocidad}")
        else:
            print("Valor de velocidad no válido (debe ser entre 0 y 3)")

    def ajustar_giro(self, nuevo_giro):
        if nuevo_giro in [True, False]:
            self.__giro = nuevo_giro
            if nuevo_giro:
                print("Giro activado")
            else:
                print("Giro desactivado")
        else:
            print("Valor inválido: giro debe ser True o False")
