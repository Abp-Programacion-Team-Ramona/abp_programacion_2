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
        self._id_vivienda = uuid.uuid4()
        self._dispositivo = DispositivoConcreto(uuid.uuid4(),uuid.uuid4(),str(self._id_vivienda),"Luz Sala",True)

    def test_cambiar_nombre_dispositivo_valido(self):
        self._dispositivo.cambiar_nombre_dispositivo("Luz Cocina")
        self.assertEqual(self._dispositivo.nombre_dispositivo, "Luz Cocina")

    def test_cambiar_nombre_dispositivo_invalido(self):
        with self.assertRaises(ValueError):
            self._dispositivo.cambiar_nombre_dispositivo("")

    def test_asignar_rutina_con_id(self):
        class Rutina:
            def __init__(self):
                self.id = uuid.uuid4()

        rutina = Rutina()
        self._dispositivo.asignar_rutina(rutina)
        self.assertEqual(self._dispositivo.rutina, rutina)
        self.assertEqual(self._dispositivo.id_rutina, rutina.id)

    def test_asignar_rutina_sin_id(self):
        class Rutina:
            pass

        rutina = Rutina()
        self._dispositivo.asignar_rutina(rutina)
        self.assertEqual(self._dispositivo.rutina, rutina)
        self.assertIsInstance(self._dispositivo.id_rutina, uuid.UUID)


if __name__ == "__main__":
    unittest.main()
