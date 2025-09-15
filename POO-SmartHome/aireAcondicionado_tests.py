import unittest
import uuid
from aireAcondicionado import AireAcondicionado


class TestAireAcondicionado(unittest.TestCase):

    def setUp(self):
        self.aire = AireAcondicionado(id_vivienda=uuid.uuid4())

    def test_encender_cuando_esta_apagado(self):
        self.assertFalse(self.aire.is_encendido())
        self.aire.encender()
        self.assertTrue(self.aire.is_encendido())

    def test_encender_cuando_ya_esta_encendido(self):
        self.aire.encender()
        self.assertTrue(self.aire.is_encendido())
        self.aire.encender()
        self.assertTrue(self.aire.is_encendido())

    def test_apagar_cuando_esta_encendido(self):
        self.aire.encender()
        self.assertTrue(self.aire.is_encendido())
        self.aire.apagar()
        self.assertFalse(self.aire.is_encendido())

    def test_apagar_cuando_ya_esta_apagado(self):
        self.assertFalse(self.aire.is_encendido())
        self.aire.apagar()
        self.assertFalse(self.aire.is_encendido())

    def test_set_temperatura_valida(self):
        self.aire.setTemperatura(22)
        self.assertEqual(self.aire.get_temperatura(), 22)

    def test_set_temperatura_invalida(self):
        with self.assertRaises(ValueError):
            self.aire.setTemperatura(10)

    def test_set_velocidad_valida(self):
        self.aire.setVelocidad(3)
        self.assertEqual(self.aire.get_velocidad(), 3)

    def test_set_velocidad_invalida(self):
        with self.assertRaises(ValueError):
            self.aire.setVelocidad(5)

    def test_set_modo_valido(self):
        self.aire.setModo("Calor")
        self.assertEqual(self.aire.get_modo(), "calor")

    def test_set_modo_invalido(self):
        with self.assertRaises(ValueError):
            self.aire.setModo("turbo")


if __name__ == "__main__":
    unittest.main()
