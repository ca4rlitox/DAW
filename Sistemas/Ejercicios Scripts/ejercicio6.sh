#!/bin/bash

# Usamos el separador de elementos por coma como pide el ejercicio
IFS=,

# Bucle while para leer nombre y salario del archivo
while read nombre salario
do
    echo "Hola $nombre con salario $salario"
done < empleados
