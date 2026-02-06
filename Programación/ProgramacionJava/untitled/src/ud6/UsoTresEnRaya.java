package ud6;

import java.util.Scanner;

public class UsoTresEnRaya {
    public static void main(String[] args) {
        TresEnRaya tresEnRaya = new TresEnRaya();
        Scanner entrada = new Scanner(System.in);
        int opcion=0;
        int pos;
        String continuarPartidaRobotica;

        do {
            System.out.println("1. Jugar partida humana");
            System.out.println("2. Jugar partida contra un robot");
            System.out.println("3. Ver una partida róbotica");
            System.out.println("4. Salir");
            opcion= entrada.nextInt();
            switch (opcion) {
                case 1:
                    tresEnRaya.iniciar();
                    tresEnRaya.DibujaTablero();
                    do {
                        System.out.println("Jugador 1, te toca mover: ");
                        pos = entrada.nextInt();
                        if (!tresEnRaya.movimientoValido(pos)) {
                            do {
                                System.out.println("No se puede realizar la tirada. Inténtalo otra vez.");
                                pos = entrada.nextInt();
                            } while (!tresEnRaya.movimientoValido(pos));
                        }
                        tresEnRaya.mueveJugador1(pos);
                        tresEnRaya.DibujaTablero();
                        if (tresEnRaya.ganaJugador1()) {
                            System.out.println("Ha ganado el jugador 1!");
                            break;
                        }
                        if (!tresEnRaya.quedanMovimientos()) {
                            System.out.println("Ya no quedan movimientos. Queda en tablas la partida.");
                            break;
                        }
                        System.out.println("Jugador 2, te toca mover: ");
                        pos = entrada.nextInt();
                        if (!tresEnRaya.movimientoValido(pos)) {
                            do {
                                System.out.println("No se puede realizar la tirada. Inténtalo otra vez.");
                                pos = entrada.nextInt();
                            } while (!tresEnRaya.movimientoValido(pos));
                        }
                        tresEnRaya.mueveJugador2(pos);
                        tresEnRaya.DibujaTablero();
                        if (tresEnRaya.ganaJugador2()) {
                            tresEnRaya.DibujaTablero();
                            System.out.println("Ha ganado el jugador 2!");
                            break;
                        }
                        if (!tresEnRaya.quedanMovimientos()) {
                            tresEnRaya.DibujaTablero();
                            System.out.println("Ya no quedan movimientos. Queda en tablas la partida.");
                            break;
                        }
                    } while (tresEnRaya.quedanMovimientos() || !tresEnRaya.ganaJugador1() || !tresEnRaya.ganaJugador2());
                    break;
                case 2:
                    tresEnRaya.iniciar();
                    tresEnRaya.DibujaTablero();
                    do {
                        System.out.println("Jugador 1, te toca mover: ");
                        pos = entrada.nextInt();
                        if (!tresEnRaya.movimientoValido(pos)) {
                            do {
                                System.out.println("No se puede realizar la tirada. Inténtalo otra vez.");
                                pos = entrada.nextInt();
                            } while (!tresEnRaya.movimientoValido(pos));
                        }
                        tresEnRaya.mueveJugador1(pos);
                        tresEnRaya.DibujaTablero();
                        if (tresEnRaya.ganaJugador1()) {
                            System.out.println("Ha ganado el jugador 1!");
                            break;
                        }
                        if (!tresEnRaya.quedanMovimientos()) {
                            System.out.println("Ya no quedan movimientos. Queda en tablas la partida.");
                            break;
                        }
                        System.out.println("Tirada robótica: ");
                        tresEnRaya.mueveOrdenador2();
                        tresEnRaya.DibujaTablero();
                        if (tresEnRaya.ganaJugador2()) {
                            System.out.println("Ha ganado el robot!");
                            break;
                        }
                        if (!tresEnRaya.quedanMovimientos()) {
                            System.out.println("Ya no quedan movimientos. Queda en tablas la partida.");
                            break;
                        }
                    } while (tresEnRaya.quedanMovimientos() || !tresEnRaya.ganaJugador1() || !tresEnRaya.ganaJugador2());
                    break;
                case 3:
                    tresEnRaya.iniciar();
                    tresEnRaya.DibujaTablero();
                    do {
                        System.out.println("Tirada robótica: ");
                        tresEnRaya.mueveOrdenador1();
                        tresEnRaya.DibujaTablero();
                        if (tresEnRaya.ganaJugador1()) {
                            System.out.println("Ha ganado el robot 1!");
                            break;
                        }
                        if (!tresEnRaya.quedanMovimientos()) {
                            System.out.println("Ya no quedan movimientos. Queda en tablas la partida.");
                            break;
                        }
                        tresEnRaya.mueveOrdenador2();
                        tresEnRaya.DibujaTablero();
                        if (tresEnRaya.ganaJugador2()) {
                            System.out.println("Ha ganado el robot 2!");
                            break;
                        }
                        if (!tresEnRaya.quedanMovimientos()) {
                            System.out.println("Ya no quedan movimientos. Queda en tablas la partida.");
                            break;
                        }
                    } while (tresEnRaya.quedanMovimientos() || !tresEnRaya.ganaJugador1() || !tresEnRaya.ganaJugador2());
                case 4:
                    break;
                default:
                    System.out.println("Opción no válida, inténtalo otra vez.");
            }
        }while (opcion!=4);
        System.out.println("Has salido correctamente.");
    }
}
