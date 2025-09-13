import unittest
from vivienda import Vivienda

class viviendaTest(unittest.TestCase):

    def setUp(self):
        self.vivienda = Vivienda("Casa Central", "usuario1", "San Martín", "123")

    def test_no_agregar_dispositivo_duplicado(self):
        self.vivienda.agregar_dispositivo("ventilador")
        self.vivienda.agregar_dispositivo("ventilador")
        self.assertEqual(len(self.vivienda.dispositivos), 1)

    def test_quitar_dispositivo_existente(self):
        self.vivienda.agregar_dispositivo("luz")
        self.vivienda.quitar_dispositivo("luz")
        self.assertEqual(len(self.vivienda.dispositivos), 0)

    def test_quitar_dispositivo_inexistente(self):
        self.vivienda.agregar_dispositivo("camara")
        self.vivienda.quitar_dispositivo("ventilador")
        self.assertEqual(len(self.vivienda.dispositivos), 1)

if __name__ == "__main__":
    unittest.main()