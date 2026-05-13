package ud11;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JPanel;
import java.awt.GridLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class VistaTresEnRaya extends JFrame {

    private ControladorTresEnRaya controlador;
    private JButton[] botones;

    public VistaTresEnRaya() {
        controlador = new ControladorTresEnRaya();
        botones = new JButton[9];

        setTitle("Tres en Raya");
        setSize(400, 400);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        JPanel panel = new JPanel();
        panel.setLayout(new GridLayout(3, 3));

        for (int i = 0; i < 9; i++) {
            botones[i] = new JButton("");
            int pos = i + 1;
            botones[i].addActionListener(new ActionListener() {
                public void actionPerformed(ActionEvent e) {
                    jugar(pos);
                }
            });
            panel.add(botones[i]);
        }

        add(panel);
        setVisible(true);
    }

    private void jugar(int pos) {
        String estadoActual = obtenerEstadoTablero();

        if (controlador.turnoUsuario(pos, estadoActual)) {
            botones[pos - 1].setText("X");
            controlador.turnoMaquina(estadoActual);
            actualizarTableroVisual();
        }
    }

    private String obtenerEstadoTablero() {
        return "000000000";
    }

    private void actualizarTableroVisual() {
    }

    public static void main(String[] args) {
        new VistaTresEnRaya();
    }
}