package ud7;

public class UsoUniversidad {
    public static void main(String[] args) {
        Persona [] personas  = new Persona[6];
        personas[0] = new Profesor("Juan","Lopez", "DCSFR45A","casade","27/02/2022",5,"informatica");
        personas[1] = new PersonaldeServicio("Petro","Gurierrez","7537484W","solteraYentera","07/04/1996",4,"limpieza");
        personas[2] = new Persona("Miguel","Lopez","147484W","solteraYentera");

        for (int i = 0; i < 2; i++) {
            System.out.println(personas[i].toString());
        }
        int profes = 0,estus=0,ps=0;

        for (int i = 0; i < personas.length; i++) {
            if(personas[i] != null) {
                if (personas[i] instanceof Profesor) {
                    profes++;
                }
                if (personas[i] instanceof PersonaldeServicio) {
                    ps++;
                }
                if (personas[i] instanceof Estudiantes) {
                    estus++;
                }
            }
        }
        System.out.println("Hay "+profes+" profes");
        // Forzado de tipo para que una subclase se comporte como otra subclase (casting o casteo),
        // cuando queremos que un objeto de tipo mas generico (Persona) se comporte como un objeto
        // de tipo mas complejo
        if (personas[1] instanceof Profesor) {
            ((Estudiantes) personas[0]).estoyHablando();
        }
        else {
            System.out.println("cacho puta");
        }

        //Quiero que todos los profesores del array expliquen
        for (int i = 0; i < personas.length; i++) {
            if (personas[i] != null) {
                if (personas[i] instanceof Profesor) {
                    System.out.println(personas[i].getNombre());
                    ((Profesor) personas[i]).estoyExplicando();
                }
            }
        }
    }
}
