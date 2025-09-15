from dispositivo import Dispositivo


class Ventilador(Dispositivo):

    def __init__(self, id_vivienda, id_rutina, rutina):
        super().__init__(id_vivienda, id_rutina, rutina)
        self.__velocidad = 0
        self.__giro = False

    @property
    def id_vivienda(self):
        return self.__id_vivienda

    @property
    def velocidad(self):
        return self.__velocidad

    @property
    def giro(self):
        return self.__giro

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
