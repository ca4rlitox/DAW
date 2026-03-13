package PracticaClinicaVeterinaria;

public class UsoClinicaVeterinaria {
    public static void main(String[] args) {
        ClinicaVeterinaria cv = new ClinicaVeterinaria();

        cv.insertaAnimal(new Gato("Firulais","01/04/2004",1,"Persa","fdsjfndsjuf"));
        cv.insertaAnimal(new Perro("Firulais","01/04/2004",1,"Persa","fdsjfndsjuf"));

        System.out.println(cv);

    }
}
