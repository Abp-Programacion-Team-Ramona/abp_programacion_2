import uuid
from dispositivo import Dispositivo

class Ventilador(Dispositivo):
    
    def __init__(self, id_vivienda, id_rutina, rutina):
        super().__init__(id_vivienda, id_rutina, rutina)
        self._id = uuid.uuid4()  
        self._velocidad = 0 
        self._giro = False


    @property
    def id_vivienda(self):
        return self._id_vivienda
        
    @property
    def velocidad(self):
        return self._velocidad

    @property
    def giro(self):
        return self._giro

    
    def ajustar_velocidad(self, nueva_velocidad):
        if 0 <= nueva_velocidad <= 3:
            self._velocidad = nueva_velocidad
            print(f"Velocidad ajustada a {nueva_velocidad}")
        else:
            print("Valor de velocidad no válido (debe ser entre 0 y 3)")
        
    def ajustar_giro(self, nuevo_giro):
        if nuevo_giro in [True, False]:
            self._giro = nuevo_giro
            if nuevo_giro:
                print("Giro activado")
            else:
                print("Giro desactivado")
        else:
            print("Valor inválido: giro debe ser True o False")