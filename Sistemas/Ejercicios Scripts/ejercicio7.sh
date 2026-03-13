#!/bin/bash

archivo="lista_empleados.txt"
# Nos aseguramos de que el fichero exista antes de empezar
touch "$archivo"

while true; do
    echo "=== MENÚ DE EMPLEADOS ==="
    echo "1. Mostrar sólo empleados"
    echo "2. Alta de empleados"
    echo "3. Baja de todos los empleados"
    echo "4. Bloquear todos los empleados"
    echo "5. Salir"
    read -p "Elige una opción: " opcion

    case $opcion in
        1)
            echo "--- Lista actual ---"
            if [ -r "$archivo" ]; then
                cat "$archivo"
            else
                echo "Error: El fichero está bloqueado y no se puede leer."
            fi
            echo "--------------------"
            ;;
        2)
            if [ -w "$archivo" ]; then
                read -p "Introduce el nombre del empleado: " nombre
                read -p "Introduce el salario de $nombre: " salario
                echo "$nombre, $salario" >> "$archivo"
                echo "Empleado registrado con éxito."
            else
                echo "Error: El fichero está bloqueado y no se puede escribir."
            fi
            ;;
        3)
            if [ -w "$archivo" ]; then
                > "$archivo"
                echo "Se ha dado de baja a todos los empleados (fichero vaciado)."
            else
                echo "Error: El fichero está bloqueado."
            fi
            ;;
        4)
            chmod 000 "$archivo"
            echo "Fichero bloqueado. Ya no se puede leer ni escribir en él."
            ;;
        5)
            echo "Saliendo del gestor de empleados..."
            break
            ;;
        *)
            echo "Opción no válida. Intenta de nuevo."
            ;;
    esac
    echo "" # Salto de línea estético
done
