package ud6;

public class Clase {
    private Notas[] notas;
    private int numAlumnos;

    public Clase() {
        notas = new Notas[20];
        numAlumnos=0;
    }

    public boolean darAlta(Notas notas) {
        if (numAlumnos>20) {
            return false;
        }
        this.notas[numAlumnos] = notas;
        numAlumnos++;
        return true;
    }

    public Notas buscarNotas(String nombre) {
        for (int i = 0; i < numAlumnos; i++) {
            Notas n = notas[i];
            if (n.getNombre().equals(nombre)) {
                return notas[i];
            }
        }
        return null;
    }

    public boolean modificarNota(String nombre, double nota) {
        for (int i = 0; i < numAlumnos; i++) {
            Notas n = notas[i];
            if (n.getNombre().equals(nombre)) {
                notas[i].setNota(nota);
                return true;
            }
        }
        return false;
    }
    public double realizarMedia() {
        double resultado = 0;
        for (int i = 0; i < numAlumnos; i++) {
            resultado += notas[i].getNota();
        }
        resultado = resultado / numAlumnos;
        return resultado;
    }
    public double realizarMediaMenorA5() {
        double resultado = 0;
        int menoresA5=0;
        for (int i = 0; i < numAlumnos; i++) {
            if (notas[i].getNota() < 5) {
                resultado += notas[i].getNota();
                menoresA5++;
            }
        }
        resultado = resultado / menoresA5;
        return resultado;
    }
    public Notas alumnoConMasNota() {
        double mayor = 0;
        Notas conMas = null;
        for (int i = 0; i < numAlumnos; i++) {
            Notas n =  notas[i];
            if (n.getNota() > mayor) {
                mayor = n.getNota();
                conMas = notas[i];
            }
        }
        return conMas;
    }
    public String alumnoConMenosNota() {
        double menor = 10;
        Notas conMenos = null;
        String tS = "";
        for (int i = 0; i < numAlumnos; i++) {
            Notas n =  notas[i];
            if (n.getNota() < menor) {
                menor = n.getNota();
                conMenos = notas[i];
            }
            tS= conMenos.toString();
        }
        return tS;
    }

    public String toString() {
        String tS="";
        for (int i = 0; i < numAlumnos; i++) {
            tS+=notas[i].toString()+"\n";
        }
        return tS;
    }

}
