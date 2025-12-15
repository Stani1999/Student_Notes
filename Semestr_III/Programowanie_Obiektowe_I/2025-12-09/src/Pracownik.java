import java.util.*;

public class Pracownik {
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
    private String nazwa = "";
    private double pensja;
    private Date DZad;

    // Inicjalizacja instancji
    {
        sn = ni;
        ni++;
    }
    // --Konstruktoru--

    // Główny
    public Pracownik(String n, double p, int d, int m, int r){
        this.nazwa = n;
        this.pensja = p;
        // Miesiące w GregorianCalendar są liczone od 0
        GregorianCalendar k = new GregorianCalendar(r, m - 1, d);
        DZad = k.getTime();
    }

    // --Metody--
    public String getNazwa(){
        return nazwa;
    }
    public int getSN(){
        return sn;
    }
    public double getPensja() {
        return pensja;
    }
    public Date getDZad(){
        return DZad;
    }
    public void premia(double p){
        pensja += pensja * p/100;
    }
}
