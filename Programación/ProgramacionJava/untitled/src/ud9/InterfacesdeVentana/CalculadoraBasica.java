package ud9.InterfacesdeVentana;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class CalculadoraBasica extends JFrame implements ActionListener {
    //atributosla ventana
    private JPanel panel; //contenido que esta dentro de la ventana
    private JTextField campoTexto1,campoTexto2;
    private JButton boton1,boton2;
    private JLabel resultado;
    double sumaOresta;

    public CalculadoraBasica() {
        sumaOresta=0;
        panel = new JPanel();
        boton1 = new JButton("Suma");
        boton2 = new JButton("Resta");
        // Añadimos campos de texto
        campoTexto1 = new JTextField();
        campoTexto2 = new JTextField();
        //Ajustamos el tamaño del campo de texto editable
        campoTexto1.setPreferredSize(new Dimension(20,20));
        campoTexto2.setPreferredSize(new Dimension(20,20));
        panel.add(campoTexto1);
        panel.add(campoTexto2);
        //añadir botones al panel
        panel.add(boton1);
        panel.add(boton2);
        //Ponemos el JLabel del resultado
        resultado = new JLabel();
        panel.add(resultado);
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
        if (e.getSource() == boton1) {
            double campoText1 = Double.parseDouble(campoTexto1.getText());
            double campoText2 = Double.parseDouble(campoTexto2.getText());
            sumaOresta = campoText1+campoText2;
            String hola = String.valueOf(sumaOresta);
            hola = hola.replace(".",",");
            resultado.setText(hola);
            resultado.setText(hola);
        }
        if (e.getSource() == boton2) {

            double campoText1 = Double.parseDouble(campoTexto1.getText());
            double campoText2 = Double.parseDouble(campoTexto2.getText());
            sumaOresta = campoText1-campoText2;
            String hola = String.valueOf(sumaOresta);
            hola = hola.replace(".",",");
            resultado.setText(hola);
        }
    }
}
