package ud4;

public class H4EJ11 {
    public static void main(String[] args) {
        // 11. Que rellene un array con los 100 primeros números pares y muestre su suma.

        //Definimos array
        int[] pares = new int[100];
        int j =0;
        int suma=0;
        //Hacemos bucle for
        for (int i=0;i<99;i=i++) {

            pares[i] = j + 2;
            j = j+2;
            System.out.println(pares[i]);
            i++;
            suma = suma + j;
        }
        System.out.println(suma);
            }


}
