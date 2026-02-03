package ud6;

public class UsoPassword {
    public static void main(String[] args) {
        Password contra1 = new Password("AaBbCcXxDd324543");
        contra1.setContraseña("AaBbCcXxDd3245433");
        System.out.println(contra1.getContraseñayLength());


        System.out.println(contra1.esFuerte());
        System.out.println(contra1.generarPasswd(4));
        System.out.println(contra1.getContraseñayLength());
        Password contra2 = new Password();

        System.out.println(contra2);

            }
}
