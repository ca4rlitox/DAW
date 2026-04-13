use logistica_global;

select * from almacenes order by id ASC;
/* Tabla almacenes:
- Eliminar _ en cod_almacen y eliminar duplicados.
- En nombre sucursal eliminar todos los registros que no cumplan el estandar: Sucursal xxx
- En ciudad_ubicacion sustituir VLC por Valencia, Barna por Barcelona...
- Eliminar los registros que no tengan numeros de contacto.
- En capacidad_m3, sustituir metros cúbicos por m3.
- En tipo_gestión, hacer un enum solo con Propia o Subcontrata. El resto de valores que no lo cumplan, se eliminan.
- Separar ubicacion geografica en dos tablas, una con la latitud y otra con la longitud, eliminando los demás registros que no lo tengan.
*/
SET SQL_SAFE_UPDATES = 0;

begin;
UPDATE almacenes SET cod_almacen = REPLACE(cod_almacen, '_', ''); -- Eliminamos _ en cod_almacen

DELETE a1 FROM almacenes a1
INNER JOIN almacenes a2 
WHERE a1.id > a2.id AND a1.cod_almacen = a2.cod_almacen; -- Eliminamos los duplicados en cod_almacen y mantenemos los que tengan el id mas bajo.

UPDATE almacenes
SET ciudad_ubicacion = CASE 
    WHEN ciudad_ubicacion = 'VLC' THEN 'Valencia'
    WHEN ciudad_ubicacion = 'Barna' THEN 'Barcelona'
    ELSE ciudad_ubicacion
END; -- Sustituimos VLC y Barna por su nombre real.

DELETE FROM almacenes WHERE tel_contacto IS NULL OR TRIM(tel_contacto) = ''; -- Eliminamos los registros que no tengan numero de contacto

UPDATE almacenes SET capacidad_m3 = REPLACE(capacidad_m3, 'metros cúbicos', 'm3'); -- Cambiamos la expresión metros cúbicos por m3

DELETE FROM almacenes WHERE UPPER(tipo_gestion) NOT IN ('PROPIA', 'SUBCONTRATA'); -- Eliminamos los registros que no tengan en tipo_gestion Propia o subcontrata.

-- Modificamos tipo_gestion para que siga un estandar con la primera en mayúscula
UPDATE almacenes SET tipo_gestion = 'Propia' WHERE UPPER(tipo_gestion) = 'PROPIA';
UPDATE almacenes SET tipo_gestion = 'Subcontrata' WHERE UPPER(tipo_gestion) = 'SUBCONTRATA';

ALTER TABLE almacenes MODIFY COLUMN tipo_gestion ENUM('Propia', 'Subcontrata'); -- Cambiamos el tipo de dato de tipo_gestion para que sea un ENUM

ALTER TABLE almacenes ADD COLUMN latitud VARCHAR(50), ADD COLUMN longitud VARCHAR(50); -- Añadimos columnas de longitud y latitud

UPDATE almacenes SET latitud = TRIM(SUBSTRING_INDEX(SUBSTRING_INDEX(ubicacion_geografica, '|', 1), ':', -1)), longitud = TRIM(SUBSTRING_INDEX(ubicacion_geografica, ':', -1)); -- Separamos latitud y longitud en dos columnas diferentes.

ALTER TABLE almacenes DROP COLUMN ubicacion_geografica; -- Eliminamos ubicacion_geografica tras haber separado en columnas diferentes la latitud y la longitud

ALTER TABLE almacenes
ADD CONSTRAINT chk_capacidad_m3 CHECK (capacidad_m3 LIKE '%m3'); -- Check de que tiene que acabar en m3

ALTER TABLE almacenes
ADD CONSTRAINT chk_cod_almacen CHECK (cod_almacen LIKE 'ALM-%%%'); -- Indicamos como tiene que empezar cod_almacen

select * from clientes;
begin;
rollback;
commit;

alter table clientes
DROP COLUMN direccion_fiscal;
alter table clientes
DROP COLUMN cp_postal;
alter table clientes
DROP COLUMN email_facturacion;
alter table clientes
DROP COLUMN activo;
alter table clientes
DROP COLUMN tipo_cliente; -- Eliminamos tablas sin uso

UPDATE clientes SET 
    limite_credito_sucio = 
    CASE 
        -- Si contiene USD, limpiamos, multiplicamos y luego pegamos el '€'
        WHEN limite_credito_sucio LIKE '%USD%' THEN 
            CONCAT(ROUND(CAST(REGEXP_REPLACE(limite_credito_sucio, '[^0-9.]', '') AS DECIMAL(10,2)) * 0.92, 2))
            
        -- Si ya tiene €, limpiamos el texto sobrante y nos aseguramos que acabe en '€' uniforme
        WHEN limite_credito_sucio LIKE '%€%' THEN 
            CONCAT(REGEXP_REPLACE(limite_credito_sucio, '[^0-9.]', ''))
            
        -- Para el resto, simplemente añadimos el símbolo 
        ELSE 
            CONCAT(REGEXP_REPLACE(limite_credito_sucio, '[^0-9.]', ''))
    END; -- cambiamos el formato de los dineros para que este todo en euros
    
UPDATE clientes SET 
    fecha_alta_cliente = DATE_FORMAT(
        CASE 
            WHEN fecha_alta_cliente LIKE '__/__/__' THEN STR_TO_DATE(fecha_alta_cliente, '%d/%m/%y')
            WHEN fecha_alta_cliente LIKE '__/__/____' THEN STR_TO_DATE(fecha_alta_cliente, '%d/%m/%Y')
            WHEN fecha_alta_cliente LIKE '__-__-____' THEN STR_TO_DATE(fecha_alta_cliente, '%d-%m-%Y')
            WHEN fecha_alta_cliente LIKE '____/__/__' THEN STR_TO_DATE(fecha_alta_cliente, '%Y/%m/%d')
            WHEN fecha_alta_cliente LIKE '____-__-__' THEN STR_TO_DATE(fecha_alta_cliente, '%Y-%m-%d')
            WHEN fecha_alta_cliente LIKE '__-__-__' THEN STR_TO_DATE(fecha_alta_cliente, '%y-%m-%d')
            ELSE fecha_alta_cliente 
        END, 
    '%Y/%m/%d'); -- Corregimos el formato de las fechas
    
ALTER TABLE clientes 
MODIFY COLUMN fecha_alta_cliente DATE; -- Cambiamos el tipo de dato

ALTER TABLE clientes 
RENAME COLUMN limite_credito_sucio TO limite_credito_en_eur; -- Cambiamos el nombre de la columna credito.

ALTER TABLE clientes
MODIFY COLUMN limite_credito_en_eur DECIMAL(10,2); -- Cambiamos el tipo de dato del limite de credito para poder operar sobre ellas

show tables;
select * from empleados;
UPDATE empleados SET nif_nie = REPLACE(nif_nie, ' ',''); -- Eliminamos espacios de la columna nif_nie

UPDATE empleados SET 
    f_alta = DATE_FORMAT(
        CASE 
            WHEN f_alta LIKE '__/__/__' THEN STR_TO_DATE(f_alta, '%d/%m/%y')
            WHEN f_alta LIKE '__/__/____' THEN STR_TO_DATE(f_alta, '%d/%m/%Y')
            WHEN f_alta LIKE '__-__-____' THEN STR_TO_DATE(f_alta, '%d-%m-%Y')
            WHEN f_alta LIKE '____/__/__' THEN STR_TO_DATE(f_alta, '%Y/%m/%d')
            WHEN f_alta LIKE '____-__-__' THEN STR_TO_DATE(f_alta, '%Y-%m-%d')
            WHEN f_alta LIKE '__-__-__' THEN STR_TO_DATE(f_alta, '%y-%m-%d')
            ELSE f_alta 
        END, 
    '%Y/%m/%d'); -- Corregimos el formato de las fechas
    
SELECT f_alta from empleados;