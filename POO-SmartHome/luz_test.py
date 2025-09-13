import unittest
import uuid
from luz import Luz

class TestLuz(unittest.TestCase):

    def setUp(self):
        self.luz = Luz(id_vivienda=uuid.uuid4())

    def test_estado_inicial(self):
        self.assertEqual(self.luz.modo, "apagado")
        self.assertEqual(self.luz.intensidad, 1)

    def test_set_modo_valido(self):
        self.luz.setModo("encendido")
        self.assertEqual(self.luz.modo, "encendido")

    def test_set_modo_invalido(self):
        with self.assertRaises(ValueError):
            self.luz.setModo("intermitente")

    def test_set_intensidad_valida(self):
        for i in (1, 2, 3):
            self.luz.setIntensidad(i)
            self.assertEqual(self.luz.intensidad, i)

    def test_set_intensidad_invalida(self):
        with self.assertRaises(ValueError):
            self.luz.setIntensidad(5)

        with self.assertRaises(ValueError):
            self.luz.setIntensidad(0)

if __name__ == '__main__':
    unittest.main()