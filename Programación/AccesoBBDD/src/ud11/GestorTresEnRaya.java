package ud11;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;

public class GestorTresEnRaya {

    private Connection conexion;

    public GestorTresEnRaya() {
        try {
            conexion = DriverManager.getConnection("jdbc:mysql://localhost:3306/TresEnRaya", "admin", "1234");
        } catch (SQLException e) {
            System.out.println(e.getMessage());;
        }
    }

    public int comprobarUsuario(String usuario, String pass) {
        try {
            PreparedStatement ps = conexion.prepareStatement("SELECT id FROM jugador WHERE usuario = ? AND contraseña = ?");
            ps.setString(1, usuario);
            ps.setString(2, pass);
            ResultSet rs = ps.executeQuery();
            if (rs.next()) {
                return rs.getInt("id");
            }
        } catch (SQLException e) {
            System.out.println(e.getMessage());;
        }
        return -1;
    }

    public void guardarMovimientoBD(int idJugador, int idPartida, int numeroMovimiento, String estadoTablero) {
        try {
            PreparedStatement ps = conexion.prepareStatement("INSERT INTO partida (id_jugador, id_partida, numero_movimiento, tablero) VALUES (?, ?, ?, ?)");
            ps.setInt(1, idJugador);
            ps.setInt(2, idPartida);
            ps.setInt(3, numeroMovimiento);
            ps.setString(4, estadoTablero);
            ps.executeUpdate();
        } catch (SQLException e) {
            System.out.println(e.getMessage());;
        }
    }

    public void sumarPuntosJugador(int idJugador, int puntosNuevos) {
        try {
            PreparedStatement ps = conexion.prepareStatement("UPDATE jugador SET puntos = puntos + ? WHERE id = ?");
            ps.setInt(1, puntosNuevos);
            ps.setInt(2, idJugador);
            ps.executeUpdate();
        } catch (SQLException e) {
            System.out.println(e.getMessage());;
        }
    }

    public int obtenerPuntosPropios(int idJugador) {
        try {
            PreparedStatement ps = conexion.prepareStatement("SELECT puntos FROM jugador WHERE id = ?");
            ps.setInt(1, idJugador);
            ResultSet rs = ps.executeQuery();
            if (rs.next()) {
                return rs.getInt("puntos");
            }
        } catch (SQLException e) {
            System.out.println(e.getMessage());;
        }
        return 0;
    }

    public ArrayList<String> obtenerMejoresJugadores() {
        ArrayList<String> estadisticas = new ArrayList<>();
        try {
            PreparedStatement ps = conexion.prepareStatement("SELECT usuario, puntos FROM jugador ORDER BY puntos DESC LIMIT 3");
            ResultSet rs = ps.executeQuery();
            while (rs.next()) {
                estadisticas.add(rs.getString("usuario") + ": " + rs.getInt("puntos") + " puntos");
            }
        } catch (SQLException e) {
            System.out.println(e.getMessage());;
        }
        return estadisticas;
    }

    public ArrayList<String> obtenerPartidaGuardada(int idJugador, int idPartida) {
        ArrayList<String> movimientos = new ArrayList<>();
        try {
            PreparedStatement ps = conexion.prepareStatement("SELECT tablero FROM partida WHERE id_jugador = ? AND id_partida = ? ORDER BY numero_movimiento ASC");
            ps.setInt(1, idJugador);
            ps.setInt(2, idPartida);
            ResultSet rs = ps.executeQuery();
            while (rs.next()) {
                movimientos.add(rs.getString("tablero"));
            }
        } catch (SQLException e) {
            System.out.println(e.getMessage());;
        }
        return movimientos;
    }
}