-- ==============================================================================
-- PROYECTO: SANEAMIENTO MASIVO Y BLINDAJE DE BIG DATA (LOGÍSTICA GLOBAL 4.0)
-- ==============================================================================
use logistica_global;
SELECT '>>> INICIANDO PROCESO DE SANEAMIENTO Y BLINDAJE...' AS Mensaje;

SET autocommit=0;
SET foreign_key_checks=0;

-- 1. FASE DE EXPANSIÓN: TABLAS DE STAGING
CREATE TABLE IF NOT EXISTS almacenes_staging LIKE almacenes;
TRUNCATE TABLE almacenes_staging;
INSERT INTO almacenes_staging SELECT * FROM almacenes;

CREATE TABLE IF NOT EXISTS empleados_staging LIKE empleados;
TRUNCATE TABLE empleados_staging;
INSERT INTO empleados_staging SELECT * FROM empleados;

CREATE TABLE IF NOT EXISTS vehiculos_staging LIKE vehiculos;
TRUNCATE TABLE vehiculos_staging;
INSERT INTO vehiculos_staging SELECT * FROM vehiculos;

CREATE TABLE IF NOT EXISTS clientes_staging LIKE clientes;
TRUNCATE TABLE clientes_staging;
INSERT INTO clientes_staging SELECT * FROM clientes;

CREATE TABLE IF NOT EXISTS proveedores_staging LIKE proveedores;
TRUNCATE TABLE proveedores_staging;
INSERT INTO proveedores_staging SELECT * FROM proveedores;

CREATE TABLE IF NOT EXISTS mantenimientos_flota_staging LIKE mantenimientos_flota;
TRUNCATE TABLE mantenimientos_flota_staging;
INSERT INTO mantenimientos_flota_staging SELECT * FROM mantenimientos_flota;

CREATE TABLE IF NOT EXISTS envios_staging LIKE envios;
TRUNCATE TABLE envios_staging;
INSERT INTO envios_staging SELECT * FROM envios;

CREATE TABLE IF NOT EXISTS incidencias_staging LIKE incidencias;
TRUNCATE TABLE incidencias_staging;
INSERT INTO incidencias_staging SELECT * FROM incidencias;

-- 3. UPDATES: LIMPIEZA DIMENSIONAL Y FINANCIERA (EXTRACCIÓN NUMÉRICA)
UPDATE empleados_staging SET salario_base_sucio = CAST(REPLACE(REGEXP_REPLACE(salario_base_sucio, '[^0-9.,-]', ''), ',', '.') AS DECIMAL(10,2));
UPDATE almacenes_staging SET capacidad_m3 = CAST(REPLACE(REGEXP_REPLACE(capacidad_m3, '[^0-9.,]', ''), ',', '.') AS DECIMAL(10,2));
UPDATE vehiculos_staging SET capacidad_carga_kg = CAST(REPLACE(REGEXP_REPLACE(capacidad_carga_kg, '[^0-9.,]', ''), ',', '.') AS DECIMAL(10,2));
UPDATE clientes_staging SET limite_credito_sucio = CAST(REPLACE(REGEXP_REPLACE(limite_credito_sucio, '[^0-9.,-]', ''), ',', '.') AS DECIMAL(10,2));
UPDATE envios_staging SET peso_kg_bruto = CAST(REPLACE(REGEXP_REPLACE(peso_kg_bruto, '[^0-9.,]', ''), ',', '.') AS DECIMAL(10,2)), importe_envio = CAST(REPLACE(REGEXP_REPLACE(importe_envio, '[^0-9.,-]', ''), ',', '.') AS DECIMAL(10,2)), ruta_distancia_km = CAST(REPLACE(REGEXP_REPLACE(ruta_distancia_km, '[^0-9.,]', ''), ',', '.') AS DECIMAL(10,2));
UPDATE incidencias_staging SET coste_asociado_sucio = CAST(REPLACE(REGEXP_REPLACE(coste_asociado_sucio, '[^0-9.,-]', ''), ',', '.') AS DECIMAL(10,2));

-- 4. DESDUPLICACIÓN ESTRUCTURAL (WINDOW FUNCTIONS CTE)
WITH CTE_Almacen AS (SELECT id, ROW_NUMBER() OVER(PARTITION BY cod_almacen ORDER BY id) as rn FROM almacenes_staging)
DELETE FROM almacenes_staging WHERE id IN (SELECT id FROM CTE_Almacen WHERE rn > 1);

WITH CTE_Clientes AS (SELECT id, ROW_NUMBER() OVER(PARTITION BY cif_nif ORDER BY id) as rn FROM clientes_staging)
DELETE FROM clientes_staging WHERE id IN (SELECT id FROM CTE_Clientes WHERE rn > 1);

WITH CTE_Envios AS (SELECT id, ROW_NUMBER() OVER(PARTITION BY tracking_number ORDER BY id) as rn FROM envios_staging)
DELETE FROM envios_staging WHERE id IN (SELECT id FROM CTE_Envios WHERE rn > 1);

-- 5. ERRADICACIÓN DE FANTASMAS Y ORfandAD (LEFT JOIN DELETION)
DELETE FROM empleados_staging WHERE nif_nie IS NULL OR TRIM(nif_nie) = '';
DELETE FROM clientes_staging WHERE cif_nif IS NULL OR TRIM(cif_nif) = '';
DELETE FROM vehiculos_staging WHERE matricula IS NULL OR TRIM(matricula) = '';
DELETE FROM envios_staging WHERE tracking_number IS NULL OR TRIM(tracking_number) = '';

DELETE e FROM empleados_staging e LEFT JOIN almacenes_staging a ON e.almacen_id = a.id WHERE a.id IS NULL;
DELETE en FROM envios_staging en LEFT JOIN clientes_staging c ON en.cliente_id = c.id WHERE c.id IS NULL;
DELETE en FROM envios_staging en LEFT JOIN vehiculos_staging v ON en.vehiculo_id = v.id WHERE v.id IS NULL;
DELETE i FROM incidencias_staging i LEFT JOIN envios_staging en ON i.envio_id = en.id WHERE en.id IS NULL;
DELETE mf FROM mantenimientos_flota_staging mf LEFT JOIN vehiculos_staging v ON mf.vehiculo_id = v.id WHERE v.id IS NULL;

-- Purgado de anomalías antes de imponer los CHECK
DELETE FROM empleados_staging WHERE nif_nie NOT REGEXP '^[0-9]{7}[A-Z]$';
DELETE FROM vehiculos_staging WHERE matricula NOT REGEXP '^[0-9]{4}{3}$|^[A-Z]{1,2}[0-9]{4}[A-Z]{1,2}$';

-- 6. FASE DE BLINDAJE: CHECKS Y CONTROL DE DOMINIOS (DATA HARDENING)
ALTER TABLE almacenes_staging 
    MODIFY cod_almacen VARCHAR(50) NOT NULL,
    ADD CONSTRAINT uq_alm UNIQUE (cod_almacen),
    ADD CONSTRAINT chk_capacidad CHECK (CAST(capacidad_m3 AS DECIMAL) >= 0);

ALTER TABLE empleados_staging 
    MODIFY nif_nie VARCHAR(20) NOT NULL,
    MODIFY salario_base_sucio DECIMAL(10,2) NOT NULL DEFAULT 0.00,
    ADD CONSTRAINT uq_emp_nif UNIQUE (nif_nie),
    ADD CONSTRAINT fk_emp_alm FOREIGN KEY (almacen_id) REFERENCES almacenes_staging(id) ON DELETE RESTRICT,
    ADD CONSTRAINT chk_emp_nif CHECK (nif_nie REGEXP '^[0-9]{7}[A-Z]$'),
    ADD CONSTRAINT chk_emp_salario CHECK (salario_base_sucio >= 0);

ALTER TABLE vehiculos_staging 
    MODIFY matricula VARCHAR(20) NOT NULL,
    ADD CONSTRAINT uq_veh_mat UNIQUE (matricula),
    ADD CONSTRAINT chk_veh_mat CHECK (matricula REGEXP '^[0-9]{4}{3}$|^[A-Z]{1,2}[0-9]{4}[A-Z]{1,2}$');

ALTER TABLE clientes_staging 
    MODIFY cif_nif VARCHAR(20) NOT NULL,
    ADD CONSTRAINT uq_cli_cif UNIQUE (cif_nif);

ALTER TABLE proveedores_staging 
    MODIFY cif_prov VARCHAR(50) NOT NULL,
    ADD CONSTRAINT uq_prov_cif UNIQUE (cif_prov);

ALTER TABLE envios_staging 
    MODIFY tracking_number VARCHAR(100) NOT NULL,
    MODIFY cliente_id INT NOT NULL,
    MODIFY vehiculo_id INT NOT NULL,
    ADD CONSTRAINT uq_env_trk UNIQUE (tracking_number),
    ADD CONSTRAINT fk_env_cli FOREIGN KEY (cliente_id) REFERENCES clientes_staging(id) ON DELETE RESTRICT,
    ADD CONSTRAINT fk_env_veh FOREIGN KEY (vehiculo_id) REFERENCES vehiculos_staging(id) ON DELETE RESTRICT;

ALTER TABLE incidencias_staging 
    MODIFY envio_id INT NOT NULL,
    ADD CONSTRAINT fk_inc_env FOREIGN KEY (envio_id) REFERENCES envios_staging(id) ON DELETE CASCADE;

ALTER TABLE mantenimientos_flota_staging 
    MODIFY vehiculo_id INT NOT NULL,
    ADD CONSTRAINT fk_man_veh FOREIGN KEY (vehiculo_id) REFERENCES vehiculos_staging(id) ON DELETE CASCADE;

-- 7. FASE DE CONTRACCIÓN (RENAME ATÓMICO)
RENAME TABLE almacenes TO almacenes_backup, almacenes_staging TO almacenes;
RENAME TABLE clientes TO clientes_backup, clientes_staging TO clientes;
RENAME TABLE vehiculos TO vehiculos_backup, vehiculos_staging TO vehiculos;
RENAME TABLE empleados TO empleados_backup, empleados_staging TO empleados;
RENAME TABLE proveedores TO proveedores_backup, proveedores_staging TO proveedores;
RENAME TABLE envios TO envios_backup, envios_staging TO envios;
RENAME TABLE incidencias TO incidencias_backup, incidencias_staging TO incidencias;
RENAME TABLE mantenimientos_flota TO mantenimientos_flota_backup, mantenimientos_flota_staging TO mantenimientos_flota;

SET foreign_key_checks=1;
COMMIT;

SELECT '>>> SANEAMIENTO COMPLETADO. Integridad Referencial Restaurada.' AS Mensaje;
-- ==============================================================================