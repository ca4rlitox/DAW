package ud6;

public class Tiempo {
    private int horas,minutos,segundos;

    //1º Constructor
    public Tiempo(int h,int m,int s) {
        this.setHora(h);
        this.setMinutos(m);
        this.setSegundos(s);
    }

    //2º Constructor
    public Tiempo (int h,int m) {
        this(h,m,0);
    }

    //3º Constructor
    public Tiempo(int h) {
        this(h,0,0);
    }

    //Metodos setter
    public void setHora (int h) {
        if (h>=0 && h<=23) {
            horas=h;
        } else {
            horas = 0;
        }
    }
    public void setMinutos (int m) {
        if (m>=0 && m<=59) {
            minutos=m;
        }else{
            minutos = 0;
        }
    }
    public void setSegundos (int s) {
        if (s>=0 && s<=59) {
            segundos=s;
        }else{
            segundos=0;
        }
    }

    public int añadirSegundo() {
        segundos++;
        if (segundos > 59) {
            segundos = 0;
            minutos++;
        }
        if (minutos > 59) {
            segundos=0;
            minutos=0;
            horas++;
        }
        if (horas > 23) {
            horas=0;
            minutos=0;
            segundos=0;
        }
        return segundos;
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
