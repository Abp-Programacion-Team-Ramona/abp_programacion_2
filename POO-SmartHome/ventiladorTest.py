import unittest
import uuid
from ventilador import Ventilador


class ventiladorTest(unittest.TestCase):

    def setUp(self):
        self.ventilador = Ventilador(uuid.uuid4(), uuid.uuid4(), None)

    def test_ajustar_velocidad_valida(self):
        self.ventilador.ajustar_velocidad(2)
        self.assertEqual(self.ventilador.velocidad, 2, "La velocidad no se ajustó correctamente")

    def test_ajustar_velocidad_invalida(self):
        self.ventilador.ajustar_velocidad(5)
        self.assertEqual(self.ventilador.velocidad, 0,
                         "La velocidad debería mantenerse en 0 si se ingresa un valor inválido")

    def test_ajustar_giro_activado(self):
        self.ventilador.ajustar_giro(True)
        self.assertTrue(self.ventilador.giro, "El giro debería estar activado")

    def test_ajustar_giro_desactivado(self):
        self.ventilador.ajustar_giro(False)
        self.assertFalse(self.ventilador.giro, "El giro debería estar desactivado")

    def test_ajustar_giro_invalido(self):
        self.ventilador.ajustar_giro("invalid")
        self.assertFalse(self.ventilador.giro, "El giro no debería cambiar si se pasa un valor inválido")


if __name__ == "_main_":
    unittest.main()
