package ud11;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class TresEnRaya extends JFrame implements ActionListener {
    private JPanel panel;
    private JLabel texto;
    private JButton boton1,boton2,boton3,boton4,boton5,boton6,boton7,boton8,boton9;

    public TresEnRaya() {
        construirPanel();
        this.add(panel);
        this.setVisible(true);
        this.setBounds(500,500,500,500);
    }

    private void construirPanel() {
        panel = new JPanel();
        texto = new JLabel("Tres en raya");
        boton1 = new JButton("");
        boton2 = new JButton("");
        boton3 = new JButton("");
        boton4 = new JButton("");
        boton5 = new JButton("");
        boton6 = new JButton("");
        boton7 = new JButton("");
        boton8 = new JButton("");
        boton9 = new JButton("");
        boton1.setBounds(300,300,300,300);
        panel.add(boton1);
        panel.add(boton2);
        panel.add(boton3);
        panel.add(boton4);
        panel.add(boton5);
        panel.add(boton6);
        panel.add(boton7);
        panel.add(boton8);
        panel.add(boton9);
    }

    @Override
    public void actionPerformed(ActionEvent actionEvent) {

    }
}
