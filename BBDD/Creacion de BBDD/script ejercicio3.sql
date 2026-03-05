DROP DATABASE IF EXISTS gestion_proyectos;
CREATE DATABASE gestion_proyectos;
USE gestion_proyectos;

CREATE TABLE empleados(
	id_empleado smallint UNSIGNED auto_increment,
    dni VARCHAR(9) NOT NULL UNIQUE,
    salario FLOAT DEFAULT 1200,
    estado ENUM('ACTIVO','INACTIVO'),
    CONSTRAINT pk_idempleado PRIMARY KEY(id_empleado),
    CONSTRAINT chk_salario CHECK (salario >=0)
    );
    
CREATE TABLE departamentos(
	id_departamento SMALLINT UNSIGNED auto_increment NOT NULL UNIQUE,
    codigo_dpto CHAR(5) UNIQUE NOT NULL,
    nombre VARCHAR(40) NOT NULL,
    presupuesto FLOAT NOT NULL,
    CONSTRAINT pk_id_departamento PRIMARY KEY(id_departamento),
    CONSTRAINT chk_presupuesto_negativo CHECK (presupuesto >=0)
    );
    
CREATE TABLE proyectos(
	id_proyecto SMALLINT UNSIGNED AUTO_INCREMENT,
    nombre VARCHAR(40) UNIQUE NOT NULL,
    id_departamento SMALLINT UNSIGNED NOT NULL,
    fecha_inicio DATE NOT NULL,
    fecha_fin DATE,
    CONSTRAINT pk_id_proyecto PRIMARY KEY(id_proyecto),
    CONSTRAINT chk_fecha_fin_anterior_a_inicio CHECK (fecha_fin > fecha_inicio),
    CONSTRAINT fk_id_departamento FOREIGN KEY(id_departamento)
    REFERENCES departamentos(id_departamento)
    ON DELETE RESTRICT ON UPDATE CASCADE
);

CREATE TABLE asignaciones(
	id_empleado SMALLINT UNSIGNED UNIQUE,
    id_proyecto SMALLINT UNSIGNED,
    horas_asignadas SMALLINT UNSIGNED DEFAULT 0,
    CONSTRAINT fk_id_empleado FOREIGN KEY(id_empleado)
    REFERENCES empleados(id_empleado)
	ON DELETE RESTRICT ON UPDATE CASCADE,
    CONSTRAINT fk_id_proyecto FOREIGN KEY(id_proyecto)
    REFERENCES proyectos(id_proyecto)
	);