-- Revisar los problemas que hay
SELECT * FROM clientes;

-- Eliminar espacios residuales
SET SQL_SAFE_UPDATES = 0;
UPDATE clientes SET nombre_completo = TRIM(nombre_completo);
SET SQL_SAFE_UPDATES = 1;

-- Replace para cambiar las cosas
select * from clientes;
-- 		BBDD		columna	reemplazar columna con '.con' con '.con'
UPDATE clientes SET nombre_completo = REPLACE(nombre_completo,'  ',' ');
SET SQL_SAFE_UPDATES = 1;

-- Estandarización de números de telefono para la tabla clientes columna telefono
-- (Eliminar guiones, espacios...)
-- CAMBIOS TEMPORALES: staging (tablas o columnas intermedias) y transacciones.
START transaction; -- A partir de ahora todos los cambios son temporales. Hasta el commit (hacerlos definitivos) o el rollback (deshacerlos).
SET SQL_SAFE_UPDATES = 0;
UPDATE clientes SET email = REPLACE(email,'@.','@');
UPDATE clientes SET email = REPLACE(email,'-','');
SET SQL_SAFE_UPDATES = 1;
COMMIT;
SELECT * FROM clientes;
-- Substring extrae una porción específica de un texto o cadena de caracteres SUBSTRING(columna,dondeempieza,dondeacaba)

-- Estados
start transaction;
select * from productos;
-- staging (columna intermedia) con ejemplo "precio_procesado"
	alter table productos
		add column precio_procesado VARCHAR(50);
UPDATE productos SET precio_procesado = REPLACE(precio,' ','');
