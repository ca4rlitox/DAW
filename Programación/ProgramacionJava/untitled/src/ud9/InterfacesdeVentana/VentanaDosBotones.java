package ud9.InterfacesdeVentana;

import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class VentanaDosBotones extends JFrame implements ActionListener {
    //atributos
    private JPanel panel; //contenido que esta dentro de la ventana
    private JButton boton1,boton2;
    private int contador;

    public VentanaDosBotones() {
        this.contador = 0;
        panel = new JPanel();
        boton1 = new JButton("Boton 1");
        boton2 = new JButton("Boton 2");
        //añadir botones al panel
        panel.add(boton1);
        panel.add(boton2);
        //añadimos el panel a la ventana
        this.add(panel);
        //vinculamos el evento al boton
        boton1.addActionListener(this);
        boton2.addActionListener(this);
        //configuramos la ventana
        this.setSize(300,300);
        this.setLocation(100,100);
        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        this.setVisible(true);
    }

    @Override
    public void actionPerformed(ActionEvent e) {

        if (e.getSource()==boton1) {
            contador++;
            System.out.println(contador);
        }
        else {
            contador--;
            System.out.println(contador);
        }
    }
}
