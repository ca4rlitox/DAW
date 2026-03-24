package ud9.InterfacesdeVentana;

import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;


//marcamos la clase susceptible de recibir eventos de tipos click
//  implementando la interfaz ActionListener
public class Ventana1 extends JFrame implements ActionListener {
    //los atributos van a ser aquellos elementos gráficos que cambien
    //o generen elementos
    private JFrame v1;
    private JPanel panel;
    private JTextField campoTexto;
    private JButton botonSuma,botonResta;
    private JLabel etNombre,etSaludo;

    public Ventana1 () {
        //Construimos una ventana
        v1 = new JFrame("holaaaaaaaaaaaaaaaa");
        v1.setSize(300,300);
        v1.setLocation(100,100);
        v1.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        panel = new JPanel();
        campoTexto = new JTextField(20); // Pasamos por parametro el número máximo de caracteres.
        botonSuma = new JButton("+");
        botonResta = new JButton("-");
        etNombre = new JLabel("hola");
        panel.add(etNombre);
        panel.add(campoTexto);
        panel.add(botonSuma);
        panel.add(botonResta);
        //Asociamos un listener y la respuesta ante el evento de click al botón
        botonSuma.addActionListener(this);
        botonResta.addActionListener(this);
        //vinculo la respuesta al botón
        v1.add(panel);
        v1.setVisible(true);
        //Construyo la etiqueta saludo
        etSaludo = new JLabel("Hola");
        panel.add(etSaludo);

    }

    //Obligacion de sobreescribir, la respuesta al click
    @Override
    public void actionPerformed(ActionEvent actionEvent) {
        String nombre=campoTexto.getText();
        int contador=0;
        etSaludo.setText("Has pulsado el botón "+contador+" veces");
        System.out.println("Has pulsado el botón "+contador+" veces");

    }
}
