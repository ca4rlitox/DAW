package ud4;

public class H4Ej15 {

    public static void main(String[] args) {
        char[][] tablero = new char[8][8];
        //Inicializamos todo a cero.
        for (int i = 0; i < 8; i++) {
            for (int j = 0; j < 8; j++) {
                tablero[i][j] = ' ';
            }
        }
        //Rellenamos la primera fila
        tablero[0][0] = 'T';
        tablero[0][1] = 'C';
        tablero[0][2] = 'A';
        tablero[0][3] = 'M';
        tablero[0][4] = 'R';
        tablero[0][5] = 'A';
        tablero[0][6] = 'C';
        tablero[0][7] = 'T';


        //Rellenamos la última fila rellenandolo con la primera.
        for (int i = 0; i < 8; i++) {
            tablero[7][i] = tablero[0][i];
        }
        //Ponemos todos los peones en el tablero.
        for (int i = 0; i < 8; i++) {
            tablero[1][i] = tablero[0][i];
            tablero[6][i] = tablero[0][i];
        }

        //Mostramos el tablero
        //Contador de fila
        for (int i = 0; i < 8; i++) {
            for (int j = 0; j < 8; j++) {
                System.out.print(tablero[i][j]+" ");
            }
            //Salto de línea tras cada fila
            System.out.println();
        }
    }
}
