package ud9.InterfacesdeVentana;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.Random;

public class EjercicioAdivino extends JFrame implements ActionListener {
    private JPanel panel;
    private JLabel et;
    private JTextField campoTexto;
    private JButton mayor,menor,igual;
    private int numAdivinar,min,max;
    private Random genAle;

    public EjercicioAdivino() {
    construirPanel();
    genAle = new Random();
    this.setBounds(300,300,300,300);
    this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    this.setVisible(true);
    }
    private void construirPanel() {
        numAdivinar = 50;
        min = 1;
        max = 100;
        panel = new JPanel();
        et = new JLabel("Número: ");
        campoTexto = new JTextField(20);
        campoTexto.setEditable(false);
        campoTexto.setText(String.valueOf(numAdivinar));
        mayor = new JButton(">");
        menor = new JButton("<");
        igual = new JButton("=");
        panel.add(et);
        panel.add(campoTexto);
        panel.add(mayor);
        panel.add(igual);
        panel.add(menor);
        this.add(panel);
        mayor.addActionListener(this);
        menor.addActionListener(this);
        igual.addActionListener(this);
    }



    @Override
    public void actionPerformed(ActionEvent e) {

        if (e.getSource() == mayor) {
            min=numAdivinar;
            numAdivinar = genAle.nextInt(min,max+1);
            campoTexto.setText(numAdivinar+"");
        }
        if (e.getSource() == menor) {
            max=numAdivinar-1;
            numAdivinar = genAle.nextInt(min,max);
            campoTexto.setText(numAdivinar+"");
        }
        if (e.getSource() == igual) {
            campoTexto.setText("Yujuuuuuuuu! He adivinado el número! Era el "+numAdivinar);
        }
    }
}
