def registrar_usuario_estandar():

    print("=== Registro de nuevo usuario ===")

    correo = input("Ingrese el correo electrónico: ").strip()
    nombre = input("Ingrese el nombre del usuario: ").strip()
    contrasena = input("Ingrese la contraseña: ").strip()
    rol = "usuario"

    if not correo or "@" not in correo:
        print(" Correo inválido.")
        return
    if not nombre:
        print(" El nombre no puede estar vacío.")
        return
    if len(contrasena) < 4:
        print(" La contraseña debe tener al menos 4 caracteres.")
        return

    nuevo_usuario = {
        "correo": correo,
        "nombre": nombre,
        "contrasena": contrasena,
        "rol": rol
    }

    print("\n Usuario registrado con éxito:")

def registrar_admin():

    print("=== Registro de administrador ===")

    nombre = "Ramona"
    contrasena = "Ramona321"

    if not correo or "@" not in correo:
        print(" Correo inválido.")
        return

    nuevo_admin = {
    
        "nombre": nombre,
        "contrasena": contrasena,
        "rol": "admin"
    }

    print("\n Usuario administrador registrado con éxito:")
    print(f" - Nombre: {nombre}")
    print(f" - Contraseña: {contrasena}")
