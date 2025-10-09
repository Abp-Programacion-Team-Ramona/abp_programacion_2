import unittest
import uuid
from luz import Luz

def nueva_luz(modo=None, intensidad=None, estado=False):
    return Luz(
        id=uuid.uuid4(),
        nombre_dispositivo="Luz prueba",
        tipo_dispositivo="luz",
        estado=estado,
        id_vivienda=uuid.uuid4(),
        modo=modo,
        intensidad=intensidad,
    )

class TestLuz(unittest.TestCase):
    def test_valores_por_defecto(self):
        luz = nueva_luz()
        self.assertEqual(luz.get_modo(), "normal")
        self.assertEqual(luz.get_intensidad(), 1)

    def test_init_asigna_directo_sin_validacion(self):
        luz = nueva_luz(modo="cualquiera", intensidad=99)
        self.assertEqual(luz.get_modo(), "cualquiera")
        self.assertEqual(luz.get_intensidad(), 99)

    def test_configurar_modo_valido(self):
        luz = nueva_luz()
        luz.configurar_modo("fiesta")
        self.assertEqual(luz.get_modo(), "fiesta")

    def test_configurar_modo_normaliza_minusculas(self):
        luz = nueva_luz()
        luz.configurar_modo("NoCturNa")
        self.assertEqual(luz.get_modo(), "nocturna")

    def test_configurar_modo_invalido_no_cambia(self):
        luz = nueva_luz()
        self.assertEqual(luz.get_modo(), "normal")
        luz.configurar_modo("lectura")
        self.assertEqual(luz.get_modo(), "normal")

    def test_configurar_intensidad_valida(self):
        luz = nueva_luz()
        luz.configurar_intensidad(3)
        self.assertEqual(luz.get_intensidad(), 3)

    def test_configurar_intensidad_invalida_no_cambia(self):
        luz = nueva_luz()
        self.assertEqual(luz.get_intensidad(), 1)
        luz.configurar_intensidad(7)
        self.assertEqual(luz.get_intensidad(), 1)

if __name__ == "__main__":
    unittest.main(verbosity=2, exit=False)
