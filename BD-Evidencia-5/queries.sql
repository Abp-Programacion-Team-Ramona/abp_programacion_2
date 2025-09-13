

CREATE TABLE usuarios (
    id CHAR(36) PRIMARY KEY,
    correo VARCHAR(100) NOT NULL,
    nombre VARCHAR(100) NOT NULL,
    contraseña VARCHAR(100) NOT NULL,
    rol VARCHAR(50) NOT NULL
);

CREATE TABLE viviendas (
    id CHAR(36) PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    id_usuario CHAR(36) NOT NULL,
    calle VARCHAR(100) NOT NULL,
    altura VARCHAR(20) NOT NULL,
    piso VARCHAR(20),
    nota VARCHAR(255),
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id) ON DELETE CASCADE
);

CREATE TABLE rutinas (
    id CHAR(36) PRIMARY KEY,
    horario_inicio DATETIME NOT NULL,
    horario_apagado DATETIME NOT NULL,
    horario_encendido DATETIME NOT NULL,
    estado_rutina BOOLEAN NOT NULL
);

CREATE TABLE dispositivos (
    id CHAR(36) PRIMARY KEY,
    nombre_dispositivo: varchar(50) not null,
    id_vivienda CHAR(36) NOT NULL,
    id_rutina CHAR(36),
    tipo_dispositivo VARCHAR(50) NOT NULL,
    estado BOOLEAN NOT NULL,
    FOREIGN KEY (id_vivienda) REFERENCES viviendas(id) ON DELETE CASCADE,
    FOREIGN KEY (id_rutina) REFERENCES rutinas(id) ON DELETE SET NULL
);

CREATE TABLE historiales (
    id CHAR(36) PRIMARY KEY,
    id_dispositivo CHAR(36) NOT NULL,
    fecha DATETIME NOT NULL,
    descripcion VARCHAR(255) NOT NULL,
    FOREIGN KEY (id_dispositivo) REFERENCES dispositivos(id) ON DELETE CASCADE
);


INSERT INTO usuarios (id, correo, nombre, contraseña, rol) VALUES
('11111111-1111-1111-1111-111111111111', 'marco.remon@cifradocesar.com', 'Benjamin Ciri', 'frqwudvhñd', 'admin'),
('22222222-2222-2222-2222-222222222222', 'candeBlanco@cifradocesar.com', 'Luz Coco', 'fliudgrfhvdu', 'usuario');

INSERT INTO viviendas (id, nombre, id_usuario, calle, altura, piso, nota) VALUES
('33333333-3333-3333-3333-333333333333', 'Casa', '11111111-1111-1111-1111-111111111111', 'Av. Los Valientes', '742', NULL, 'Casa mia'),
('44444444-4444-4444-4444-444444444444', 'Depto Hija', '22222222-2222-2222-2222-222222222222', 'Calle Independencia', '123', '3B', 'NO FUNCIONA TIMBRE');

INSERT INTO rutinas (id, horario_inicio, horario_apagado, horario_encendido, estado_dispositivo) VALUES
('55555555-5555-5555-5555-555555555555', '2025-09-10 07:00:00', '2025-09-10 23:00:00', '2025-09-10 07:00:00', true),
('66666666-6666-6666-6666-666666666666', '2025-09-10 18:00:00', '2025-09-10 23:30:00', '2025-09-10 18:00:00', true),
('77777777-7777-7777-7777-777777777777', '2025-09-10 12:00:00', '2025-09-10 16:00:00', '2025-09-10 12:00:00', false),
('88888888-8888-8888-8888-888888888888', '2025-09-10 20:00:00', '2025-09-11 02:00:00', '2025-09-10 20:00:00', true);

INSERT INTO rutinas (id, horario_inicio, horario_apagado, horario_encendido, estado_dispositivo) VALUES
('99990000-aaaa-bbbb-cccc-111111111111', '2025-09-11 08:00:00', '2025-09-11 20:00:00', '2025-09-11 08:00:00', true),
('99990000-bbbb-cccc-dddd-222222222222', '2025-09-11 06:30:00', '2025-09-11 22:30:00', '2025-09-11 06:30:00', false);


INSERT INTO dispositivos (id,nombre_dispositivo, id_vivienda, id_rutina, tipo_dispositivo, estado) VALUES
('99999999-1111-1111-1111-999999999999','aire pieza', '33333333-3333-3333-3333-333333333333', '55555555-5555-5555-5555-555555555555', 'aire', true),
('99999999-2222-2222-2222-999999999999','luz afuera atras', '33333333-3333-3333-3333-333333333333', '66666666-6666-6666-6666-666666666666', 'luz', false),
('99999999-3333-3333-3333-999999999999','ventilador cocina', '33333333-3333-3333-3333-333333333333', '77777777-7777-7777-7777-777777777777', 'ventilador', true),
('99999999-4444-4444-4444-999999999999','aire living', '44444444-4444-4444-4444-444444444444', '88888888-8888-8888-8888-888888888888', 'aire', true),
('99999999-5555-5555-5555-999999999999','luz frente', '44444444-4444-4444-4444-444444444444', '55555555-5555-5555-5555-555555555555', 'luz', true),
('99999999-6666-6666-6666-999999999999','ventilador living', '44444444-4444-4444-4444-444444444444', '66666666-6666-6666-6666-666666666666', 'ventilador', false);

INSERT INTO dispositivos (id,nombre_dispositivo, id_vivienda, id_rutina, tipo_dispositivo, estado) VALUES
('aaaa1111-bbbb-cccc-dddd-eeee11111111','ventilador pieza abuela', '33333333-3333-3333-3333-333333333333', '99990000-aaaa-bbbb-cccc-111111111111', 'ventilador', true),
('bbbb2222-cccc-dddd-eeee-ffff22222222','ventilador estudio', '44444444-4444-4444-4444-444444444444', '99990000-bbbb-cccc-dddd-222222222222', 'ventilador', false);


INSERT INTO historiales (id, id_dispositivo, fecha, descripcion) VALUES
('aaaaaaa1-aaaa-aaaa-aaaa-aaaaaaaaaaaa', '99999999-1111-1111-1111-999999999999', '2025-09-09 10:00:00', 'Encendido automático por rutina'),
('aaaaaaa2-aaaa-aaaa-aaaa-aaaaaaaaaaaa', '99999999-1111-1111-1111-999999999999', '2025-09-09 22:00:00', 'Apagado programado'),
('aaaaaaa3-aaaa-aaaa-aaaa-aaaaaaaaaaaa', '99999999-2222-2222-2222-999999999999', '2025-09-09 19:30:00', 'Luz encendida manualmente'),
('aaaaaaa4-aaaa-aaaa-aaaa-aaaaaaaaaaaa', '99999999-3333-3333-3333-999999999999', '2025-09-09 12:05:00', 'Ventilador encendido por rutina'),
('aaaaaaa5-aaaa-aaaa-aaaa-aaaaaaaaaaaa', '99999999-3333-3333-3333-999999999999', '2025-09-09 16:00:00', 'Ventilador apagado programado'),
('bbbbbbb1-bbbb-bbbb-bbbb-bbbbbbbbbbbb', '99999999-4444-4444-4444-999999999999', '2025-09-09 20:15:00', 'Aire acondicionado encendido automático'),
('bbbbbbb2-bbbb-bbbb-bbbb-bbbbbbbbbbbb', '99999999-4444-4444-4444-999999999999', '2025-09-10 02:00:00', 'Aire acondicionado apagado programado'),
('bbbbbbb3-bbbb-bbbb-bbbb-bbbbbbbbbbbb', '99999999-5555-5555-5555-999999999999', '2025-09-09 18:00:00', 'Luz encendida por rutina'),
('bbbbbbb4-bbbb-bbbb-bbbb-bbbbbbbbbbbb', '99999999-5555-5555-5555-999999999999', '2025-09-09 23:30:00', 'Luz apagada automática'),
('bbbbbbb5-bbbb-bbbb-bbbb-bbbbbbbbbbbb', '99999999-6666-6666-6666-999999999999', '2025-09-09 21:00:00', 'Ventilador encendido manualmente');

INSERT INTO historiales (id, id_dispositivo, fecha, descripcion) VALUES
('cccc3333-dddd-eeee-ffff-gggg33333333', 'aaaa1111-bbbb-cccc-dddd-eeee11111111', '2025-09-11 09:00:00', 'Ventilador encendido'),
('dddd4444-eeee-ffff-gggg-hhhh44444444', 'bbbb2222-cccc-dddd-eeee-ffff22222222', '2025-09-11 21:15:00', 'Ventilador encendido');


select * from usuarios

select * from viviendas

select * from rutinas where estado_dispositivo=true

select * from dispositivos where tipo_dispositivo = 'aire' and estado =1

select * from historiales
