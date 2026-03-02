#!/bin/bash

for ((i=0; i<=10; i++))
do
    echo "Tabla del $i"
    for ((j=0; j<=10; j++))
    do
        echo "$i x $j = $(($i*$j))"
    done
done