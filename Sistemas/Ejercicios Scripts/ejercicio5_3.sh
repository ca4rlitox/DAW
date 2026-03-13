#!/bin/bash
dirs=0
archs=0

for param in "$@"; do
    if [ -d "$param" ]; then
        ((dirs++))
    elif [ -f "$param" ]; then
        ((archs++))
    fi
done

echo "Se han pasado $# parámetros en total."
echo "Directorios encontrados: $dirs"
echo "Archivos encontrados: $archs"
