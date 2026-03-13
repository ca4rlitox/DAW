#!/bin/bash

# Bucle externo: recorre los números del 1 al 10 para las tablas
for i in {1..10}; do
    echo "=== Tabla del $i ==="
    
    # Bucle interno: multiplica el número actual ($i) por los números del 1 al 10 ($j)
    for j in {1..10}; do
        resultado=$((i * j))
        echo "$i x $j = $resultado"
    done
    
    # Un pequeño salto de línea para que se vea más ordenado
    echo ""
done
