package ud4;

import java.util.Scanner;

public class tresEnRaya {
    static Scanner in = new Scanner(System.in);
    static char[] tablero = new char[9];

    public static void main(String[] args) {
        int opcion;
        int jugador1;
        int jugador2;

        do {
            System.out.println("1. Jugar una partida");
            System.out.println("2. Mostrar estadísticas");
            System.out.println("3. Salir");
            System.out.println("Seleccione una opción: ");
            opcion = in.nextInt();

            switch (opcion) {

                case 1:
                    dibujaTablero();
                    iniciar();
                    System.out.println("Introduzca movimiento (Jugador 1):\n");
                    jugador1 = in.nextInt();
                    mueveJugador1(jugador1);
                    dibujaTablero();


                    break;

                case 2:

                    break;


                default:
                    System.out.println("Opción no válida. Inténtalo otra vez.");

            }

        } while (opcion != 3);


    }

    public static void dibujaTablero() {

        System.out.println("-------------\n" +
                "| 1 | 2 | 3 |\n" +
                "-------------\n" +
                "| 4 | 5 | 6 |\n" +
                "-------------\n" +
                "| 7 | 8 | 9 |\n" +
                "-------------");

    }


    public static void iniciar() {

        System.out.print("-------------\n" +
                "| "+tablero[0]+" | "+tablero [1]+" | "+tablero [2]+" |\n" +
                "-------------\n" +
                "| "+tablero[3]+" | "+tablero[4]+" | "+tablero[5]+" |\n" +
                "-------------\n" +
                "| "+tablero[6]+" | "+tablero[7]+" | "+tablero[8]+" |\n" +
                "-------------");

    }

    public static void mueveJugador1(int pos) {

        if (pos==0) {
            tablero[0] = 'x';
        }
        if (pos==1) {
            tablero[1] = 'x';
        }
        if (pos==2) {
            tablero[2] = 'x';
        }
        if (pos==3) {
            tablero[3] = 'x';
        }
        if (pos==4) {
            tablero[4] = 'x';
        }
        if (pos==5) {
            tablero[5] = 'x';
        }
        if (pos==6) {
            tablero[6] = 'x';
        }
        if (pos==7) {
            tablero[7] = 'x';
        }
        if (pos==8) {
            tablero[8] = 'x';
        }

    }


    public static void mueveJugador2(int pos) {


    }

    public static boolean movimientoValido(int pos) {

        return true;

    }

    public static boolean ganaJugador1() {

        return true;

    }

    public static boolean ganaJugador2() {

return true;

    }

}