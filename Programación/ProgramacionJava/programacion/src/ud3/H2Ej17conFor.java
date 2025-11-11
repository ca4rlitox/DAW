package ud3;

public class H2Ej17conFor {
    public static void main(String[] args) {

        //Inicializamos variables

        // Hacemos que cuente del 1 al 100
        for (int a=1;a<=100;a=a+1)
        {
            System.out.print(a+" ");
            //Aqui hacemos de un salto de página cuando el módulo de 10 de 0 (el caso de 10,20,30...)
            if(a%10==0) {
                System.out.println();
            }
        }

            }

        }




