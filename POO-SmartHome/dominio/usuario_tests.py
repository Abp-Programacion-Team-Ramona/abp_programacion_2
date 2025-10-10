import unittest
import uuid
from unittest.mock import patch
from usuario import Usuario


class TestUsuario(unittest.TestCase):

    def setUp(self):
        self.usuario_id = uuid.uuid4()
        self.usuario = Usuario(id=self.usuario_id, correo="test@mail.com", nombre="Diego", contraseña="123456", rol="usuario")

    def test_constructor_asigna_valores(self):
        self.assertEqual(self.usuario.id, self.usuario_id)
        self.assertEqual(self.usuario.correo, "test@mail.com")
        self.assertEqual(self.usuario.nombre, "Diego")
        self.assertEqual(self.usuario.rol, "usuario")
        self.assertTrue(isinstance(self.usuario.id, uuid.UUID))

    def test_id_unico(self):
        usuario2_id = uuid.uuid4()
        usuario2 = Usuario(usuario2_id, "otro@mail.com", "Maria", "pass456", "admin")
        self.assertNotEqual(self.usuario.id, usuario2.id)

    @patch('builtins.input', return_value='contraseña_valida_123')
    @patch('builtins.print')
    def test_cambiar_contraseña_valida(self, mock_print, mock_input):
        self.usuario.cambiar_contraseña()
        mock_input.assert_called_once()

    @patch('builtins.input', side_effect=['123', '12345', 'contraseña_valida'])
    @patch('builtins.print')
    def test_cambiar_contraseña_invalida_luego_valida(self, mock_print, mock_input):
        self.usuario.cambiar_contraseña()
        self.assertEqual(mock_input.call_count, 3)

    @patch('builtins.input', return_value='admin')
    @patch('builtins.print')
    def test_cambiar_rol_valido(self, mock_print, mock_input):
        self.usuario.cambiar_rol()
        self.assertEqual(self.usuario.rol, "admin")

    @patch('builtins.input', side_effect=['superuser', 'root', 'admin'])
    @patch('builtins.print')
    def test_cambiar_rol_invalido_luego_valido(self, mock_print, mock_input):
        self.usuario.cambiar_rol()
        self.assertEqual(self.usuario.rol, "admin")
        self.assertEqual(mock_input.call_count, 3)

    @patch('builtins.input', return_value='nuevo@mail.com')
    @patch('builtins.print')
    def test_cambiar_correo_valido(self, mock_print, mock_input):
        """Test que verifica el cambio de correo con formato válido"""
        self.usuario.cambiar_correo()
        self.assertEqual(self.usuario.correo, "nuevo@mail.com")

    @patch('builtins.input', side_effect=['correo_invalido', 'sin_punto@', 'valido@mail.com'])
    @patch('builtins.print')
    def test_cambiar_correo_invalido_luego_valido(self, mock_print, mock_input):
        self.usuario.cambiar_correo()
        self.assertEqual(self.usuario.correo, "valido@mail.com")
        self.assertEqual(mock_input.call_count, 3)

    @patch('builtins.input', return_value='Carlos')
    @patch('builtins.print')
    def test_cambiar_nombre_valido(self, mock_print, mock_input):
        self.usuario.cambiar_nombre()
        self.assertEqual(self.usuario.nombre, "Carlos")

    @patch('builtins.input', side_effect=['', '   ', 'Carlos'])
    @patch('builtins.print')
    def test_cambiar_nombre_vacio_luego_valido(self, mock_print, mock_input):
        self.usuario.cambiar_nombre()
        self.assertEqual(self.usuario.nombre, "Carlos")
        self.assertEqual(mock_input.call_count, 3)

    def test_agregar_vivienda_valida(self):
        vivienda_id = uuid.uuid4()
        self.usuario.agregar_vivienda(vivienda_id)

    def test_agregar_vivienda_duplicada(self):
        vivienda_id = uuid.uuid4()
        self.usuario.agregar_vivienda(vivienda_id)
        with self.assertRaises(ValueError):
            self.usuario.agregar_vivienda(vivienda_id)

    def test_quitar_vivienda_valida(self):
        vivienda_id = uuid.uuid4()
        self.usuario.agregar_vivienda(vivienda_id)
        self.usuario.quitar_vivienda(vivienda_id)

    def test_quitar_vivienda_inexistente(self):
        vivienda_id = uuid.uuid4()
        with self.assertRaises(ValueError):
            self.usuario.quitar_vivienda(vivienda_id)

if __name__ == "__main__":
    unittest.main()