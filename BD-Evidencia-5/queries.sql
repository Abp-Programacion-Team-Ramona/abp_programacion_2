CREATE TABLE rutinas (
    id CHAR(36) PRIMARY KEY,
    horario_inicio DATETIME NOT NULL,
    horario_apagado DATETIME NOT NULL,
    horario_encendido DATETIME NOT NULL,
    estado_rutina BOOLEAN NOT NULL
);

INSERT INTO rutinas (id, horario_inicio, horario_apagado, horario_encendido, estado_rutina) VALUES
('55555555-5555-5555-5555-555555555555', '2025-09-10 07:00:00', '2025-09-10 23:00:00', '2025-09-10 07:00:00', true),
('66666666-6666-6666-6666-666666666666', '2025-09-10 18:00:00', '2025-09-10 23:30:00', '2025-09-10 18:00:00', true),
('77777777-7777-7777-7777-777777777777', '2025-09-10 12:00:00', '2025-09-10 16:00:00', '2025-09-10 12:00:00', false),
('88888888-8888-8888-8888-888888888888', '2025-09-10 20:00:00', '2025-09-11 02:00:00', '2025-09-10 20:00:00', true);

INSERT INTO rutinas (id, horario_inicio, horario_apagado, horario_encendido, estado_rutina) VALUES
('99990000-aaaa-bbbb-cccc-111111111111', '2025-09-11 08:00:00', '2025-09-11 20:00:00', '2025-09-11 08:00:00', true),
('99990000-bbbb-cccc-dddd-222222222222', '2025-09-11 06:30:00', '2025-09-11 22:30:00', '2025-09-11 06:30:00', false);