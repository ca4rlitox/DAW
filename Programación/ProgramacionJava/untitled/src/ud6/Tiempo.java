package ud6;

public class Tiempo {
    private int horas;
    private int minutos;
    private int segundos;

    //1º Constructor
    public Tiempo(int h) {
        if (h>=0 && h<=23) {
            horas = h;
        }
        else {
            horas = 0;
        }
        minutos=0;
        segundos=0;
    }

    //2º Constructor
    public Tiempo (int h,int m,int s) {
        horas=h;
        minutos=m;
        segundos=s;
    }

    //Metodos setter
    public void setHora (int h) {
        if (h>=0 && h<=23) {
            horas=h;
        }
    }
    public void setMinutos (int m) {
        if (m>=0 && m<=59) {
            minutos=m;
        }
    }
    public void setSegundos (int s) {
        if (s>=0 && s<=59) {
            segundos=s;
        }
    }

    //Metodos getter
    public int getHoras() {
        return horas;
    }
    public int getMinutos() {
        return minutos;
    }
    public int getSegundos() {
        return segundos;
    }
    public String toString() {
        return "Son las: "+getHoras()+":"+getMinutos()+":"+getSegundos();
    }

}
