import unittest
import uuid
from luz import Luz


class TestLuz(unittest.TestCase):

    def setUp(self):
        self.luz = Luz(id_vivienda=uuid.uuid4())

    def test_encender_cuando_esta_apagada(self):
        self.assertFalse(self.luz.is_encendida())
        self.luz.encender()
        self.assertTrue(self.luz.is_encendida())

    def test_encender_cuando_ya_esta_encendida(self):
        self.luz.encender()
        with self.assertRaises(RuntimeError):
            self.luz.encender()

    def test_apagar_cuando_esta_encendida(self):
        self.luz.encender()
        self.luz.apagar()
        self.assertFalse(self.luz.is_encendida())

    def test_apagar_cuando_ya_esta_apagada(self):
        self.assertFalse(self.luz.is_encendida())
        with self.assertRaises(RuntimeError):
            self.luz.apagar()

    def test_set_modo_valido(self):
        self.luz.setModo("fiesta")
        self.assertEqual(self.luz.get_modo(), "fiesta")

    def test_set_modo_invalido(self):
        with self.assertRaises(ValueError):
            self.luz.setModo("lectura")

    def test_set_intensidad_valida(self):
        self.luz.setIntensidad(3)
        self.assertEqual(self.luz.get_intensidad(), 3)

    def test_set_intensidad_invalida(self):
        with self.assertRaises(ValueError):
            self.luz.setIntensidad(5)


if __name__ == "__main__":
    unittest.main()
