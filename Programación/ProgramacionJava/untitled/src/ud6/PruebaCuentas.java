package ud6;

public class PruebaCuentas {
    public static void main(String[] args) {

    Cuenta cuentaUno=new Cuenta("1");
    Cuenta cuentaDos=new Cuenta("2");
    Persona personaUno=new Persona("07095334H");
    cuentaUno.recibirAbono(100);
    cuentaUno.pagarAbono(200);
    personaUno.addCuenta(cuentaUno );
    personaUno.addCuenta( cuentaDos );
    System.out.println(personaUno);
    if(personaUno.esMorosa()){
        System.out.println("La persona con DNI: "+personaUno.getDni()+" es Morosa");
    }else {
        System.out.println("La persona con DNI: "+personaUno.getDni()+" no esMorosa");
    }

    //Quiero ingresar 150 euros en la cuenta "2"
        personaUno.dameCuenta("2").recibirAbono(140);
        System.out.println(personaUno.esMorosa());
        personaUno.addCuenta(new Cuenta("3"));
        personaUno.dameCuenta("3").recibirAbono(140);
        System.out.println(personaUno.esMorosa());
    }
}
