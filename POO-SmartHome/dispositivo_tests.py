import unittest
import uuid
from dispositivo import Dispositivo


class DispositivoConcreto(Dispositivo):
    def encender(self):
        self.__estado = True

    def apagar(self):
        self.__estado = False


class TestDispositivo(unittest.TestCase):
    def setUp(self):
        self.__id_vivienda = uuid.uuid4()
        self.__dispositivo = DispositivoConcreto(self.__id_vivienda, "Luz Sala")

    def test_cambiar_nombre_dispositivo_valido(self):
        self.__dispositivo.cambiar_nombre_dispositivo("Luz Cocina")
        self.assertEqual(self.__dispositivo.nombre_dispositivo, "Luz Cocina")

    def test_cambiar_nombre_dispositivo_invalido(self):
        with self.assertRaises(ValueError):
            self.__dispositivo.cambiar_nombre_dispositivo("")

    def test_asignar_rutina_con_id(self):
        class Rutina:
            def __init__(self):
                self.id = uuid.uuid4()

        rutina = Rutina()
        self.__dispositivo.asignar_rutina(rutina)
        self.assertEqual(self.__dispositivo.rutina, rutina)
        self.assertEqual(self.__dispositivo.id_rutina, rutina.id)

    def test_asignar_rutina_sin_id(self):
        class Rutina:
            pass

        rutina = Rutina()
        self.__dispositivo.asignar_rutina(rutina)
        self.assertEqual(self.__dispositivo.rutina, rutina)
        self.assertIsInstance(self.__dispositivo.id_rutina, uuid.UUID)


if __name__ == "__main__":
    unittest.main()
