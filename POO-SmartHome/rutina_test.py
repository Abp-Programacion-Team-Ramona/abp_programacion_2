import unittest
from rutina import Rutina
import uuid

class TestRutina(unittest.TestCase):
    def setUp(self):
        self.rutina = Rutina("08:00", "22:00", "08:05", False)

    def test_id_es_uuid(self):
        self.assertIsInstance(self.rutina.id, uuid.UUID)

    def test_estado_inicial(self):
        self.assertFalse(self.rutina.estado_rutina)

    def test_cambiar_estado_activar(self):
        self.rutina.cambiar_estado_rutina(True)
        self.assertTrue(self.rutina.estado_rutina)

    def test_cambiar_estado_desactivar(self):
        self.rutina.cambiar_estado_rutina(True)
        self.rutina.cambiar_estado_rutina(False)
        self.assertFalse(self.rutina.estado_rutina)

if __name__ == '__main__':
    unittest.main()
