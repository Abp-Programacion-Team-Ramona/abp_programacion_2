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
        success = False
        while not success:
            print("¿Desea encender el ventilador? (si/no)")
            respuesta = input().lower()
            if respuesta in ("si", "sí"):
                if not self._encendido:
                    self._encendido = True
                    print("Se encendió el ventilador")
                else:
                    print("El ventilador ya estaba encendido")
                success = True
                return True
            elif respuesta == "no":
                print("El ventilador permanecerá apagado")
                success = True
                return False
            else:
                print("Respuesta inválida. Escriba 'si' o 'no'")
                
    def apagar(self):
        success = False
        while not success:
            print("¿Desea apagar el ventilador? (si/no)")
            respuesta = input().lower()
            if respuesta in ("si", "sí"):
                if self._encendido:
                    self._encendido = False
                    print("Se apagó el ventilador")
                else:
                    print("El ventilador ya estaba apagado")
                success = True
                return True
            elif respuesta == "no":
                print("El ventilador permanecerá encendido")
                success = True
                return False
            else:
                print("Respuesta inválida. Escriba 'si' o 'no'")

    def ajustar_velocidad(self):
        if not self._encendido:
            print("No se puede ajustar la velocidad si el ventilador está apagado")
            return
        success = False
        while not success:
            print("Indique una velocidad entre 1 y 3")
            nueva_velocidad = input()

            if not nueva_velocidad.isdigit():
                print("Debe ingresar un número válido (1, 2 o 3)")
            else:
                nueva_velocidad = int(nueva_velocidad)
                if 1 <= nueva_velocidad <= 3:
                    self._velocidad = nueva_velocidad
                    print(f"Velocidad ajustada a {nueva_velocidad}")
                    success = True
                else:
                    print("La velocidad debe estar entre 1 y 3")

    def ajustar_giro(self):
        if not self._encendido:
            print("No se puede ajustar el giro si el ventilador está apagado")
            return
        success = False
        while not success:
            print("¿Desea activar el giro? (si/no)")
            respuesta = input().lower()
            if respuesta in ("si", "sí"):
                self._giro = True
                print("Giro activado")
                success = True
            elif respuesta == "no":
                self._giro = False
                print("Giro desactivado")
                success = True
            else:
                print("Respuesta inválida. Escriba 'si' o 'no'")
                
