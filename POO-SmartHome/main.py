from dao.usuario_dao import UsuarioDAO
from conn.db_conn import DatabaseConnection
from dominio.usuario import Usuario
from dao.dispositivo_dao import DispositivoDAO
from dominio.aireAcondicionado import AireAcondicionado
from dominio.ventilador import Ventilador
from dominio.luz import Luz
from dao.rutina_dao import RutinaDAO
from dominio.rutina import Rutina
import uuid


def main():
    conexion = DatabaseConnection.connect_to_mysql
    if not conexion:
        print("fallo de conexion a db")
        return

    registrar_admin()

    while True:
        print("Elija una opcion")
        print("1: Registrar usuario")
        print("2: Login")
        print("3: Salir")
        opcion = int(input)
        if opcion < 1 or opcion > 3:
            print("Elija una opcion valida")
        if opcion == 1:
            registrar_usuario_estandar()
        if opcion == 2:
            user = iniciar_sesion()
            if user:
                activar_menu(user)
        if opcion == 3:
            return False


def activar_menu(user: Usuario):
    print(f"Bienvenido {user.nombre}")
    if user.rol == "usuario":
        while True:
            print("Elija una opcion")
            print("1. Consultar datos personales")
            print("2. Consultar dispositivos")
            print("3. Salir")
            opcion = int(input())
            if opcion < 1 or opcion > 3:
                print("Elija una opcion valida")
            if opcion == 1:
                user.mostrar_datos()
            if opcion == 2:
                DispositivoDAO.get_dispositivos_x_usuario(user.id)
            if opcion == 3:
                return False
    if user.rol == "admin":
        while True:
            print("Elija una opcion")
            print("1. Cambiar rol de un usuario")
            print("2. Registrar dispositivo")
            print("3. Actualizar dispositivo")
            print("4. Eliminar dispositivo")
            print("5. Buscar dispositivo")
            print("6. Automatizar dispositivo")
            print("7. Salir")
            opcion = int(input())
            if opcion < 1 or opcion > 7:
                print("Elija una opcion valida")
            if opcion == 1:
                cambiar_rol_usuario()
            if opcion == 2:
                registrar_dispositivo()
            if opcion == 3:
                id = uuid.UUID(input("Ingrese el id del dispositivo"))
                nombre = input("Indique el nuevo nombre del dispositivo")
                tipo = input(
                    "Indique que tipo de dispositivo es: 1) Aire Acondicionado. 2) Ventilador. 3) Luz"
                )
                if tipo == 1:
                    temperatura = int(input("Ingrese la nueva temperatura:"))
                    if temperatura < 16 or temperatura > 30:
                        print("Valores invalidos")
                        return
                    velocidad = int(input("Ingresa la nueva velocidad:"))
                    if velocidad < 1 or velocidad > 3:
                        print("Valores invalidos")
                        return
                    modo = int(input("Ingresa el nuevo modo"))
                    if modo not in ("frio", "calor", "auto", "ventilador"):
                        print("Valores invalidos")
                        return

                    nuevo = AireAcondicionado(
                        temperatura,
                        velocidad,
                        modo,
                        id,
                        None,
                        nombre,
                        "aire_acondicionado",
                        True,
                    )
                    DispositivoDAO.update_dispositivo(nuevo)
                if tipo == 2:
                    velocidad = int(input("Ingrese velocidad:"))
                    giro_input = input("Activar giro: si | no")
                    giro = False
                    if str.lower(giro_input) == "si":
                        giro = True
                    nuevo = Ventilador(
                        velocidad, giro, id, None, nombre, "ventilador", True
                    )
                    DispositivoDAO.update_dispositivo(nuevo)
                if tipo == 3:
                    modo = str.lower(
                        input(
                            "Ingrese el nuevo modo: normal | fiesta | diurna | nocturna"
                        )
                    )
                    intensidad = int(input("Ingrese intensidad: 1 2 3"))
                    nuevo = Luz(modo, intensidad, id, None, nombre, "luz", True)
                    DispositivoDAO.update_dispositivo(nuevo)
            if opcion == 4:
                id = input("Ingrese el id del dispositivo a eliminar")
                DispositivoDAO.delete_dispositivo(id)
            if opcion == 5:
                id = input("Ingrese el id del dispositivo")
                tipo_input = int(input("Seleccione el tipo de dispositivo"))
                tipo = ""
                print("1. Aire Acondicionado")
                print("2. Luz")
                print("3. Ventilador")
                if tipo_input == 1:
                    tipo = "aire_acondicionado"
                if tipo_input == 2:
                    tipo = "luz"
                if tipo_input == 3:
                    tipo = "ventilador"
                print(f"Dispositivo:{DispositivoDAO.get_dispositivo(id, tipo)}")
            if opcion == 6:
                id_dispositivo = input("Ingrese el id del dispositivo a automatizar")
                horario_inicio = input(
                    "Ingrese la hora del inicio de la rutina formato 00:00 "
                )
                descripcion = input("Ingrese la descripcion de la rutina:")
                horario_apagado = input(
                    "Ingrese el horario de apagado del dispositivo si corresponde"
                )
                horario_encendido = input(
                    "Ingrese el horario de encendido si corresponde"
                )
                rutina = Rutina(
                    uuid.uuid4,
                    id_dispositivo,
                    descripcion,
                    horario_inicio,
                    horario_apagado,
                    horario_encendido,
                    True,
                )
                RutinaDAO.create_rutina(rutina)

            if opcion == 7:
                return False


def registrar_dispositivo():
    print("Registrando dispositivo:")
    vivienda = input("Indique el identificador de la vivienda")
    nombre = input("Indique el nombre del dispositivo")
    tipo = input(
        "Indique que tipo de dispositivo es: 1) Aire Acondicionado. 2) Ventilador. 3) Luz"
    )
    if tipo < 1 or tipo > 3:
        print("Elija un tipo valido")
    elif tipo == "1":
        registrar_aire_acondicionado(vivienda, nombre)
    elif tipo == "2":
        registrar_ventilador(nombre, vivienda)
    elif tipo == "3":
        registrar_luz(nombre, vivienda)


def cambiar_rol_usuario():
    user = input("Indique el mail del usuario:")
    rol = input("Indique el rol: usuario | admin")
    UsuarioDAO.update_usuario_rol(user, str.lower(rol))


def registrar_aire_acondicionado(vivienda, nombre):
    asignando_temperatura = True
    while asignando_temperatura:
        temperatura = input("Ingrese la temperatura: ")
        if temperatura < 16 or temperatura > 30:
            print("La temperatura debe estar entre 16 y 30 grados")
        else:
            asignando_temperatura = False

    asignando_velocidad = True
    while asignando_velocidad:
        velocidad = input("Ingrese la velocidad entre 1 y 3")
        if velocidad < 1 or velocidad > 3:
            print("La velocidad debe estar entre 1 y 3")
        else:
            asignando_velocidad = False

    asignando_modo = True
    while asignando_modo:
        modo = input("Ingrese el modo: frio, calor, auto, ventilador")
        if str.lower(modo) not in (
            "frio",
            "calor",
            "auto",
            "ventilador",
        ):
            print("Ingrese un modo valido")
        else:
            asignando_modo = False

    dispositivo = AireAcondicionado(
        temperatura,
        velocidad,
        modo,
        uuid.uuid4,
        uuid.UUID(vivienda),
        nombre,
        "aire_acondicionado",
        True,
    )
    DispositivoDAO.create_dispositivo(dispositivo)


def registrar_luz(nombre, vivienda):
    asignando_modo = True
    while asignando_modo:
        modo = input("Ingrese el modo: normal, fiesta, diurna, nocturna")
        if str.lower(modo) not in (
            "normal",
            "fiesta",
            "diurna",
            "nocturna",
        ):
            print("Ingrese un modo valido")
        else:
            asignando_modo = False
    asignando_intensidad = True
    while asignando_intensidad:
        intensidad = input("Ingrese la velocidad entre 1 y 3")
        if intensidad < 1 or intensidad > 3:
            print("La intensidad debe estar entre 1 y 3")
        else:
            asignando_intensidad = False

    dispositivo = Luz(
        modo, intensidad, uuid.uuid4, uuid.UUID(vivienda), nombre, "luz", True
    )
    DispositivoDAO.create_dispositivo(dispositivo)


def registrar_ventilador(nombre, vivienda):
    asignando_velocidad = True
    while asignando_velocidad:
        velocidad = input("Ingrese la velocidad entre 1 y 3")
        if velocidad < 1 or velocidad > 3:
            print("La velocidad debe estar entre 1 y 3")
        else:
            asignando_velocidad = False
    dispositivo = Ventilador(
        velocidad, True, uuid.uuid4, uuid.UUID(vivienda), nombre, "ventilador", True
    )
    DispositivoDAO.create_dispositivo(dispositivo)


def iniciar_sesion(user, password) -> Usuario:
    user = UsuarioDAO.get_usuario(user, password)
    if user is None:
        print("No se encontro ningun usuario con esas credenciales")
        return None
    return user


def registrar_admin():
    nombre = "admin"
    contrasena = "admin123"
    correo = "correo@admin.com"

    admin = Usuario(uuid.uuid4, correo, nombre, contrasena, "admin")

    UsuarioDAO.create_usuario(admin)


def registrar_usuario_estandar():
    print("=== Registro de nuevo usuario ===")

    correo = input("Ingrese el correo electrónico: ").strip()
    nombre = input("Ingrese el nombre del usuario: ").strip()
    contrasena = input("Ingrese la contraseña: ").strip()

    if not correo or "@" not in correo:
        print(" Correo inválido.")
        return
    if not nombre:
        print(" El nombre no puede estar vacío.")
        return
    if len(contrasena) < 4:
        print(" La contraseña debe tener al menos 4 caracteres.")
        return

    user = Usuario(uuid.uuid4, correo, nombre, contrasena, "usuario")

    UsuarioDAO.create_usuario(user)

    print("\n Usuario registrado con éxito:")
