#!/bin/bash
# Usamos el comando exacto que pide el ejercicio
grep '^[AEIOUaeiou]' $1 > $2

echo "Se han filtrado las palabras de $1 y se han guardado en $2"
