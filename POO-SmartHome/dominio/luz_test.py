import unittest
import uuid
from luz import Luz


class TestLuz(unittest.TestCase):
    def setUp(self):
        self.luz = Luz(modo="fiesta", intensidad=1, id_vivienda=uuid.uuid4())

    def test_encender_cuando_esta_apagada(self):
        self.assertFalse(self.luz.is_encendida())
        self.luz.encender()
        self.assertTrue(self.luz.is_encendida())

    def test_encender_cuando_ya_esta_encendida(self):
        self.luz.encender()
        self.luz.encender()
        self.assertTrue(self.luz.is_encendida())

    def test_apagar_cuando_esta_encendida(self):
        self.luz.encender()
        self.luz.apagar()
        self.assertFalse(self.luz.is_encendida())

    def test_apagar_cuando_ya_esta_apagada(self):
        self.assertFalse(self.luz.is_encendida())
        self.luz.apagar()
        self.assertFalse(self.luz.is_encendida())

    def test_configurar_modo_valido(self):
        self.luz.configurar_modo("diurna")
        self.assertEqual(self.luz.get_modo(), "diurna")

    def test_configurar_modo_invalido(self):
        self.assertEqual(self.luz.get_modo(), "fiesta")
        self.luz.configurar_modo("lectura")
        self.assertEqual(self.luz.get_modo(), "fiesta")

    def test_configurar_intensidad_valida(self):
        self.luz.configurar_intensidad(3)
        self.assertEqual(self.luz.get_intensidad(), 3)

    def test_configurar_intensidad_invalida(self):
        self.assertEqual(self.luz.get_intensidad(), 1)
        self.luz.configurar_intensidad(5)
        self.assertEqual(self.luz.get_intensidad(), 1)


if __name__ == "__main__":
    unittest.main()
