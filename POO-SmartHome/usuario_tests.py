from usuario import Usuario
from usuario_error import UsuarioError
import unittest


class TestUsuario(unittest.TestCase):

    def setUp(self):
        self.usuario = Usuario("juan@mail.com", "Juan", "123456", "usuario")
        self.vivienda = "Casa Falsa 123"  

    def test_agregar_vivienda(self):
        self.usuario.agregar_vivienda(self.vivienda)
        self.assertIn(self.vivienda, self.usuario.viviendas)

    def test_quitar_vivienda(self):
        self.usuario.agregar_vivienda(self.vivienda)
        self.usuario.quitar_vivienda(self.vivienda)
        self.assertNotIn(self.vivienda, self.usuario.viviendas)

    def test_rol_invalido(self):
        with self.assertRaises(UsuarioError):
            Usuario("maria@mail.com", "María", "abcdef", "invalido")

    def test_contraseña_corta(self):
        with self.assertRaises(UsuarioError):
            Usuario("ana@mail.com", "Ana", "123", "usuario")
