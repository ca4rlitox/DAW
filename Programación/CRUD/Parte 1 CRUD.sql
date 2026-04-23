-- DDL
CREATE DATABASE bd_clientes;
use bd_clientes;

-- DML
CREATE TABLE clientes(
	id varchar(10),
    nombre varchar(20),
    edad int
);

INSERT INTO clientes values ("123a","Paco",10);

select concat("nombre",nombre),1.2*edad from clientes;