import java.util.*;
import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
import javax.swing.Timer;


public class KlasaWew {
    static void main(String[] args) {
        Zegar z = new Zegar(2*1000, true);
        z.start();
        JOptionPane.showMessageDialog(null, "Dziala?");
        System.exit(0);
    }
}
class Zegar {
    private int odstep;
    private boolean ton;

    public Zegar(int odstep, boolean ton) {
        this.odstep = odstep;
        this.ton = ton;
    }

    public void start() {
        ActionListener al = new ZegarShow();
        Timer t = new Timer(odstep, al);
        t.start();
    }
    public class ZegarShow implements ActionListener{
        @Override
        public void actionPerformed(ActionEvent ae){
            Date d = new Date();
            System.out.println("Data: " +  d);
            if (ton) Toolkit.getDefaultToolkit().beep();
        }
    }
}
