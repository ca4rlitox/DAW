#!/bin/bash

# Guardamos el primer parámetro (ASC o DESC) en una variable
orden=$1

# Usamos 'shift' para eliminar el primer parámetro de la lista. 
# Así, $@ ahora solo contiene las palabras a ordenar.
shift 

# Comprobamos si el orden es ASC o DESC
if [ "$orden" == "ASC" ]; then
    echo "Ordenando de forma ASCENDENTE:"
    # printf imprime cada palabra en una nueva línea, y sort las ordena alfabéticamente
    printf "%s\n" "$@" | sort
elif [ "$orden" == "DESC" ]; then
    echo "Ordenando de forma DESCENDENTE:"
    # sort -r las ordena al revés (reverse)
    printf "%s\n" "$@" | sort -r
else
    echo "Error: El primer parámetro debe ser exactamente ASC o DESC en mayúsculas."
fi
