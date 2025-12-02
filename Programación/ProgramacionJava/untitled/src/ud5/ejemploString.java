package ud5;

public class ejemploString {

    public static void main(String[] args) {

        String cad1=new String();
        cad1="hola";
        cad1=cad1+" a todos";

        System.out.println(cad1+" la longitud de la cadena es "+cad1.length());
        System.out.println("El primer caracter es "+cad1.charAt(cad1.length()-1));
        cad1=cad1.toUpperCase();
        System.out.println(cad1);

    }
}
