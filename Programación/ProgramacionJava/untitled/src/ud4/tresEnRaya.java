package ud4;

import java.util.Scanner;

public class tresEnRaya {
    static Scanner in = new Scanner(System.in);
    static char[] tablero = new char[9];
    static char fichaJugador1;
    static char fichaJugador2;

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
                    //Solicitamos mediante una función que el jugador 1 elija su ficha.
                    seleccionarFichas();

                    do {
                        //Dibujamos el tablero si empieza, o cada ronda
                        dibujaTablero();
                        //Pedimos movimiento al jugador 1
                        System.out.println("Introduzca movimiento (Jugador 1):\n");
                        jugador1 = in.nextInt();
                        //En la funcion mueveJugador1 verificamos si el movimiento con la funcion movimientoValido es válido y hacemos el movimiento
                        mueveJugador1(jugador1);
                        dibujaTablero();

                        //Comprobamos mediante la funcion ganaJugador1 si están las piezas puestas para ganar, y si lo están termina la partida y
                        //suma a la estadística una victoria para el jugador 1.
                        if (ganaJugador1()) {
                            muestraResultado();
                            estadisticas++;
                            break;
                        }

                        if (!quedanCasillas() && esEmpate()) {
                            muestraResultado();
                            break;
                        }

                        System.out.println("Introduzca movimiento (Jugador 2):\n");
                        jugador2 = in.nextInt();
                        //En la funcion mueveJugador2 verificamos si el movimiento con la funcion movimientoValido es válido y hacemos el movimiento
                        mueveJugador2(jugador2);
                        dibujaTablero();
                        //Comprobamos mediante la funcion ganaJugador2 si están las piezas puestas para ganar, y si lo están termina la partida y
                        //suma a la estadística una victoria para el jugador 2.
                        if (ganaJugador2()) {
                            muestraResultado();
                            estadisticas2++;
                            break;
                        }
                        // Verificamos si quedan casillas después de que el jugador2 ha puesto.
                            if (!quedanCasillas() && esEmpate()) {
                                muestraResultado();
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
        //Con un bucle for ponemos un espacio en cada array para que se vea vacio y limpiamos las fichas de los jugadores con la variable creada.
        char vaciar=' ';
        fichaJugador1= vaciar;
        fichaJugador2= vaciar;

        for (int i=0;i<9;i++) {
            tablero[i] = vaciar;
        }

    }

    public static void seleccionarFichas() {
        // Limpiamos buffer del teclado ya que si no salta error OutOfBounds.
        in.nextLine();
        // Pedimos al jugador 1 que elija ficha.
        System.out.println("Jugador 1, elige la ficha. Tiene que ser X o O.");
        fichaJugador1 = in.nextLine().charAt(0);
        if (fichaJugador1 != 'X' && fichaJugador1 != 'O') {
            do {
                System.out.println("Ficha elegida no válida. Tiene que ser X o O.");
                fichaJugador1 = in.nextLine().charAt(0);
            } while (fichaJugador1 != 'X' && fichaJugador1 != 'O');
        }

        // Aqui le damos la ficha sobrante al jugador 2
        if (fichaJugador1 == 'X') {
            fichaJugador2 = 'O';
        }
        else {
            fichaJugador2 = 'X';
        }

    }

    public static void mueveJugador1(int pos) {
        //Revisamos si el movimiento es válido y si no, entra en un do while hasta que lo meta en una casilla libre.
        if (!movimientoValido(pos)) {
            do {
                System.out.println("Intentalo otra vez. Movimiento inválido.");
                pos = in.nextInt();
            }while (!movimientoValido(pos));
        }
        //Una vez verificado que la casilla está libre, se coloca la ficha.
        tablero[pos - 1] = fichaJugador1;

    }


    public static void mueveJugador2(int pos) {
        //Revisamos si el movimiento es válido y si no, entra en un do while hasta que lo meta en una casilla libre.
        if (!movimientoValido(pos)) {
            do {
                System.out.println("Intentalo otra vez. Movimiento inválido.");
                pos = in.nextInt();
            }while (!movimientoValido(pos));
        }
        //Una vez verificado que la casilla está libre, se coloca la ficha.
        tablero[pos - 1] = fichaJugador2;

    }

    public static boolean movimientoValido(int pos) {
        //Con una estructura if, revisamos si donde se quiere poner la ficha está libre, si está libre devuelve true y si no, false.
        if (tablero[pos - 1]==' ') {

            return true;

        }
        return false;
    }

    public static boolean quedanCasillas() {
        //Aquí revisamos en cada array si hay espacios vacios, si no hay espacios vacios en el array, se devuelve false para terminar la partida.
        for (int i = 0;i<9;i++) {
            if (tablero[i]==' ') {
                return true;
            }
        }
                return false;
        }


    public static boolean ganaJugador1() {

        //Aqui comprobamos las posiciones para ver si el jugador 1 ha ganado.
        if ((tablero[0]==fichaJugador1) && (tablero[4]==fichaJugador1) && (tablero[8]==fichaJugador1)) {

            return true;
        }
        else if ((tablero[2]==fichaJugador1) && (tablero[4]==fichaJugador1) && (tablero[6]==fichaJugador1)) {

            return true;
        }
        else if ((tablero[0]==fichaJugador1) && (tablero[1]==fichaJugador1) && (tablero[2]==fichaJugador1)) {

            return true;
        }
        else if ((tablero[3]==fichaJugador1) && (tablero[4]==fichaJugador1) && (tablero[5]==fichaJugador1)) {

            return true;
        }
        else if ((tablero[6]==fichaJugador1) && (tablero[7]==fichaJugador1) && (tablero[8]==fichaJugador1)) {

            return true;
        }
        else if ((tablero[0]==fichaJugador1) && (tablero[3]==fichaJugador1) && (tablero[6]==fichaJugador1)) {

            return true;
        }
        else if ((tablero[1]==fichaJugador1) && (tablero[4]==fichaJugador1) && (tablero[7]==fichaJugador1)) {

            return true;
        }
        else if ((tablero[2]==fichaJugador1) && (tablero[5]==fichaJugador1) && (tablero[8]==fichaJugador1)) {

            return true;
        }

        return false;

    }

    public static boolean ganaJugador2() {

        //Aqui comprobamos las posiciones para ver si el jugador 2 ha ganado.
        if ((tablero[0]==fichaJugador2) && (tablero[4]==fichaJugador2) && (tablero[8]==fichaJugador2)) {

            return true;
        }
        else if ((tablero[2]==fichaJugador2) && (tablero[4]==fichaJugador2) && (tablero[6]==fichaJugador2)) {

            return true;
        }
        else if ((tablero[0]==fichaJugador2) && (tablero[1]==fichaJugador2) && (tablero[2]==fichaJugador2)) {

            return true;
        }
        else if ((tablero[3]==fichaJugador2) && (tablero[4]==fichaJugador2) && (tablero[5]==fichaJugador2)) {

            return true;
        }
        else if ((tablero[6]==fichaJugador2) && (tablero[7]==fichaJugador2) && (tablero[8]==fichaJugador2)) {

            return true;
        }
        else if ((tablero[0]==fichaJugador2) && (tablero[3]==fichaJugador2) && (tablero[6]==fichaJugador2)) {

            return true;
        }
        else if ((tablero[1]==fichaJugador2) && (tablero[4]==fichaJugador2) && (tablero[7]==fichaJugador2)) {

            return true;
        }
        else if ((tablero[2]==fichaJugador2) && (tablero[5]==fichaJugador2) && (tablero[8]==fichaJugador2)) {

            return true;
        }

        return false;

    }

    public static boolean esEmpate () {
        //Comprobamos si las casillas están ocupadas con la funcion quedanCasillas
            if (!quedanCasillas()) {
                return true;
            }

        return false;
    }

    public static void muestraResultado () {
        //Mostramos el mensaje de si ha ganado el jugador 1.
        if (ganaJugador1()) {
            System.out.println("¡Ha ganado el jugador 1!");
        }
        //Mostramos el mensaje de si ha ganado el jugador 1.
        else if (ganaJugador2()) {
            System.out.println("¡Ha ganado el jugador 2!");
        }
        //Mostramos el mensaje si la partida ha quedado en empate.
        else if (esEmpate()) {
            System.out.println("La partida queda en empate.");
        }
    }
    }
