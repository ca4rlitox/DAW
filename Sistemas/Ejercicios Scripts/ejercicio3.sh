#!/bin/bash

fichero="lista_nombres.txt"

# Vaciamos el fichero por si ya existía y tenía datos de pruebas anteriores
> "$fichero"

# Guardamos cada parámetro (los nombres) en el fichero usando un bucle
for nombre in "$@"; do
    echo "$nombre" >> "$fichero"
done

echo "=== Contenido original del fichero ==="
cat "$fichero"

echo ""
echo "=== Contenido en orden inverso ==="
# El comando 'tac' es como 'cat' pero lee el archivo de abajo hacia arriba
tac "$fichero"
