

CREATE TABLE usuarios (
    id CHAR(36) PRIMARY KEY,
    correo VARCHAR(100) NOT NULL,
    nombre VARCHAR(100) NOT NULL,
    contraseña VARCHAR(100) NOT NULL,
    rol VARCHAR(50) NOT NULL
);

CREATE TABLE viviendas (
    id CHAR(36) PRIMARY KEY,
    id_usuario CHAR(36) NOT NULL,
    nombre VARCHAR(100) NOT NULL,
    calle VARCHAR(100) NOT NULL,
    altura VARCHAR(20) NOT NULL,
    piso VARCHAR(20),
    nota VARCHAR(255),
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id) ON DELETE CASCADE
);

CREATE TABLE rutinas (
    id CHAR(36) PRIMARY KEY,
    id_dispositivo CHAR(36) UNIQUE NOT NULL,
    horario_inicio DATETIME NOT NULL,
    horario_apagado DATETIME NOT NULL,
    horario_encendido DATETIME NOT NULL,
    estado_rutina BOOLEAN NOT NULL,
    FOREIGN KEY (id_dispositivo) REFERENCES dispositivos(id) ON DELETE CASCADE
);

CREATE TABLE historiales (
    id CHAR(36) PRIMARY KEY,
    id_dispositivo CHAR(36) NOT NULL,
    fecha DATETIME NOT NULL,
    descripcion VARCHAR(255) NOT NULL,
    FOREIGN KEY (id_dispositivo) REFERENCES dispositivos(id) ON DELETE CASCADE
);


CREATE TABLE dispositivos (
    id CHAR(36) PRIMARY KEY,
    id_vivienda CHAR(36) NOT NULL,
    nombre_dispositivo VARCHAR(50) NOT NULL,
    tipo_dispositivo VARCHAR(50) NOT NULL,
    estado BOOLEAN NOT NULL,
    FOREIGN KEY (id_vivienda) REFERENCES viviendas(id) ON DELETE CASCADE
);

CREATE TABLE aires_acondicionados (
    id CHAR(36) PRIMARY KEY,
    temperatura INT,
    velocidad INT,
    modo VARCHAR(50),
    FOREIGN KEY (id) REFERENCES dispositivos(id)
);

CREATE TABLE luces (
    id CHAR(36) PRIMARY KEY,
    modo VARCHAR(50),
    intensidad INT,
    FOREIGN KEY (id) REFERENCES dispositivos(id)
);

CREATE TABLE ventiladores (
    id CHAR(36) PRIMARY KEY,
    velocidad int,
    giro bool,
    FOREIGN KEY (id) REFERENCES dispositivos(id)
);