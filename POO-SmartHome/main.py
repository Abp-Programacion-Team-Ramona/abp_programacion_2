from dao.usuario_dao import UsuarioDAO
from conn.db_conn import DatabaseConnection
from dominio.usuario import Usuario
from dao.dispositivo_dao import DispositivoDAO
from dominio.aire_acondicionado import AireAcondicionado
from dominio.ventilador import Ventilador
from dominio.luz import Luz
from dao.rutina_dao import RutinaDAO
from dominio.rutina import Rutina
from dominio.vivienda import Vivienda
from dao.vivienda_dao import ViviendaDAO
import uuid


def main():
    conexion = DatabaseConnection.connect_to_mysql()
    if not conexion:
        print("fallo de conexion a db")
        return

    usuarioDAO = UsuarioDAO(DatabaseConnection)
    registrar_admin(usuarioDAO)
    viviendaDAO = ViviendaDAO(DatabaseConnection)
    dispositivoDAO = DispositivoDAO(DatabaseConnection)
    rutinaDAO = RutinaDAO(DatabaseConnection)

    while True:
        print("Elija una opcion")
        print("1: Registrar usuario")
        print("2: Login")
        print("3: Salir")
        opcion = int(input())
        if opcion < 1 or opcion > 3:
            print("Elija una opcion valida")
        if opcion == 1:
            registrar_usuario_estandar(usuarioDAO, viviendaDAO)
        if opcion == 2:
            user = iniciar_sesion(usuarioDAO)
            if user:
                activar_menu(user, dispositivoDAO, usuarioDAO, rutinaDAO)
        if opcion == 3:
            return False


def activar_menu(user: Usuario, dispositivoDAO: DispositivoDAO, usuarioDAO: UsuarioDAO, rutinaDAO: RutinaDAO):
    print(f"Bienvenido {user.nombre}")
    print("Elija una opcion: ")

    if user.rol == "usuario":
        while True:
            print("1. Consultar datos personales")
            print("2. Consultar dispositivos")
            print("3. Salir")
            opcion = int(input())
            if opcion < 1 or opcion > 3:
                print("Elija una opcion valida")
            if opcion == 1:
                user.mostrar_datos()
            if opcion == 2:
                consultar_datos(dispositivoDAO, user)
            if opcion == 3:
                return False
    if user.rol == "admin":
        while True:
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
                cambiar_rol_usuario(usuarioDAO)
            if opcion == 2:
                registrar_dispositivo(dispositivoDAO)
            if opcion == 3:
                id = uuid.UUID(input("Ingrese el id del dispositivo: "))
                nombre = input("Indique el nuevo nombre del dispositivo: ")
                tipo = int(input(
                    "Indique que tipo de dispositivo es: 1) Aire Acondicionado. 2) Ventilador. 3) Luz: "
                ))
                if tipo == 1:
                    temperatura = int(input("Ingrese la nueva temperatura: "))
                    if temperatura < 16 or temperatura > 30:
                        print("Valores invalidos")
                        return
                    velocidad = int(input("Ingresa la nueva velocidad: "))
                    if velocidad < 1 or velocidad > 3:
                        print("Valores invalidos")
                        return
                    modo = input("Ingresa el nuevo modo: ")
                    if modo not in ("frio", "calor", "auto", "ventilador"):
                        print("Valores invalidos")
                        return

                    nuevo = AireAcondicionado(
                        temperatura=temperatura,
                        velocidad=velocidad,
                        modo=modo,
                        id=id,
                        id_vivienda=None,
                        nombre_dispositivo=nombre,
                        tipo_dispositivo="aire_acondicionado",
                        estado=True,
                    )
                    dispositivoDAO.update(dispositivo=nuevo)
                if tipo == 2:
                    velocidad = int(input("Ingrese velocidad:"))
                    giro_input = input("Activar giro: si | no")
                    giro = False
                    if str.lower(giro_input) == "si":
                        giro = True
                    nuevo = Ventilador(
                        velocidad=velocidad,
                        giro=giro,
                        id=id,
                        id_vivienda=None,
                        nombre_dispositivo=nombre,
                        tipo_dispositivo="ventilador",
                        estado=True
                    )
                    dispositivoDAO.update(nuevo)
                if tipo == 3:
                    modo = str.lower(
                        input(
                            "Ingrese el nuevo modo: normal | fiesta | diurna | nocturna"
                        )
                    )
                    intensidad = int(input("Ingrese intensidad: 1 2 3"))
                    nuevo = Luz(
                        modo,
                        intensidad,
                        id=id,
                        id_vivienda=None,
                        nombre_dispositivo=nombre,
                        tipo_dispositivo="luz",
                        estado=True)
                    dispositivoDAO.update(nuevo)
            if opcion == 4:
                id = input("Ingrese el id del dispositivo a eliminar: ")
                dispositivoDAO.delete(id)
            if opcion == 5:
                id = input("Ingrese el id del dispositivo: ")
                print("Seleccione el tipo de dispositivo: ")
                tipo = ""
                print("1. Aire Acondicionado")
                print("2. Luz")
                print("3. Ventilador")
                tipo_input = int(input())
                if tipo_input == 1:
                    tipo = "aires_acondicionados"
                    cls=AireAcondicionado
                if tipo_input == 2:
                    tipo = "luces"
                    cls = Luz
                if tipo_input == 3:
                    tipo = "ventiladores"
                    cls = Ventilador

                dispositivo=dispositivoDAO.get(id,tipo,cls)
                print(f"Dispositivo:{dispositivo.nombre_dispositivo}, Tipo:{dispositivo.tipo_dispositivo}")
            if opcion == 6:
                id_dispositivo = input("Ingrese el id del dispositivo a automatizar: ")
                horario_inicio = input(
                    "Ingrese la hora del inicio de la rutina formato 00:00: "
                )
                descripcion = input("Ingrese la descripcion de la rutina: ")
                horario_apagado = input(
                    "Ingrese el horario de apagado del dispositivo si corresponde: "
                )
                horario_encendido = input(
                    "Ingrese el horario de encendido si corresponde: "
                )
                rutina = Rutina(
                    uuid.uuid4(),
                    id_dispositivo,
                    descripcion,
                    horario_inicio,
                    horario_apagado,
                    horario_encendido,
                    True,
                )
                rutinaDAO.create(rutina)
            if opcion == 7:
                return False


def consultar_datos(dispositivoDAO, user):
    dispositivos = dispositivoDAO.get_dispositivos_x_usuario(user.id)
    print(f"Nombre de usuario: {user.nombre}")
    print(f"Rol de usuario: {user.rol}")
    print("Dispositivos:")
    for d in dispositivos:
        print(
            f"ID: {d['id']}, "
            f"Nombre: {d['nombre_dispositivo']}, "
            f"Tipo: {d['tipo_dispositivo']}, "
            f"Estado: {d['estado']}")


def registrar_dispositivo(dispositivoDAO: DispositivoDAO):
    print("Registrando dispositivo: ")
    # vivienda = input("Indique el identificador de la vivienda: ")
    vivienda = uuid.UUID("29f4f66b-f34d-4afd-b16a-b11e65ef4914")
    nombre = input("Indique el nombre del dispositivo: ")
    tipo = input(
        "Indique que tipo de dispositivo es: 1) Aire Acondicionado. 2) Ventilador. 3) Luz: "
    )
    if int(tipo) < 1 or int(tipo) > 3:
        print("Elija un tipo valido")
    if tipo == "1":
        registrar_aire_acondicionado(dispositivoDAO, vivienda, nombre)
        return
    if tipo == "2":
        registrar_ventilador(dispositivoDAO, nombre, vivienda)
        return
    if tipo == "3":
        registrar_luz(dispositivoDAO, nombre, vivienda)
        return


def cambiar_rol_usuario(usuarioDAO: UsuarioDAO):
    correo = input("Indique el mail del usuario:")
    rol = input("Indique el rol: usuario | admin :")
    usuarioDAO.update_usuario_rol(correo=correo, rol=str.lower(rol))


def registrar_aire_acondicionado(dispositivoDAO, vivienda, nombre):
    asignando_temperatura = True
    while asignando_temperatura:
        temperatura = int(input("Ingrese la temperatura: "))
        if temperatura < 16 or temperatura > 30:
            print("La temperatura debe estar entre 16 y 30 grados")
        else:
            asignando_temperatura = False

    asignando_velocidad = True
    while asignando_velocidad:
        velocidad = int(input("Ingrese la velocidad entre 1 y 3: "))
        if velocidad < 1 or velocidad > 3 or velocidad is None:
            print("La velocidad debe estar entre 1 y 3")
        else:
            asignando_velocidad = False

    asignando_modo = True
    while asignando_modo:
        modo = input("Ingrese el modo: frio, calor, auto, ventilador: ")
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
        temperatura=temperatura,
        velocidad=velocidad,
        modo=modo,
        id=uuid.uuid4(),
        id_vivienda=vivienda,
        nombre_dispositivo=nombre,
        tipo_dispositivo="aire_acondicionado",
        estado=True,
    )
    dispositivoDAO.create(dispositivo)


def registrar_luz(dispositivoDAO, nombre, vivienda):
    asignando_modo = True
    while asignando_modo:
        modo = input("Ingrese el modo: normal, fiesta, diurna, nocturna: ")
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
        intensidad = int(input("Ingrese la velocidad entre 1 y 3: "))
        if intensidad < 1 or intensidad > 3 or intensidad is None:
            print("La intensidad debe estar entre 1 y 3")
        else:
            asignando_intensidad = False

    dispositivo = Luz(
        modo=modo,
        intensidad=intensidad,
        id=uuid.uuid4(),
        id_vivienda=vivienda,
        nombre_dispositivo=nombre,
        tipo_dispositivo="luz", estado=True
    )
    dispositivoDAO.create(dispositivo)


def registrar_ventilador(dispositivoDAO, nombre, vivienda):
    asignando_velocidad = True
    while asignando_velocidad:
        velocidad = int(input("Ingrese la velocidad entre 1 y 3: "))
        if velocidad < 1 or velocidad > 3:
            print("La velocidad debe estar entre 1 y 3")
        else:
            asignando_velocidad = False
            dispositivo = Ventilador(
                velocidad=velocidad,
                giro=True,
                id=uuid.uuid4(),
                id_vivienda=vivienda,
                nombre_dispositivo=nombre,
                tipo_dispositivo="ventilador",
                estado=True)
            dispositivoDAO.create(dispositivo)


def iniciar_sesion(usuarioDAO: UsuarioDAO) -> Usuario:
    user = input("Ingrese nombre de usuario: ")
    passw = input("Ingrese contraseña: ")
    user = usuarioDAO.get(user, passw)
    if user is None:
        print("No se encontro ningun usuario con esas credenciales")
        return None
    return user


def registrar_admin(usuarioDAO: UsuarioDAO):
    nombre = "admin"
    contrasena = "admin123"
    correo = "correo@admin.com"

    admin = Usuario(uuid.uuid4(), correo, nombre, contrasena, "admin")
    if usuarioDAO.get(user="admin", contrasena="admin123") is None:
        usuarioDAO.create(usuario=admin)


def registrar_usuario_estandar(usuarioDAO: UsuarioDAO, viviendaDAO: ViviendaDAO):
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

    id_usuario = uuid.uuid4()

    user = Usuario(id_usuario, correo, nombre, contrasena, "usuario")

    usuarioDAO.create(user)

    print("Iniciando registro de vivienda")

    nombre_vivienda = input("Indique el nombre de la vivienda: ")
    calle = input("Indique la direccion sin altura: ")
    altura = input("Indique la altura, si no tiene deje el campo vacio: ")
    piso = input("Indique el piso si corresponde si no tiene deje el campo vacio: ")
    nota = input("Agregue alguna nota si lo requiere: ")

    vivienda = Vivienda(uuid.uuid4(), nombre_vivienda, id_usuario, calle, altura, piso, nota)

    viviendaDAO.create(vivienda)

    print("\n Usuario registrado con éxito:")


if __name__ == '__main__':
    main()
