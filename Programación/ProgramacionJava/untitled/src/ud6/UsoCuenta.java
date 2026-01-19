package ud6;

public class UsoCuenta {
    public static void main(String[] args) {
        Cuenta cuenta1 = new Cuenta("Paco");
        cuenta1.setCantidad(40.25);

        cuenta1.ingresar(-25);
        System.out.println(cuenta1.toString());

        cuenta1.retirar(200);
        System.out.println(cuenta1.toString());

        Cuenta cuenta2 = new Cuenta("Maria");
        System.out.println(cuenta2.toString());
    }
}
