CREATE TABLE empleados(
	id_empleado smallint auto_increment,
    dni VARCHAR(9) UNIQUE NOT NULL,
    salario FLOAT DEFAULT 2000,
    estado VARCHAR(8) DEFAULT 'ACTIVO',
    CONSTRAINT pk_idempleado PRIMARY KEY(id_empleado),
    CONSTRAINT chk_estado CHECK (estado = 'ACTIVO' OR estado = 'INACTIVO')
    );
    