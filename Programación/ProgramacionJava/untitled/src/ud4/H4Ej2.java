package ud4;
import java.util.Scanner;
public class H4Ej2 {
    static Scanner in = new Scanner(System.in);
    static char[] tablero = new char[9];
    static char elegirFicha1;
    static char elegirFicha2;

    public static void main(String[] args) {
        //Creamos las variables necesarias
        int opcion;
        int jugador1;
        int jugador2;
        int estadisticas=0;
        int estadisticas2=0;
        //Hacemos el menú con un do while y un switch
        do {
            System.out.println("1. Jugar una partida");
            System.out.println("2. Mostrar estadísticas");
            System.out.println("3. Salir");
            System.out.println("Seleccione una opción: ");
            opcion = in.nextInt();
            switch (opcion) {
                case 1:
                    //Hacemos aquí otro do while fuera de la funcion iniciar para evitar que se reinicie la partida cada vez que da la vuelta el tablero
                    iniciar();
                    do {
                        //Dibujamos el tablero si empieza, o cada ronda
                        dibujaTablero();
                        //Pedimos movimiento al jugador 1
                        System.out.println("Introduzca movimiento (Jugador 1):\n");
                        jugador1 = in.nextInt();
                        jugador1 = jugador1 - 1;
                        //En la funcion mueveJugador1 verificamos si el movimiento con la funcion movimientoValido es válido y hacemos el movimiento
                        mueveJugador1(jugador1);
                        dibujaTablero();
                        //Comprobamos mediante la funcion ganaJugador1 si están las piezas puestas para ganar, y si lo están termina la partida y
                        //suma a la estadística una victoria para el jugador 1.
                        if (ganaJugador1()) {
                            System.out.println("Ha ganado el jugador 1!\n");
                            estadisticas++;
                            break;
                        }
                        if (!quedanCasillas()) {
                            System.out.println("Ya no quedan casillas.\n");
                            break;
                        }
                        System.out.println("Introduzca movimiento (Jugador 2):\n");
                        jugador2 = in.nextInt();
                        jugador2 = jugador2 - 1;
                        //En la funcion mueveJugador2 verificamos si el movimiento con la funcion movimientoValido es válido y hacemos el movimiento
                        mueveJugador2(jugador2);
                        //Comprobamos mediante la funcion ganaJugador2 si están las piezas puestas para ganar, y si lo están termina la partida y
                        //suma a la estadística una victoria para el jugador 2.
                        if (ganaJugador2()) {
                            dibujaTablero();
                            System.out.println("Ha ganado el jugador 2!\n");
                            estadisticas2++;
                            break;
                        }
                        // Verificamos si quedan casillas después de que el jugador2 ha puesto.
                            if (!quedanCasillas()) {
                                System.out.println("Ya no quedan casillas.\n");
                                break;
                            }
                    } while (quedanCasillas()); //Mientras queden casillas, continuar
                    break;
                case 2: //En caso de que la opcion sea dos, enseña las estadisticas con las variables.
                    System.out.println("\n Estadisticas:\nEl jugador 1 lleva "+estadisticas+" partidas ganadas, y el jugador 2 lleva "+estadisticas2+" partidas ganadas\n");
                    break;
                case 3: // Hacemos opcion de salida con break.
                    System.out.println("Has salido.");
                    break;
                default: //En caso de que se teclee otra cosa, vuelve a pedir el número.
                    System.out.println("Opción no válida. Inténtalo otra vez.\n");
            }
        } while (opcion != 3); // Mientras no se teclee en opcion 3, se repite el do while.
    }
    public static void dibujaTablero() {
        //Dibujamos el tablero
        System.out.println("-------------\n" +
                "| "+tablero[0]+" | "+tablero[1]+" | "+tablero[2]+" |\n" +
                "-------------\n" +
                "| "+tablero[3]+" | "+tablero[4]+" | "+tablero[5]+" |\n" +
                "-------------\n" +
                "| "+tablero[6]+" | "+tablero[7]+" | "+tablero[8]+" |\n" +
                "-------------");

    }
    public static void iniciar() {
        //Con un bucle for ponemos un espacio en cada array para que se vea vacio.
        char vaciar=' ';
        elegirFicha1 = ' ';
        for (int i=0;i<9;i++) {
            tablero[i] = vaciar;
        }
        //Aqui hacemos que el jugador 1 elija ficha
        in.nextLine();
        do{
            System.out.println("Elige ficha, jugador 1 entre X y O.");
            elegirFicha1 = in.nextLine().charAt(0);

            if ((elegirFicha1!='X') && (elegirFicha1!='O')) {
                System.out.println("Ficha no válida. Intentalo otra vez.");
            }
        }while((elegirFicha1!='X') && (elegirFicha1!='O'));
        if (elegirFicha1 == 'X') {
            elegirFicha2 = 'O';
        }
        else {
            elegirFicha2 = 'X';
        }
    }
    public static void mueveJugador1(int pos) {
        //Revisamos si el movimiento es válido y si no, entra en un do while hasta que lo meta en una casilla libre.
        if (!movimientoValido(pos)) {
            do {
                System.out.println("Intentalo otra vez. Movimiento inválido.");
                pos = in.nextInt();
                pos = pos - 1;
            }while (!movimientoValido(pos));
        }
        //Una vez verificado que la casilla está libre, se coloca la ficha.
        tablero[pos] = elegirFicha1;
    }
    public static void mueveJugador2(int pos) {
        //Revisamos si el movimiento es válido y si no, entra en un do while hasta que lo meta en una casilla libre.
        if (!movimientoValido(pos)) {
            do {
                System.out.println("Intentalo otra vez. Movimiento inválido.");
                pos = in.nextInt();
                pos = pos - 1;
            }while (!movimientoValido(pos));
        }
        //Una vez verificado que la casilla está libre, se coloca la ficha.
        tablero[pos] = elegirFicha2;
    }
    public static boolean movimientoValido(int pos) {
        //Con una estructura if, revisamos si donde se quiere poner la ficha está libre, si está libre devuelve true y si no, false.
        return pos >=0 && pos < 9 && tablero[pos] == ' ';
    }
    public static boolean quedanCasillas() {
        //Aquí revisamos en cada array si hay espacios vacios, si no hay espacios vacios en el array, se devuelve false para terminar la partida.
        for (int i = 0;i<9;i++) {
            if (tablero[i]==' ') {
                return true;
            }
        } return false;
        }
    public static boolean ganaJugador1() {
        if (elegirFicha1=='X') {
        //Aqui comprobamos las posiciones para ver si el jugador 1 ha ganado.
        if ((tablero[0]=='X') && (tablero[4]=='X') && (tablero[8]=='X')) {
            return true;
        }
        else if ((tablero[2]=='X') && (tablero[4]=='X') && (tablero[6]=='X')) {
            return true;
        }
        else if ((tablero[0]=='X') && (tablero[1]=='X') && (tablero[2]=='X')) {
            return true;
        }
        else if ((tablero[3]=='X') && (tablero[4]=='X') && (tablero[5]=='X')) {
            return true;
        }
        else if ((tablero[6]=='X') && (tablero[7]=='X') && (tablero[8]=='X')) {
            return true;
        }
        else if ((tablero[0]=='X') && (tablero[3]=='X') && (tablero[6]=='X')) {
            return true;
        }
        else if ((tablero[1]=='X') && (tablero[4]=='X') && (tablero[7]=='X')) {
            return true;
        }
        else if ((tablero[2]=='X') && (tablero[5]=='X') && (tablero[8]=='X')) {
            return true;
        }
        }
        if (elegirFicha1=='O') {
            if ((tablero[0]=='O') && (tablero[4]=='O') && (tablero[8]=='O')) {
                return true;
            }
            else if ((tablero[2]=='O') && (tablero[4]=='O') && (tablero[6]=='O')) {
                return true;
            }
            else if ((tablero[0]=='O') && (tablero[1]=='O') && (tablero[2]=='O')) {
                return true;
            }
            else if ((tablero[3]=='O') && (tablero[4]=='O') && (tablero[5]=='O')) {
                return true;
            }
            else if ((tablero[6]=='O') && (tablero[7]=='O') && (tablero[8]=='O')) {
                return true;
            }
            else if ((tablero[0]=='O') && (tablero[3]=='O') && (tablero[6]=='O')) {
                return true;
            }
            else if ((tablero[1]=='O') && (tablero[4]=='O') && (tablero[7]=='O')) {
                return true;
            }
            else if ((tablero[2]=='O') && (tablero[5]=='O') && (tablero[8]=='O')) {
                return true;
            }
        }
        return false;
    }
    public static boolean ganaJugador2() {
        //Aqui comprobamos las posiciones para ver si el jugador 2 ha ganado.
        if (elegirFicha2 == 'X') {
            //Aqui comprobamos las posiciones para ver si el jugador 1 ha ganado.
            if ((tablero[0] == 'X') && (tablero[4] == 'X') && (tablero[8] == 'X')) {
                return true;
            } else if ((tablero[2] == 'X') && (tablero[4] == 'X') && (tablero[6] == 'X')) {
                return true;
            } else if ((tablero[0] == 'X') && (tablero[1] == 'X') && (tablero[2] == 'X')) {
                return true;
            } else if ((tablero[3] == 'X') && (tablero[4] == 'X') && (tablero[5] == 'X')) {
                return true;
            } else if ((tablero[6] == 'X') && (tablero[7] == 'X') && (tablero[8] == 'X')) {
                return true;
            } else if ((tablero[0] == 'X') && (tablero[3] == 'X') && (tablero[6] == 'X')) {
                return true;
            } else if ((tablero[1] == 'X') && (tablero[4] == 'X') && (tablero[7] == 'X')) {
                return true;
            } else if ((tablero[2] == 'X') && (tablero[5] == 'X') && (tablero[8] == 'X')) {
                return true;
            }
        }
        if (elegirFicha2 == 'O') {
            if ((tablero[0] == 'O') && (tablero[4] == 'O') && (tablero[8] == 'O')) {
                return true;
            } else if ((tablero[2] == 'O') && (tablero[4] == 'O') && (tablero[6] == 'O')) {
                return true;
            } else if ((tablero[0] == 'O') && (tablero[1] == 'O') && (tablero[2] == 'O')) {
                return true;
            } else if ((tablero[3] == 'O') && (tablero[4] == 'O') && (tablero[5] == 'O')) {
                return true;
            } else if ((tablero[6] == 'O') && (tablero[7] == 'O') && (tablero[8] == 'O')) {
                return true;
            } else if ((tablero[0] == 'O') && (tablero[3] == 'O') && (tablero[6] == 'O')) {
                return true;
            } else if ((tablero[1] == 'O') && (tablero[4] == 'O') && (tablero[7] == 'O')) {
                return true;
            } else if ((tablero[2] == 'O') && (tablero[5] == 'O') && (tablero[8] == 'O')) {
                return true;
            }
        }
        return false;
    }
}