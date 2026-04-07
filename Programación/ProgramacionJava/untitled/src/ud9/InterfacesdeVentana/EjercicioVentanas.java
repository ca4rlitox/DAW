package ud9.InterfacesdeVentana;

import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class EjercicioVentanas extends JFrame implements ActionListener {
/* Hacer una ventana para la cual se pida si quieres ir a la principal o a la otra*/

    private JPanel panel1,panel2;
    private JLabel et;
    private JButton boton1,boton2;

    public EjercicioVentanas() {
        construirPanel();
    }

    private void construirPanel() {
        panel1 = new JPanel();
        panel2 = new JPanel();
        panel1.setBounds(300,300,300,300);
        panel2.setBounds(100,100,300,300);
        et = new JLabel("¿Quieres ir a la otra ventana?");
        boton1 = new JButton("Ventana 1");
        boton2 = new JButton("Ventana 2");
        this.add(panel1);
        this.add(panel2);
        panel1.add(et);
        panel2.add(et);
        panel1.add(boton1);
        panel1.add(boton2);
        panel2.add(boton1);
        panel2.add(boton2);
        boton1.addActionListener(this);
        boton2.addActionListener(this);
        panel1.setVisible(true);
        panel2.setVisible(true);

    }





    @Override
    public void actionPerformed(ActionEvent e) {
        if (e.getSource() == boton1) {
            panel2.setVisible(false);
        }
        if (e.getSource() == boton2) {
            panel1.setVisible(false);
        }
    }

    public static void main (String[] args) {
        EjercicioVentanas eV = new EjercicioVentanas();
    }
}

