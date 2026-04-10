DROP DATABASE IF EXISTS gha_analytics;
CREATE DATABASE gha_analytics CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE gha_analytics;

-- 1. Tabla de Pacientes (Crítica: NIFs sucios, muchos NULLs)
CREATE TABLE pacientes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nif VARCHAR(50),
    nombre_completo VARCHAR(200),
    email VARCHAR(150),
    tel_contacto VARCHAR(50),
    f_nacimiento VARCHAR(50),
    num_poliza VARCHAR(50) -- Muchos NULLs para pacientes sin seguro
) ENGINE=InnoDB;

-- 2. Tabla de Médicos (Códigos de colegiado con formatos inconsistentes)
CREATE TABLE medicos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    num_colegiado VARCHAR(50),
    nombre VARCHAR(150),
    especialidad_id INT
) ENGINE=InnoDB;

-- 3. Especialidades
CREATE TABLE especialidades (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50)
) ENGINE=InnoDB;

-- 4. Visitas Médicas (Fechas VARCHAR, Costes sucios)
CREATE TABLE visitas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    paciente_id INT,
    medico_id INT,
    fecha_visita VARCHAR(100),
    importe_sucio VARCHAR(50),
    descuento_aplicado VARCHAR(20), -- Muchos NULLs
    observaciones TEXT
) ENGINE=InnoDB;

-- 5. Tabla de Staging (Volcado masivo de CSV externo)
CREATE TABLE raw_import_visitas (
    ext_id INT,
    raw_data TEXT, -- Formato: "NIF|Nombre|FechaVisita|Coste"
    raw_phone VARCHAR(50)
);

-- ==========================================
-- CARGA DE DATOS "RADIOACTIVOS"
-- ==========================================

INSERT INTO especialidades (nombre) VALUES ('Medicina General'), ('Pediatría'), ('Cardiología'), ('Traumatología');

INSERT INTO pacientes (nif, nombre_completo, email, tel_contacto, f_nacimiento, num_poliza) VALUES
('12345678A', 'Juan Carlos Ibañez', 'jc.ibanez@mail.com', '+34 600 111 222', '12/05/1980', 'POL-9988'),
('87654321-B', 'Maria Lopez Sanz', 'm.lopez@gmail,con', '611-222-333', '1992.08.15', NULL), -- NIF guion, email coma/con, poliza null
(' 11223344C ', '  LUIS MARTINEZ  ', 'luis@test@es', '0034622444555', '01-01-1975', 'POL-1122'), -- Espacios, doble arroba
('12345678A', 'Juan Carlos Ibañez', 'jc.ibanez@mail.com', '600111222', '12/05/1980', 'POL-9988'), -- Duplicado exacto
('22334455D', 'Ana Ruiz Pardo', NULL, NULL, '20/10/2005', NULL), -- Casi todo NULL
('99999999Z', 'Paciente de Borrado', 'test@delete.com', '123', '2020-01-01', 'FAKE-000'),
('44556677X', 'Sonia  Valverde', 'sonia.v@outlook.com', '+34 655-999-000', '15/03/1988', 'POL-5566'),
('44556677X', 'Sonia Valverde', 'sonia.v@outlook.com', '655999000', '15/03/1988', 'POL-5566'), -- Duplicado con ligeras diferencias
('NULL_NIF', 'Error en Registro', NULL, '912334455', NULL, NULL);

INSERT INTO medicos (num_colegiado, nombre, especialidad_id) VALUES
('COL-28-1234', 'Dr. House', 1),
('28/5566', 'Dra. Quinn', 2),
('COL289900', 'Dr. Strange', 3),
('28-7788', 'Dr. Zivago', 1),
('INV-999', 'Medico Provisional', 99); -- Especialidad inexistente

INSERT INTO visitas (paciente_id, medico_id, fecha_visita, importe_sucio, descuento_aplicado, observaciones) VALUES
(1, 1, '12/03/2026 10:30', '150.50€', '10.00', 'Revisión anual'),
(2, 2, '2026.03.13 09:00', '$80.00', NULL, NULL), -- Importe $, descuento null
(3, 1, '14-03-2026 11:15', ' 120,00 ', '5.50', 'Dolor muscular'),
(1, 1, '12/03/2026 10:30', '150.50€', '10.00', NULL), -- Visita duplicada
(999, 1, '15/03/2026 12:00', '50.00', NULL, 'Paciente inexistente'),
(4, 888, '16/03/2026 13:00', '75.00', '0.00', 'Médico inexistente'),
(5, 3, '17/03/2026 10:00', 'Gratis', NULL, 'Campaña promoción'),
(1, 2, '18/03/2026 11:00', '200.00 EUR', '20.00', 'Urgencia');

INSERT INTO raw_import_visitas VALUES 
(1001, '12345678A|Juan Carlos|12/03/2026|150.50', '600111222'),
(1002, '44556677X|Sonia Valverde|15/03/2026|75.00', NULL),
(1003, '11223344C|LUIS MARTINEZ|2026-03-17|120,00 EUR', '622444555'),
(1004, '55667788Y|Roberto Gomez|18/03/2026|90.00$', '611000999'),
(1005, '99887766K|Elena Nito|2026.03.19| GRATIS ', NULL),
(1006, '12345678A|Juan Carlos|20/03/2026|200.00', '600111222'),
(1007, '87654321B|Maria Lopez|21-03-2026|110.00', '611222333');

SET SQL_SAFE_UPDATES = 0;

-- Normalización de Identidad (Pacientes):
-- Hacemos un inner join con la misma tabla para comparar el nombre y el nif y borramos el que tenga el id mas alto
DELETE p1 from pacientes p1 INNER JOIN pacientes p2
WHERE p1.id > p2.id AND p1.nif = p2.nif;
-- Quitamos los espacios en los NIF
UPDATE pacientes SET nif = REPLACE(nif,' ','');
-- Quitamos los guiones que separan algún NIF
UPDATE pacientes SET nif = REPLACE(nif,'-','');
-- Eliminamos las filas que no tengan exactamente 9 caracteres en el NIF
DELETE p1 from pacientes p1 WHERE length(nif) != 9;
-- Añadimos check con el REGEXP para validar que se cumpla el patrón del NIF.
ALTER TABLE pacientes
ADD CONSTRAINT chk_nif check (nif REGEXP '^[0-9]{8}[A-Z]$');
-- Convertimos la columna NIF en unica y sin nulos
ALTER TABLE pacientes
MODIFY COLUMN nif char(9) NOT NULL,
ADD CONSTRAINT unique_nif UNIQUE(nif);

-- Actualizamos los datos que tengan un formato parecido al exigido (6 números)
UPDATE medicos 
SET num_colegiado = CONCAT(
    'COL-', 
    SUBSTRING(REGEXP_REPLACE(num_colegiado, '[^0-9]', ''), 1, 2), 
    '-', 
    SUBSTRING(REGEXP_REPLACE(num_colegiado, '[^0-9]', ''), 3, 4)
)
WHERE LENGTH(REGEXP_REPLACE(num_colegiado, '[^0-9]', '')) = 6
  AND num_colegiado NOT REGEXP '^COL-[0-9]{2}-[0-9]{4}$';

-- Eliminamos los datos que no sigan el formato especificado.
DELETE FROM medicos
WHERE num_colegiado NOT REGEXP '^COL-[0-9]{2}-[0-9]{4}$';

-- Añadimos check para que no se introduzcan datos que no sigan el regex
ALTER TABLE medicos
ADD CONSTRAINT chk_formato_colegiado
CHECK (num_colegiado REGEXP '^COL-[0-9]{2}-[0-9]{4}$');

-- Asignamos al id 1 las especialidades que no sean 1,2,3,4 usando una subconsulta de la tabla especialidades
UPDATE medicos
SET especialidad_id = 1
WHERE especialidad_id NOT IN (SELECT id FROM especialidades);

-- Añadimos la clave foranea en la tabla medicos para las especialidades.
ALTER TABLE medicos
ADD CONSTRAINT fk_medicos_especialidad
FOREIGN KEY (especialidad_id) REFERENCES especialidades(id);
-- Para poder actualizar las claves foraneas, tenemos que borrar las visitas con pacientes/medicos inexistentes.

DELETE FROM visitas 
WHERE paciente_id NOT IN (SELECT id FROM pacientes);
DELETE FROM visitas 
WHERE medico_id NOT IN (SELECT id FROM medicos);

-- Ahora si añadimos claves foraneas en al tabla especialidades del id de los pacientes y el id de los medicos
ALTER TABLE visitas
ADD CONSTRAINT fk_visitas_paciente
FOREIGN KEY (paciente_id) REFERENCES pacientes(id),
ADD CONSTRAINT fk_visitas_medico
FOREIGN KEY (medico_id) REFERENCES medicos(id);


-- Normalizamos la información de la tabla pacientes, para tener la información de los seguros de los pacientes y su estado, asegurando la integridad referencial.
CREATE TABLE seguros_pacientes (
    id_seguro_paciente INT AUTO_INCREMENT,
    id_paciente INT NOT NULL,
    num_poliza VARCHAR(50) NOT NULL,
    estado_poliza VARCHAR(20) DEFAULT 'ACTIVA',
    CONSTRAINT fk_id_seguro_paciente PRIMARY KEY(id_seguro_paciente),
    CONSTRAINT fk_id_paciente FOREIGN KEY (id_paciente)
		REFERENCES pacientes(id));
        
-- Migramos los datos de la tabla pacientes a la nueva tabla para tener la información que tenemos
INSERT INTO seguros_pacientes (id_paciente, num_poliza)
SELECT id, num_poliza 
FROM pacientes 
WHERE num_poliza IS NOT NULL;

-- Eliminamos la columna num_poliza para terminar de normalizar la tabla, ya que si no tendriamos los datos en las dos tablas.
ALTER TABLE pacientes
DROP COLUMN num_poliza;

-- Columnas Calculadas y Blindaje
-- Añadimos a la tabla visitas la columna copago_estimado
ALTER TABLE visitas
ADD COLUMN copago_estimado DECIMAL(10,2);

-- Ponemos los datos en la nueva tabla creada, de una manera limpia.
UPDATE visitas
SET copago_estimado = (
    CASE 
        WHEN UPPER(importe_sucio) LIKE '%GRATIS%' THEN 0
        ELSE CAST(REGEXP_REPLACE(REPLACE(importe_sucio, ',', '.'), '[^0-9.]', '') AS DECIMAL(10,2))
    END
) * 0.20;

-- Modificamos la columna copago_estimado y seguros_pacientes de sus respectivas tablas para que no puedan ser nulos.
ALTER TABLE visitas
MODIFY COLUMN copago_estimado DECIMAL(10,2) NOT NULL;

ALTER TABLE seguros_pacientes
MODIFY COLUMN num_poliza VARCHAR(50) NOT NULL;

-- 5.
-- Migramos los datos de raw_import_visitas para ponerlos en los campos correspondientes, asegurando de que no haya duplicados con el distinct.
-- Primero insertamos los pacientes

INSERT INTO pacientes (nif, nombre_completo, tel_contacto)
SELECT DISTINCT 
    TRIM(SUBSTRING_INDEX(raw_data, '|', 1)) AS nuevo_nif, 
    TRIM(SUBSTRING_INDEX(SUBSTRING_INDEX(raw_data, '|', 2), '|', -1)) AS nuevo_nombre,
    raw_phone
FROM raw_import_visitas raw
WHERE 
    REGEXP_REPLACE(UPPER(SUBSTRING_INDEX(raw_data, '|', 1)), '[^A-Z0-9]', '') 
    NOT IN (
        SELECT REGEXP_REPLACE(UPPER(nif), '[^A-Z0-9]', '') 
        FROM pacientes 
        WHERE nif IS NOT NULL
    );

-- Y ahora insertamos los datos en la tabla visitas.
INSERT INTO visitas (paciente_id, medico_id, fecha_visita, importe_sucio, copago_estimado)
SELECT 
    p.id AS paciente_id,
    1 AS medico_id,
    TRIM(SUBSTRING_INDEX(SUBSTRING_INDEX(raw.raw_data, '|', 3), '|', -1)) AS fecha_visita,
    TRIM(SUBSTRING_INDEX(raw.raw_data, '|', -1)) AS importe_sucio,
    (CASE 
        WHEN UPPER(SUBSTRING_INDEX(raw.raw_data, '|', -1)) LIKE '%GRATIS%' THEN 0
        ELSE CAST(REGEXP_REPLACE(REPLACE(SUBSTRING_INDEX(raw.raw_data, '|', -1), ',', '.'), '[^0-9.]', '') AS DECIMAL(10,2))
    END) * 0.20 AS copago_estimado

FROM raw_import_visitas raw
JOIN pacientes p 
  ON REGEXP_REPLACE(UPPER(p.nif), '[^A-Z0-9]', '') = REGEXP_REPLACE(UPPER(SUBSTRING_INDEX(raw.raw_data, '|', 1)), '[^A-Z0-9]', '');
  
  
  
-- Memoria técnica
select * from visitas;
-- Manejo de null si no tiene ni mail ni polizas:
SELECT 
    pacientes.nombre_completo,
    COALESCE(pacientes.email, 'Sin email registrado - Contactar por teléfono') AS email_contacto,
    COALESCE(seguros_pacientes.num_poliza, 'Paciente Privado (Sin Seguro)') AS estado_facturacion,
    visitas.fecha_visita,
    visitas.copago_estimado
FROM pacientes
LEFT JOIN seguros_pacientes ON pacientes.id = seguros_pacientes.id_paciente
JOIN visitas ON pacientes.id = visitas.paciente_id;

-- Saneamos las fechas. Ponemos el ignore para las fechas que no tengan tiempo, y las ponemos a 00:00
UPDATE IGNORE visitas
SET fecha_visita = COALESCE(
    STR_TO_DATE(fecha_visita, '%d/%m/%Y %H:%i'),
    STR_TO_DATE(fecha_visita, '%Y.%m.%d %H:%i'),
    STR_TO_DATE(fecha_visita, '%d-%m-%Y %H:%i'),
    STR_TO_DATE(fecha_visita, '%Y-%m-%d %H:%i')
);
