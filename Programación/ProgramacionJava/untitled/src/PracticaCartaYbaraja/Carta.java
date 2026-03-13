package PracticaCartaYbaraja;

public class Carta {
    private int numero;
    private int palo;

    public Carta(int numero, int palo) {
        setNumero(numero);
        setPalo(palo);
    }
    public Carta(int id) {
        setNumyPalo(id);
    }
    private void setNumyPalo(int num) {
        int oros,copas,espadas,bastos;
        for (int i = 1; i < 41; i++) {
            if (num >= 1 && num <=10) {
                this.numero = num;
                palo = 0;
                i=41;
            }
            if (num >= 11 && num <= 20) {
                this.numero = num-10;
                palo = 1;
                i=41;
            }
            if (num >= 21 && num <= 30) {
                this.numero = num-20;
                palo = 2;
                i=41;
            }
            if (num >= 31 && num <= 40) {
                this.numero = num-30;
                palo = 3;
                i=41;
            }
        }
        if (num < 1 || num > 40) {
            numero = -1;
            palo = -1;
        }
    }
    private void setNumero(int num) {
        if (num >= 1 && num <=10) {
            this.numero = num;
        }
        else {
            this.numero = 0;
        }
    }
    private void setPalo(int palo) {
        if (palo >= 0 && palo <= 3) {
            this.palo = palo;
        }
        else {
            this.palo = 0;
        }
    }

    public int getNumero() {
        return numero;
    }

    public int getPalo() {
        return palo;
    }
    public String NombreNumero() {
        if (this.numero == 1) return "as";
        if (this.numero == 2) return "dos";
        if (this.numero == 3) return "tres";
        if (this.numero == 4) return "cuatro";
        if (this.numero == 5) return "cinco";
        if (this.numero == 6) return "seis";
        if (this.numero == 7) return "siete";
        if (this.numero == 8) return "sota";
        if (this.numero == 9) return "caballo";
        if (this.numero == 10) return "rey";
        return "";
    }
    public String NombreCarta () {
        String cad="";
        for (int i = 0; i < 40; i++) {
            if (this.numero >= 1 && this.numero <=10) {
                cad+=NombreNumero();
                cad+=" de oros";
                return cad;
            }
            if (this.numero >= 11 && this.numero <= 20) {
                cad+=NombreNumero();
                cad+=" de copas";
                return cad;
            }
            if (this.numero >= 21 && this.numero <= 30) {
                cad+=NombreNumero();
                cad+=" de espadas";
                return cad;
            }
            if (this.numero >= 31 && this.numero <= 40) {
                cad+=NombreNumero();
                cad+=" de bastos";
                return cad;
            }
        }
        return cad;
    }
    public int ValorTute(Carta carta) {
        if (carta.numero == 1) return 11;
        if (carta.numero == 3) return 10;
        if (carta.numero == 10) return 2;
        if (carta.numero == 11) return 3;
        if (carta.numero == 12) return 4;
        return 0;
    }
    public int ValorMus(Carta carta) {
        if (carta.numero == 1 || carta.numero == 2) return 1;
        if (carta.numero == 8  || carta.numero == 9 || carta.numero == 10) return 10;
        else return carta.getNumero();
    }
    public double Valor7ymedia(Carta carta) {
        if (carta.getNumero() > 0 && carta.getNumero() < 8) return carta.getNumero();
        if (carta.getNumero() > 7) return 0.5;
        return 0;
    }

}
