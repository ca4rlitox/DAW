package ud9.InterfacesdeVentana;

import javax.swing.*;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.util.ArrayList;

public class Traductor_ingles_espanol extends JFrame implements ActionListener {
    private ArrayList<String> listaPalabras;
    private JPanel panel; //contenido que esta dentro de la ventana
    private JTextField campoTexto1,campoTexto2;
    private JButton botonIngles,botonEspanol;
    private JLabel espanol;
    private JLabel ingles;
    FileReader entrada;

    public Traductor_ingles_espanol() {
        try {
            panel = new JPanel();
            this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
            construirPanel();
            this.setVisible(true);
            this.setSize(300, 300);
        } catch (FileNotFoundException e) {
            System.out.println(e.getMessage());
        }
    }
    private void construirPanel() throws FileNotFoundException {
        panel.setBounds(300,300,300,300);
        espanol = new JLabel("Español");
        ingles = new JLabel("Inglés");
        botonEspanol = new JButton(">>");
        botonIngles = new JButton("<<");
        campoTexto1 = new JTextField(10);
        campoTexto2 = new JTextField(10);
        panel.add(espanol);
        panel.add(campoTexto1);
        panel.add(botonEspanol);
        panel.add(botonIngles);
        panel.add(ingles);
        panel.add(campoTexto2);
        botonIngles.addActionListener(this);
        botonEspanol.addActionListener(this);
        this.add(panel);
        leerArchivos();
    }

    @Override
    public void actionPerformed(ActionEvent actionEvent) {

    }

    private void leerArchivos() throws FileNotFoundException {
        try {
            entrada = new FileReader("/home/alumno/Escritorio/fich.txt");

        } catch (FileNotFoundException e) {
            System.out.println(e.getMessage());
        }
    }
}