import unittest
import uuid
from aireAcondicionado import AireAcondicionado
from unittest.mock import patch


class TestAireAcondicionado(unittest.TestCase):
    def setUp(self):
        self.aire = AireAcondicionado(
            temperatura=17,
            velocidad=1,
            modo="frio",
            id=uuid.uuid4(),
            id_vivienda=uuid.uuid4(),
            nombre_dispositivo="Aire living",
            tipo_dispositivo="aire acondicionado",
            estado=False,
        )

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

    @patch("builtins.input", side_effect=[22])
    def test_set_temperatura_valida(self, mock_input):
        self.aire.cambiar_temperatura()
        self.assertEqual(self.aire.get_temperatura(), 22)

    @patch("builtins.input", side_effect=[5, 23])
    @patch("builtins.print")
    def test_set_temperatura_invalida(self, mock_print, mock_input):
        self.aire.cambiar_temperatura()
        self.assertEqual(self.aire._temperatura, 23)
        self.assertGreaterEqual(mock_input.call_count, 2)
        mock_print.assert_any_call("La temperatura debe estar entre 16 y 30 grados")

    @patch("builtins.input", side_effect=[3])
    def test_set_velocidad_valida(self, mock_input):
        self.aire.cambiar_velocidad()
        self.assertEqual(self.aire.get_velocidad(), 3)

    @patch("builtins.input", side_effect=[4, 2])
    @patch("builtins.print")
    def test_set_velocidad_invalida(self, mock_print, mock_input):
        self.aire.cambiar_velocidad()
        self.assertEqual(self.aire.get_velocidad(), 2)
        self.assertGreaterEqual(mock_input.call_count, 2)
        mock_print.assert_any_call(
            "La velocidad debe ser 1 (baja), 2 (media) o 3 (alta)"
        )

    @patch("builtins.input", side_effect=["calor"])
    def test_set_modo_valido(self, mock_input):
        self.aire.cambiar_modo()
        self.assertEqual(self.aire.get_modo(), "calor")

    @patch("builtins.input", side_effect=["helado", "auto"])
    @patch("builtins.print")
    def test_set_modo_invalido(self, mock_print, mock_input):
        self.aire.cambiar_modo()
        self.assertEqual(self.aire._modo, "auto")
        self.assertGreaterEqual(mock_input.call_count, 2)
        mock_print.assert_any_call("El modo: helado es invalido")


if __name__ == "__main__":
    unittest.main()
