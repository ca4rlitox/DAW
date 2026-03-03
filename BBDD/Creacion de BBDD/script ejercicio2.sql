DROP DATABASE IF EXISTS ejercicio2;
CREATE DATABASE ejercicio2;
DROP DATABASE IF EXISTS ejercicio2;
USE ejercicio2;

SET FOREIGN_KEY_CHECKS = 0;

CREATE TABLE investigador(
	id_investigador SMALLINT UNSIGNED AUTO_INCREMENT UNIQUE,
	id_laboratorio SMALLINT UNIQUE,
    nombre_investigador VARCHAR(60) NOT NULL,
    CONSTRAINT pk_id_investigador PRIMARY KEY(id_investigador),
    CONSTRAINT fk_id_laboratorio FOREIGN KEY(id_laboratorio)
    REFERENCES laboratorio(id_laboratorio)
    ON DELETE RESTRICT ON UPDATE CASCADE
    );
    
CREATE TABLE laboratorio(
	id_laboratorio SMALLINT UNSIGNED AUTO_INCREMENT UNIQUE,
    nombre_laboratorio VARCHAR(60),
    id_investigador_principal SMALLINT UNSIGNED UNIQUE,
    CONSTRAINT pk_id_laboratorio PRIMARY KEY(id_laboratorio),
    CONSTRAINT fk_id_investigador_principal FOREIGN KEY(id_investigador_principal)
    REFERENCES investigador(id_investigador)
    ON DELETE RESTRICT ON UPDATE CASCADE
    );
    
    SET FOREIGN_KEY_CHECKS = 1;