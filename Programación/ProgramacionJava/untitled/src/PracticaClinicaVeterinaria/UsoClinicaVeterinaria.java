package PracticaClinicaVeterinaria;

public class UsoClinicaVeterinaria {
    public static void main(String[] args) {
        Gato gato1 = new Gato ("Firulais", "01/04/2005",25,"Persa","hy45tbc7842tg");
        ClinicaVeterinaria cv = new ClinicaVeterinaria();

        cv.insertaAnimal(gato1);

        System.out.println(cv.buscaAnimal("Firulais"));
    }
}
