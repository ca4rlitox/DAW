package ud4;

public class EjemploInicializarArray2D {
    public static void main(String[] args) {

        int[][] sudoku = {
                {5, 3, 4, 6, 7, 8, 9, 1, 2},
                {6, 7, 2, 1, 9, 5, 3, 4, 8},
                {1, 9, 8, 3, 4, 2, 5, 6, 7},

                {8, 5, 9, 7, 6, 1, 4, 2, 3},
                {4, 2, 6, 8, 5, 3, 7, 9, 1},
                {7, 1, 3, 9, 2, 4, 8, 5, 6},

                {9, 6, 1, 5, 3, 7, 2, 8, 4},
                {2, 8, 7, 4, 1, 9, 6, 3, 5},
                {3, 4, 5, 2, 8, 6, 1, 7, 9}
        };

        validarSudoku(sudoku);

    }
    //Creamos una funcion para validar el sudoku
    public static boolean validarSudoku (int[][] sudoku) {
        //Inicializamos booleanos para comprobas filas, cubos y columnas.
        boolean filas;
        boolean cubo=true;
        boolean columnas;

        // Primero comprobamos que la fila no tenga el mismo número repetido

        for (int i = 0;i<9;i++) {
            for (int j = 0;i<9;i++) {

            if (sudoku[i][j] == sudoku[i][j]) {

            }
            }

        }

        return cubo;


    }
}
