#!/bin/bash
opcion=0
while [ $opcion -ne 5 ];
do
    echo "1.Crear directorio"
    echo "2.Borrar directorio"
    echo "3.Crear fichero"
    echo "4.Borrar fichero"
    echo "5.Salir"
    read opcion

    case $opcion in
        1)
            echo "Escribe el nombre del directorio que quieres crear:"
            read nombreDirectorio
            mkdir $nombreDirectorio
            ;;
        2)
            echo "Escribe el nombre del directorio que quieres borrar:"
            read nombreDirectorio
            rmdir $nombreDirectorio
            ;;
        3)
            echo "Escribe el nombre del fichero que quieres crear:"
            read nombreFichero
            touch $nombreFichero
            ;;
        4)
            echo "Escribe el nombre del fichero que quieres borrar:"
            read nombreFichero
            rm $nombreFichero
            ;;
        5)
            echo "Saliendo..."
            ;;
        *)
            echo "Invalid choice. Please try again."
            ;;
    esac
done