package ud11;

import java.util.ArrayList;

public class ControladorTresEnRaya {

    private TresEnRaya modelo;
    private GestorTresEnRaya gestorBD;

    private int idJugadorLogueado;
    private int idPartidaActual;
    private int contadorMovimientos;

    public ControladorTresEnRaya() {
        this.modelo = new TresEnRaya();
        this.gestorBD = new GestorTresEnRaya();
    }

    public boolean iniciarSesion(String usuario, String pass) {
        int id = gestorBD.comprobarUsuario(usuario, pass);
        if (id != -1) {
            this.idJugadorLogueado = id;
            return true;
        }
        return false;
    }

    public void nuevaPartidaContraMaquina(int idPartida) {
        this.idPartidaActual = idPartida;
        this.contadorMovimientos = 0;
        modelo.iniciar();
    }

    public boolean turnoUsuario(int pos, String tableroVarchar) {
        if (modelo.movimientoValido(pos)) {
            modelo.mueveJugador1(pos);
            contadorMovimientos++;
            gestorBD.guardarMovimientoBD(idJugadorLogueado, idPartidaActual, contadorMovimientos, tableroVarchar);
            return true;
        }
        return false;
    }

    public void turnoMaquina(String tableroVarchar) {
        if (modelo.quedanMovimientos()) {
            modelo.mueveOrdenador2();
            contadorMovimientos++;
            gestorBD.guardarMovimientoBD(idJugadorLogueado, idPartidaActual, contadorMovimientos, tableroVarchar);
        }
    }

    public int comprobarEstadoPartida() {
        if (modelo.ganaJugador1()) {
            gestorBD.sumarPuntosJugador(idJugadorLogueado, 3);
            return 1;
        }
        if (modelo.ganaJugador2()) {
            return 2;
        }
        if (!modelo.quedanMovimientos()) {
            gestorBD.sumarPuntosJugador(idJugadorLogueado, 1);
            return 0;
        }
        return -1;
    }

    public ArrayList<String> verTop3() {
        return gestorBD.obtenerMejoresJugadores();
    }

    public int verMisPuntos() {
        return gestorBD.obtenerPuntosPropios(idJugadorLogueado);
    }

    public ArrayList<String> recrearPartidaHistorica(int idPartida) {
        return gestorBD.obtenerPartidaGuardada(idJugadorLogueado, idPartida);
    }
}