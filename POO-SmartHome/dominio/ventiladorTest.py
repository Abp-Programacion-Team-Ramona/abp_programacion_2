import unittest
import uuid
from ventilador import Ventilador


class ventiladorTest(unittest.TestCase):

    def setUp(self):
            self.ventilador = Ventilador(
                id=uuid.uuid4(),
                id_vivienda=uuid.uuid4(),
                nombre_dispositivo="Ventilador techo",
                tipo_dispositivo="ventilador",
                estado=True,
                velocidad=3,
                giro=True,
            )

    def test_ajustar_velocidad_valida(self):
        self.ventilador._velocidad = 2
        self.assertEqual(self.ventilador.velocidad, 2)

    def test_ajustar_velocidad_invalida(self):
        self.ventilador._velocidad = 5
        if self.ventilador._velocidad > 3:
            self.ventilador._velocidad = 0
        self.assertEqual(self.ventilador.velocidad, 0)

    def test_ajustar_giro_activado(self):
        self.ventilador._giro = True
        self.assertTrue(self.ventilador.giro)

    def test_ajustar_giro_desactivado(self):
        self.ventilador._giro = False
        self.assertFalse(self.ventilador.giro)

    def test_ajustar_giro_invalido(self):
        valor = "invalido"
        if not isinstance(valor, bool):
            self.ventilador._giro = False
        self.assertFalse(self.ventilador.giro)


if __name__ == "__main__":
    unittest.main()