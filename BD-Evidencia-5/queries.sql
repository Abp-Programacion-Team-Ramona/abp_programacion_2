CREATE TABLE usuarios (
    id CHAR(36) PRIMARY KEY,
    correo VARCHAR(100) NOT NULL,
    nombre VARCHAR(100) NOT NULL,
    contrasena VARCHAR(100) NOT NULL,
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

CREATE TABLE dispositivos (
    id CHAR(36) PRIMARY KEY,
    id_vivienda CHAR(36) NOT NULL,
    nombre_dispositivo VARCHAR(50) NOT NULL,
    tipo_dispositivo VARCHAR(50) NOT NULL,
    estado BOOLEAN NOT NULL,
    FOREIGN KEY (id_vivienda) REFERENCES viviendas(id) ON DELETE CASCADE
);

CREATE TABLE rutinas (
    id CHAR(36) PRIMARY KEY,
    id_dispositivo CHAR(36) UNIQUE NOT NULL,
    descripcion VARCHAR (255) NOT NULL,
    horario_inicio CHAR(36) NOT NULL,
    horario_apagado CHAR(36) NOT NULL,
    horario_encendido CHAR(36) NOT NULL,
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

INSERT INTO usuarios (id, correo, nombre, contrasena, rol) VALUES
('11111111-1111-1111-1111-000000000001','ana@example.com','Ana','hash1','admin'),
('11111111-1111-1111-1111-000000000002','bruno@example.com','Bruno','hash2','user'),
('11111111-1111-1111-1111-000000000003','carla@example.com','Carla','hash3','user'),
('11111111-1111-1111-1111-000000000004','diego@example.com','Diego','hash4','user'),
('11111111-1111-1111-1111-000000000005','eva@example.com','Eva','hash5','user'),
('11111111-1111-1111-1111-000000000006','facu@example.com','Facundo','hash6','user'),
('11111111-1111-1111-1111-000000000007','gina@example.com','Gina','hash7','user'),
('11111111-1111-1111-1111-000000000008','hugo@example.com','Hugo','hash8','user'),
('11111111-1111-1111-1111-000000000009','ivan@example.com','Iván','hash9','user'),
('11111111-1111-1111-1111-000000000010','julia@example.com','Julia','hash10','user');

INSERT INTO viviendas (id, id_usuario, nombre, calle, altura, piso, nota) VALUES
('22222222-2222-2222-2222-000000000001','11111111-1111-1111-1111-000000000001','Casa Ana','San Martín','1200',NULL,'Casa principal con patio'),
('22222222-2222-2222-2222-000000000002','11111111-1111-1111-1111-000000000002','Depto Bruno','Belgrano','540','3','Depto de 3 ambientes'),
('22222222-2222-2222-2222-000000000003','11111111-1111-1111-1111-000000000003','Casa Carla','Rivadavia','2300',NULL,'Dúplex'),
('22222222-2222-2222-2222-000000000004','11111111-1111-1111-1111-000000000004','Casa Diego','9 de Julio','450',NULL,'Con patio grande'),
('22222222-2222-2222-2222-000000000005','11111111-1111-1111-1111-000000000005','Depto Eva','Mitre','800','7','Vista al río'),
('22222222-2222-2222-2222-000000000006','11111111-1111-1111-1111-000000000006','Casa Facu','Sarmiento','1500',NULL,'Con cochera'),
('22222222-2222-2222-2222-000000000007','11111111-1111-1111-1111-000000000007','Casa Gina','Italia','300',NULL,'Recién pintada'),
('22222222-2222-2222-2222-000000000008','11111111-1111-1111-1111-000000000008','Casa Hugo','España','990',NULL,'Obra nueva'),
('22222222-2222-2222-2222-000000000009','11111111-1111-1111-1111-000000000009','Depto Iván','Perú','1330','2','Monoambiente'),
('22222222-2222-2222-2222-000000000010','11111111-1111-1111-1111-000000000010','Casa Julia','Francia','410',NULL,'Amplia y luminosa');

INSERT INTO dispositivos (id, id_vivienda, nombre_dispositivo, tipo_dispositivo, estado) VALUES
('33333333-3333-3333-3333-AC0000000001','22222222-2222-2222-2222-000000000001','AA Living','aire_acondicionado',TRUE),
('33333333-3333-3333-3333-AC0000000002','22222222-2222-2222-2222-000000000001','AA Dormitorio','aire_acondicionado',FALSE),
('33333333-3333-3333-3333-AC0000000003','22222222-2222-2222-2222-000000000002','AA Comedor','aire_acondicionado',TRUE),
('33333333-3333-3333-3333-AC0000000004','22222222-2222-2222-2222-000000000003','AA Escritorio','aire_acondicionado',FALSE),
('33333333-3333-3333-3333-AC0000000005','22222222-2222-2222-2222-000000000004','AA Pasillo','aire_acondicionado',TRUE),
('33333333-3333-3333-3333-AC0000000006','22222222-2222-2222-2222-000000000005','AA Dormitorio','aire_acondicionado',TRUE),
('33333333-3333-3333-3333-AC0000000007','22222222-2222-2222-2222-000000000005','AA Living','aire_acondicionado',FALSE),
('33333333-3333-3333-3333-AC0000000008','22222222-2222-2222-2222-000000000004','AA Cocina','aire_acondicionado',TRUE),
('33333333-3333-3333-3333-AC0000000009','22222222-2222-2222-2222-000000000003','AA Taller','aire_acondicionado',TRUE),
('33333333-3333-3333-3333-AC0000000010','22222222-2222-2222-2222-000000000002','AA Balcón','aire_acondicionado',FALSE),
('33333333-3333-3333-3333-LU0000000001','22222222-2222-2222-2222-000000000006','Luz Living','luz',TRUE),
('33333333-3333-3333-3333-LU0000000002','22222222-2222-2222-2222-000000000006','Luz Cocina','luz',FALSE),
('33333333-3333-3333-3333-LU0000000003','22222222-2222-2222-2222-000000000007','Luz Patio','luz',TRUE),
('33333333-3333-3333-3333-LU0000000004','22222222-2222-2222-2222-000000000007','Luz Dormitorio','luz',TRUE),
('33333333-3333-3333-3333-LU0000000005','22222222-2222-2222-2222-000000000008','Luz Baño','luz',FALSE),
('33333333-3333-3333-3333-LU0000000006','22222222-2222-2222-2222-000000000008','Luz Garage','luz',TRUE),
('33333333-3333-3333-3333-LU0000000007','22222222-2222-2222-2222-000000000009','Luz Hall','luz',FALSE),
('33333333-3333-3333-3333-LU0000000008','22222222-2222-2222-2222-000000000009','Luz Escritorio','luz',TRUE),
('33333333-3333-3333-3333-LU0000000009','22222222-2222-2222-2222-000000000010','Luz Terraza','luz',TRUE),
('33333333-3333-3333-3333-LU0000000010','22222222-2222-2222-2222-000000000010','Luz Comedor','luz',FALSE),
('33333333-3333-3333-3333-VE0000000001','22222222-2222-2222-2222-000000000001','Vent Living','ventilador',TRUE),
('33333333-3333-3333-3333-VE0000000002','22222222-2222-2222-2222-000000000002','Vent Techo','ventilador',TRUE),
('33333333-3333-3333-3333-VE0000000003','22222222-2222-2222-2222-000000000003','Vent Pie','ventilador',FALSE),
('33333333-3333-3333-3333-VE0000000004','22222222-2222-2222-2222-000000000004','Vent Escritorio','ventilador',TRUE),
('33333333-3333-3333-3333-VE0000000005','22222222-2222-2222-2222-000000000005','Vent Pared','ventilador',FALSE),
('33333333-3333-3333-3333-VE0000000006','22222222-2222-2222-2222-000000000006','Vent Garage','ventilador',TRUE),
('33333333-3333-3333-3333-VE0000000007','22222222-2222-2222-2222-000000000007','Vent Terraza','ventilador',TRUE),
('33333333-3333-3333-3333-VE0000000008','22222222-2222-2222-2222-000000000008','Vent Taller','ventilador',FALSE),
('33333333-3333-3333-3333-VE0000000009','22222222-2222-2222-2222-000000000009','Vent Patio','ventilador',TRUE),
('33333333-3333-3333-3333-VE0000000010','22222222-2222-2222-2222-000000000010','Vent Dormitorio','ventilador',TRUE);

INSERT INTO aires_acondicionados (id, temperatura, velocidad, modo) VALUES
('33333333-3333-3333-3333-AC0000000001',24,2,'frio'),
('33333333-3333-3333-3333-AC0000000002',26,1,'auto'),
('33333333-3333-3333-3333-AC0000000003',22,3,'frio'),
('33333333-3333-3333-3333-AC0000000004',20,3,'frio'),
('33333333-3333-3333-3333-AC0000000005',25,2,'seco'),
('33333333-3333-3333-3333-AC0000000006',23,2,'frio'),
('33333333-3333-3333-3333-AC0000000007',27,1,'ventilacion'),
('33333333-3333-3333-3333-AC0000000008',21,3,'frio'),
('33333333-3333-3333-3333-AC0000000009',24,2,'frio'),
('33333333-3333-3333-3333-AC0000000010',28,1,'calor');

INSERT INTO luces (id, modo, intensidad) VALUES
('33333333-3333-3333-3333-LU0000000001','blanco',1),
('33333333-3333-3333-3333-LU0000000002','calido',2),
('33333333-3333-3333-3333-LU0000000003','frio',3),
('33333333-3333-3333-3333-LU0000000004','blanco',3),
('33333333-3333-3333-3333-LU0000000005','calido',1),
('33333333-3333-3333-3333-LU0000000006','blanco',2),
('33333333-3333-3333-3333-LU0000000007','frio',1),
('33333333-3333-3333-3333-LU0000000008','blanco',2),
('33333333-3333-3333-3333-LU0000000009','calido',3),
('33333333-3333-3333-3333-LU0000000010','frio',3);

INSERT INTO ventiladores (id, velocidad, giro) VALUES
('33333333-3333-3333-3333-VE0000000001',2,TRUE),
('33333333-3333-3333-3333-VE0000000002',3,FALSE),
('33333333-3333-3333-3333-VE0000000003',1,TRUE),
('33333333-3333-3333-3333-VE0000000004',3,TRUE),
('33333333-3333-3333-3333-VE0000000005',2,FALSE),
('33333333-3333-3333-3333-VE0000000006',1,TRUE),
('33333333-3333-3333-3333-VE0000000007',2,TRUE),
('33333333-3333-3333-3333-VE0000000008',3,FALSE),
('33333333-3333-3333-3333-VE0000000009',1,TRUE),
('33333333-3333-3333-3333-VE0000000010',2,TRUE);

INSERT INTO rutinas (id, id_dispositivo, descripcion,horario_inicio, horario_apagado, horario_encendido, estado_rutina) VALUES
('44444444-4444-4444-4444-000000000001','33333333-3333-3333-3333-LU0000000001','ENCENDER','2025-10-01 07:00:00','2025-10-01 23:30:00','2025-10-01 07:00:00',TRUE),
('44444444-4444-4444-4444-000000000002','33333333-3333-3333-3333-LU0000000002','APAGAR','2025-10-01 18:30:00','2025-10-01 23:00:00','2025-10-01 18:30:00',TRUE),
('44444444-4444-4444-4444-000000000003','33333333-3333-3333-3333-AC0000000001','CAMBIAR MODO CALOR','2025-10-01 14:00:00','2025-10-01 18:00:00','2025-10-01 14:15:00',TRUE),
('44444444-4444-4444-4444-000000000004','33333333-3333-3333-3333-AC0000000003','CAMBIAR MODO FRIO','2025-10-01 12:00:00','2025-10-01 16:00:00','2025-10-01 12:05:00',FALSE),
('44444444-4444-4444-4444-000000000005','33333333-3333-3333-3333-VE0000000002','SUBIR VELOCIDAD','2025-10-01 10:00:00','2025-10-01 12:00:00','2025-10-01 10:00:00',TRUE),
('44444444-4444-4444-4444-000000000006','33333333-3333-3333-3333-VE0000000004','APAGAR','2025-10-01 21:00:00','2025-10-02 06:00:00','2025-10-01 21:00:00',TRUE),
('44444444-4444-4444-4444-000000000007','33333333-3333-3333-3333-LU0000000005','ACTIVAR MODO FIESTA','2025-10-01 06:30:00','2025-10-01 08:00:00','2025-10-01 06:30:00',FALSE),
('44444444-4444-4444-4444-000000000008','33333333-3333-3333-3333-LU0000000009','ACTIVAR MODO NOCTURNO','2025-10-01 19:00:00','2025-10-01 22:00:00','2025-10-01 19:00:00',TRUE),
('44444444-4444-4444-4444-000000000009','33333333-3333-3333-3333-AC0000000008','BAJAR TEMPERATURA','2025-10-01 11:00:00','2025-10-01 13:00:00','2025-10-01 11:00:00',TRUE),
('44444444-4444-4444-4444-000000000010','33333333-3333-3333-3333-VE0000000009','ENCENDER','2025-10-01 15:00:00','2025-10-01 17:30:00','2025-10-01 15:00:00',TRUE);

INSERT INTO historiales (id, id_dispositivo, fecha, descripcion) VALUES
('55555555-5555-5555-5555-000000000001','33333333-3333-3333-3333-LU0000000001','2025-10-01 07:05:00','Encendido automático'),
('55555555-5555-5555-5555-000000000002','33333333-3333-3333-3333-LU0000000001','2025-10-01 23:35:00','Apagado por rutina'),
('55555555-5555-5555-5555-000000000003','33333333-3333-3333-3333-AC0000000001','2025-10-01 14:20:00','Modo frío 24°C'),
('55555555-5555-5555-5555-000000000004','33333333-3333-3333-3333-VE0000000002','2025-10-01 10:10:00','Velocidad 3'),
('55555555-5555-5555-5555-000000000005','33333333-3333-3333-3333-AC0000000008','2025-10-01 11:10:00','Encendido manual'),
('55555555-5555-5555-5555-000000000006','33333333-3333-3333-3333-LU0000000005','2025-10-01 06:35:00','Intensidad 30%'),
('55555555-5555-5555-5555-000000000007','33333333-3333-3333-3333-LU0000000009','2025-10-01 20:00:00','Cambio a modo cálido'),
('55555555-5555-5555-5555-000000000008','33333333-3333-3333-3333-VE0000000004','2025-10-01 21:05:00','Activado por rutina nocturna'),
('55555555-5555-5555-5555-000000000009','33333333-3333-3333-3333-LU0000000008','2025-10-01 19:10:00','Encendido manual'),
('55555555-5555-5555-5555-000000000010','33333333-3333-3333-3333-AC0000000003','2025-10-01 12:10:00','Rutina deshabilitada');

-- usuarios y rol 
SELECT id, nombre, correo, rol FROM usuarios ORDER BY nombre;

-- viviendas
SELECT id, id_usuario, nombre, calle, altura, piso FROM viviendas ORDER BY id;

-- dispositivos y estado actual
SELECT id, id_vivienda, nombre_dispositivo, tipo_dispositivo, estado FROM dispositivos ORDER BY id;

-- dispositivo y configuracion actual
SELECT id, temperatura, velocidad, modo FROM aires_acondicionados ORDER BY id;
SELECT id, modo, intensidad FROM luces ORDER BY id;
SELECT id, velocidad, giro FROM ventiladores ORDER BY id;

-- rutinas activas e inactivas
SELECT id, id_dispositivo, horario_inicio, horario_apagado, estado_rutina FROM rutinas ORDER BY id;

-- eventos mas recientes
SELECT id, id_dispositivo, fecha, descripcion FROM historiales ORDER BY fecha DESC;

-- que dispositivos tiene cada usuario y el estado de cada uno
SELECT u.nombre AS usuario, d.id AS dispositivo_id, d.nombre_dispositivo, d.tipo_dispositivo, d.estado
FROM dispositivos d
JOIN viviendas v ON v.id = d.id_vivienda
JOIN usuarios  u ON u.id = v.id_usuario
ORDER BY usuario, d.tipo_dispositivo, d.nombre_dispositivo;

-- Ultimo evento del dispositivo
SELECT d.id AS dispositivo_id,
       d.nombre_dispositivo,
       d.tipo_dispositivo,
       (SELECT h.descripcion FROM historiales h WHERE h.id_dispositivo = d.id ORDER BY h.fecha DESC LIMIT 1) AS ultimo_evento,
       (SELECT h.fecha       FROM historiales h WHERE h.id_dispositivo = d.id ORDER BY h.fecha DESC LIMIT 1) AS fecha_ultimo_evento
FROM dispositivos d
ORDER BY fecha_ultimo_evento DESC;

-- cuantos dispositivos de cada tipo en que casa
SELECT v.nombre AS vivienda, d.tipo_dispositivo, COUNT(*) AS cantidad
FROM dispositivos d
JOIN viviendas v ON v.id = d.id_vivienda
GROUP BY v.nombre, d.tipo_dispositivo
ORDER BY vivienda, tipo_dispositivo;

-- rutinas activas 
SELECT u.nombre AS usuario, v.nombre AS vivienda, d.nombre_dispositivo, d.tipo_dispositivo,
       r.estado_rutina, r.horario_encendido, r.horario_apagado
FROM rutinas r
JOIN dispositivos d ON d.id = r.id_dispositivo
JOIN viviendas  v  ON v.id = d.id_vivienda
JOIN usuarios   u  ON u.id = v.id_usuario
where estado_rutina =1
ORDER BY usuario, vivienda, r.horario_encendido;

-- aires acondicionados de cada usuario
SELECT u.nombre AS usuario, v.nombre AS vivienda, d.nombre_dispositivo,
       aa.temperatura, aa.velocidad, aa.modo, d.estado
FROM aires_acondicionados aa
JOIN dispositivos d ON d.id = aa.id
JOIN viviendas v ON v.id = d.id_vivienda
JOIN usuarios u ON u.id = v.id_usuario
ORDER BY usuario, vivienda;

-- luces con intensidad muy alta
SELECT u.nombre AS usuario, v.nombre AS vivienda, d.nombre_dispositivo, l.intensidad
FROM luces l
JOIN dispositivos d ON d.id = l.id
JOIN viviendas v ON v.id = d.id_vivienda
JOIN usuarios u ON u.id = v.id_usuario
LEFT JOIN rutinas r ON r.id_dispositivo = d.id
WHERE l.intensidad = 3 AND r.id IS NULL
ORDER BY u.nombre, v.nombre;

-- dispositivo sin rutina/automatizar
SELECT d.id, d.nombre_dispositivo, d.tipo_dispositivo
FROM dispositivos d
WHERE NOT EXISTS (SELECT 1 FROM rutinas r WHERE r.id_dispositivo = d.id)
ORDER BY d.tipo_dispositivo, d.nombre_dispositivo;

-- que usuarios tienen 3 o mas dispositivos
SELECT u.id, u.nombre, u.correo,
       (SELECT COUNT(*) FROM dispositivos d
         JOIN viviendas v ON v.id = d.id_vivienda
        WHERE v.id_usuario = u.id) AS total_dispositivos
FROM usuarios u
WHERE (SELECT COUNT(*) FROM dispositivos d
         JOIN viviendas v ON v.id = d.id_vivienda
        WHERE v.id_usuario = u.id) >= 3
ORDER BY total_dispositivos DESC;

-- aires con temperatura "alta" (mayor a 26)
SELECT d.id AS dispositivo_id, u.nombre AS usuario, aa.temperatura, aa.modo
FROM aires_acondicionados aa
JOIN dispositivos d ON d.id = aa.id
JOIN viviendas v ON v.id = d.id_vivienda
JOIN usuarios u ON u.id = v.id_usuario
WHERE aa.temperatura >= 26
ORDER BY aa.temperatura DESC;