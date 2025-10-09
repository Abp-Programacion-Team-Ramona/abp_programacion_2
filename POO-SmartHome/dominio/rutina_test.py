import unittest
import uuid
from datetime import time
from rutina import Rutina


class TestRutina(unittest.TestCase):
    def setUp(self):
        self.rutina = Rutina(
            id=uuid.uuid4,
            id_dispositivo=uuid.uuid4,
            descripcion="Definicion",
            horario_inicio="00:00",
            horario_apagado="00:00",
            horario_encendido="00:00",
            estado_rutina=False,
        )

    def test_set_horario_inicio(self):
        nuevo = time(9, 30)
        self.rutina.horario_inicio = nuevo
        self.assertEqual(self.rutina.horario_inicio, nuevo)

    def test_set_horario_apagado(self):
        nuevo = time(22, 0)
        self.rutina.horario_apagado = nuevo
        self.assertEqual(self.rutina.horario_apagado, nuevo)

    def test_set_horario_encendido(self):
        nuevo = time(19, 0)
        self.rutina.horario_encendido = nuevo
        self.assertEqual(self.rutina.horario_encendido, nuevo)

    def test_cambiar_estado_activa(self):
        msg = self.rutina.cambiar_estado_rutina(True)
        self.assertTrue(self.rutina.estado_rutina)
        self.assertEqual(msg, "Rutina ahora activada.")

    def test_cambiar_estado_inactiva(self):
        self.rutina.estado_rutina = True
        msg = self.rutina.cambiar_estado_rutina(False)
        self.assertFalse(self.rutina.estado_rutina)
        self.assertEqual(msg, "La rutina ya está desactivada.")

    def test_cambiar_estado_redundante_activa(self):
        self.rutina.estado_rutina = True
        msg = self.rutina.cambiar_estado_rutina(True)
        self.assertTrue(self.rutina.estado_rutina)
        self.assertEqual(msg, "Rutina ahora activada.")

    def test_cambiar_estado_redundante_inactiva(self):
        self.rutina.estado_rutina = False
        msg = self.rutina.cambiar_estado_rutina(False)
        self.assertFalse(self.rutina.estado_rutina)
        self.assertEqual(msg, "La rutina ya está desactivada.")


if __name__ == "__main__":
    unittest.main()
