import java.util.*;

public class Pracownik extends Intruz {
    // --Pola--
    //Pole statyczne
    public static int ni;

    // Blok statyczny (uruchamiany prze łądowaniu klasy)
    static{
        Random r = new Random();
        ni = r.nextInt(10);
    }
    // Pola instancji
    private int sn;
    private double wyplata;
    private Date DZad;

    // Inicjalizacja instancji
    {
        sn = ni;
        ni++;
    }
    // --Konstruktoru--

    // Główny
    public Pracownik(String n,double w, int d, int m, int r){
        super (n);
        this.wyplata = w;
        // Miesiące w GregorianCalendar są liczone od 0
        GregorianCalendar k = new GregorianCalendar(r, m - 1, d);
        DZad = k.getTime();
    }

    // --Metody--
    public int getSN(){
        return sn;
    }
    public double getWyplata() {
        return wyplata;
    }
    public Date getDZad(){
        return DZad;
    }
    public void premia(double p){
        wyplata += wyplata * p/100;
    }
    public String getOpis(){
        return String.format("w: %.2f zł", wyplata);
    }
}
