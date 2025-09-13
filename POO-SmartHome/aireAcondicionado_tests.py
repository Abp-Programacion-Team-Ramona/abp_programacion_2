import unittest
import uuid
from aireAcondicionado import AireAcondicionado

class TestAireAcondicionadoBasico(unittest.TestCase):
    def setUp(self):
        self.aire = AireAcondicionado(id_vivienda=uuid.uuid4())

    def test_estado_inicial(self):
        self.assertEqual(self.aire.get_temperatura(), 24)
        self.assertEqual(self.aire.get_velocidad(), 1)
        self.assertEqual(self.aire.get_modo(), "frio")

    def test_set_temperatura_fuera_de_rango(self):
        with self.assertRaises(ValueError):
            self.aire.setTemperatura(15)
        with self.assertRaises(ValueError):
            self.aire.setTemperatura(31)

    def test_set_velocidad_invalida(self):
        for valor in [0, 4, -1]:
            with self.assertRaises(ValueError):
                self.aire.setVelocidad(valor)

    def test_set_modo_valido(self):
        self.aire.setModo("CALOR")
        self.assertEqual(self.aire.get_modo(), "calor")

    def test_set_modo_invalido(self):
        with self.assertRaises(ValueError):
            self.aire.setModo("turbo")

if __name__ == "__main__":
    unittest.main(verbosity=2)
