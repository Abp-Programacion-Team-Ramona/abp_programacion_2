import unittest
import uuid
from dispositivo import Dispositivo


class DispositivoConcreto(Dispositivo):
    def encender(self):
        self._estado = True

    def apagar(self):
        self._estado = False


class TestDispositivo(unittest.TestCase):
    def setUp(self):
        self.id_vivienda = uuid.uuid4()
        self.dispositivo = DispositivoConcreto(self.id_vivienda, "Luz Sala")

    def test_cambiar_nombre_dispositivo_valido(self):
        self.dispositivo.cambiar_nombre_dispositivo("Luz Cocina")
        self.assertEqual(self.dispositivo.nombre_dispositivo, "Luz Cocina")

    def test_cambiar_nombre_dispositivo_invalido(self):
        with self.assertRaises(ValueError):
            self.dispositivo.cambiar_nombre_dispositivo("")

    def test_asignar_rutina_con_id(self):
        class Rutina:
            def __init__(self):
                self.id = uuid.uuid4()

        rutina = Rutina()
        self.dispositivo.asignar_rutina(rutina)
        self.assertEqual(self.dispositivo.rutina, rutina)
        self.assertEqual(self.dispositivo.id_rutina, rutina.id)

    def test_asignar_rutina_sin_id(self):
        class Rutina:
            pass

        rutina = Rutina()
        self.dispositivo.asignar_rutina(rutina)
        self.assertEqual(self.dispositivo.rutina, rutina)
        self.assertIsInstance(self.dispositivo.id_rutina, uuid.UUID)

    def test_encender_y_apagar(self):
        self.dispositivo.encender()
        self.assertTrue(self.dispositivo.estado)
        self.dispositivo.apagar()
        self.assertFalse(self.dispositivo.estado)


if __name__ == "__main__":
    unittest.main()
