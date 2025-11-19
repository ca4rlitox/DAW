package ud4;

import java.util.Scanner;

public class tresEnRaya {
    static Scanner in = new Scanner(System.in);
    static char[] tablero = new char[9];

    public static void main(String[] args) {
        int opcion;
        int jugador1;
        int jugador2;
        int estadisticas=0;
        int estadisticas2=0;

        do {
            System.out.println("1. Jugar una partida");
            System.out.println("2. Mostrar estadísticas");
            System.out.println("3. Salir");
            System.out.println("Seleccione una opción: ");
            opcion = in.nextInt();

            switch (opcion) {

                case 1:
                    iniciar();
                    do {

                        dibujaTablero();
                        System.out.println("Introduzca movimiento (Jugador 1):\n");
                        jugador1 = in.nextInt();
                        mueveJugador1(jugador1 - 1);
                        dibujaTablero();

                        if (ganaJugador1()) {
                            System.out.println("Ha ganado el jugador 1!\n");
                            estadisticas++;
                            break;
                        }

                        System.out.println("Introduzca movimiento (Jugador 2):\n");
                        jugador2 = in.nextInt();
                        mueveJugador2(jugador2 - 1);
                        if (ganaJugador2()) {
                            dibujaTablero();
                            System.out.println("Ha ganado el jugador 2!\n");
                            estadisticas2++;
                            break;
                        }


                    } while (quedanCasillas());

                    break;

                case 2:
                    System.out.println("\n Estadisticas:\nEl jugador 1 lleva "+estadisticas+" partidas ganadas, y el jugador 2 lleva "+estadisticas2+" partidas ganadas\n");
                    break;

                case 3:
                    System.out.println("Has salido.");
                    break;

                default:
                    System.out.println("Opción no válida. Inténtalo otra vez.\n");

            }

        } while (opcion != 3);


    }

    public static void dibujaTablero() {

        System.out.println("-------------\n" +
                "| "+tablero[0]+" | "+tablero[1]+" | "+tablero[2]+" |\n" +
                "-------------\n" +
                "| "+tablero[3]+" | "+tablero[4]+" | "+tablero[5]+" |\n" +
                "-------------\n" +
                "| "+tablero[6]+" | "+tablero[7]+" | "+tablero[8]+" |\n" +
                "-------------");

    }


    public static void iniciar() {

        char vaciar=' ';
        for (int i=0;i<9;i++) {
            tablero[i] = vaciar;
        }

    }

    public static void mueveJugador1(int pos) {

        movimientoValido(pos);
        tablero[pos] = 'X';

    }


    public static void mueveJugador2(int pos) {

        do {
            movimientoValido(pos);
            tablero[pos] = 'O';
        }while(!movimientoValido(pos));
    }

    public static boolean movimientoValido(int pos) {
        int validacion;
        if ((tablero[pos]=='X') || (tablero[pos]=='O')) {
            do {

                System.out.println("Movimiento no válido. Inténtalo otra vez");
                pos = in.nextInt();
                pos = pos - 1;
                validacion = pos;

            } while ((tablero[pos] == 'X') || (tablero[pos] == 'O'));

        }

        return false;
    }

    public static boolean quedanCasillas() {

        for (int i = 0;i<9;i++) {
            if (tablero[i]==' ') {
                return true;
            }
        }
                return false;

        }


    public static boolean ganaJugador1() {
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

        return false;

    }

    public static boolean ganaJugador2() {

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

        return false;

    }

}