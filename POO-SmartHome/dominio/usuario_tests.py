import unittest
import uuid
from usuario import Usuario
from usuario_error import UsuarioError


class TestUsuario(unittest.TestCase):

    def setUp(self):
        self.usuario = Usuario(correo="test@mail.com", nombre="Diego", contraseña="123456")

    def test_constructor_asigna_valores(self):
        self.assertEqual(self.usuario.correo, "test@mail.com")
        self.assertEqual(self.usuario.nombre, "Diego")
        self.assertEqual(self.usuario.rol, "usuario")
        self.assertTrue(isinstance(self.usuario.id, uuid.UUID))


    def test_contraseña_valida(self):
        self.usuario.set_contraseña("abcdef")

    def test_contraseña_invalida(self):
        with self.assertRaises(UsuarioError):
            self.usuario.set_contraseña("123")

    def test_set_rol_valido(self):
        self.usuario.set_rol("admin")
        self.assertEqual(self.usuario.rol, "admin")

    def test_set_rol_invalido(self):
        with self.assertRaises(UsuarioError):
            self.usuario.set_rol("superuser")

    def test_agregar_vivienda_valida(self):
        vivienda_id = uuid.uuid4()
        self.usuario.agregar_vivienda(vivienda_id)
        self.assertIn(vivienda_id, self.usuario.viviendas)

    def test_agregar_vivienda_duplicada(self):
        vivienda_id = uuid.uuid4()
        self.usuario.agregar_vivienda(vivienda_id)
        with self.assertRaises(UsuarioError):
            self.usuario.agregar_vivienda(vivienda_id)

    def test_quitar_vivienda_valida(self):
        vivienda_id = uuid.uuid4()
        self.usuario.agregar_vivienda(vivienda_id)
        self.usuario.quitar_vivienda(vivienda_id)
        self.assertNotIn(vivienda_id, self.usuario.viviendas)

    def test_quitar_vivienda_inexistente(self):
        vivienda_id = uuid.uuid4()
        with self.assertRaises(UsuarioError):
            self.usuario.quitar_vivienda(vivienda_id)



if __name__ == "__main__":
    unittest.main()
