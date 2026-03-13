DROP DATABASE IF EXISTS gestion_universidad;
CREATE DATABASE gestion_universidad;
USE gestion_universidad;

CREATE TABLE facultades(
	id_facultad SMALLINT AUTO_INCREMENT NOT NULL,
    codigo CHAR(4) UNIQUE NOT NULL,
    nombre VARCHAR(30) UNIQUE NOT NULL,
    id_decano SMALLINT,
    CONSTRAINT pk_id_facultad PRIMARY KEY (id_facultad)
);

CREATE TABLE profesores(
	id_profesor SMALLINT AUTO_INCREMENT NOT NULL,
    NIF CHAR(9) UNIQUE NOT NULL,
    nombre_completo VARCHAR(64) NOT NULL,
    salario FLOAT NOT NULL DEFAULT 2000,
    id_facultad SMALLINT NOT NULL,
    CONSTRAINT pk_id_profe PRIMARY KEY(id_profesor),
    CONSTRAINT fk_id_facultad FOREIGN KEY(id_facultad)
    REFERENCES facultades(id_facultad),
    CONSTRAINT chk_salario_mayor_0 CHECK (salario > 0)
);

ALTER TABLE facultades
	ADD CONSTRAINT fk_id_profesor FOREIGN KEY (id_decano)
		REFERENCES profesores(id_profesor);
        
CREATE TABLE grados(
	id_grado SMALLINT auto_increment NOT NULL,
    nombre VARCHAR(32) NOT NULL UNIQUE,
    id_facultad SMALLINT NOT NULL,
    CONSTRAINT pk_id_grado PRIMARY KEY(id_grado),
    CONSTRAINT fk_id_facultado FOREIGN KEY(id_facultad)
    REFERENCES facultades(id_facultad));
    
CREATE TABLE asignaturas(
	id_asignatura SMALLINT auto_increment NOT NULL,
    codigo_asig VARCHAR(10) UNIQUE NOT NULL,
    nombre VARCHAR(32) NOT NULL,
    creditos TINYINT DEFAULT 6,
    CONSTRAINT pk_id_asignaturas PRIMARY KEY(id_asignatura),
    CONSTRAINT chk_creditos CHECK (creditos >= 3)
);

CREATE TABLE imparten(
	id_profesor SMALLINT NOT NULL,
	id_asignatura SMALLINT NOT NULL,
    tipo_grupo ENUM('TEORIA','PRACTICA') DEFAULT 'TEORIA',
	CONSTRAINT fk_id_profesor_imparten PRIMARY KEY(id_profesor,id_asignatura)
    );
    
ALTER TABLE imparten
    ADD CONSTRAINT fk_id_profesor_imparten FOREIGN KEY(id_profesor)
		REFERENCES profesores(id_profesor)
        ON DELETE CASCADE,
	ADD CONSTRAINT fk_id_asignatura_imparten FOREIGN KEY(id_asignatura)
		REFERENCES asignaturas(id_asignatura)
        ON DELETE CASCADE;
        
INSERT INTO `gestion_universidad`.`facultades`
(`id_facultad`,
`codigo`,
`nombre`,
`id_decano`)
VALUES
(1,1,'morosi',1);

INSERT INTO `gestion_universidad`.`profesores`
(`id_profesor`,
`NIF`,
`nombre_completo`,
`salario`,
`id_facultad`)
VALUES
(1,'51180393B','MORO SANCHEZ',2500,1)