#!/bin/bash
opcion=0
while [ $opcion -ne 5 ]; do
    echo " MENÚ "
    echo "1. Crear directorio"
    echo "2. Borrar directorio"
    echo "3. Crear fichero"
    echo "4. Borrar fichero"
    echo "5. Salir"
    read -p "Elige una opción: " opcion

    case $opcion in
        1) read -p "Nombre del directorio a crear: " dir; mkdir "$dir" ;;
        2) read -p "Nombre del directorio a borrar: " dir; rmdir "$dir" ;;
        3) read -p "Nombre del fichero a crear: " arch; touch "$arch" ;;
        4) read -p "Nombre del fichero a borrar: " arch; rm "$arch" ;;
        5) echo "Saliendo del programa..." ;;
        *) echo "Opción no válida." ;;
    esac
done
